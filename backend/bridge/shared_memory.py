"""
Read-only access to an existing named Windows shared-memory section.

``mmap`` is deliberately not used here. On Windows, Python's ``mmap`` with a
tagname goes through ``CreateFileMapping``, which *creates* the section if it
does not already exist — so a missing HWiNFO would silently yield a mapping full
of zeroes instead of an error, and worse, could occupy the name HWiNFO wants
when it next starts. It also rejects a zero length against an anonymous handle,
so the size cannot be discovered that way either.

``OpenFileMappingW`` has exactly the semantics wanted: open an existing section
or fail.
"""
import ctypes
from ctypes import wintypes

FILE_MAP_READ = 0x0004
_IS_64BIT = ctypes.sizeof(ctypes.c_void_p) == 8

_kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

_kernel32.OpenFileMappingW.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.LPCWSTR]
_kernel32.OpenFileMappingW.restype = wintypes.HANDLE

_kernel32.MapViewOfFile.argtypes = [
    wintypes.HANDLE,
    wintypes.DWORD,
    wintypes.DWORD,
    wintypes.DWORD,
    ctypes.c_size_t,
]
_kernel32.MapViewOfFile.restype = ctypes.c_void_p

_kernel32.UnmapViewOfFile.argtypes = [ctypes.c_void_p]
_kernel32.UnmapViewOfFile.restype = wintypes.BOOL

_kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
_kernel32.CloseHandle.restype = wintypes.BOOL


class _MemoryBasicInformation(ctypes.Structure):
    _fields_ = (
        [
            ("BaseAddress", ctypes.c_void_p),
            ("AllocationBase", ctypes.c_void_p),
            ("AllocationProtect", wintypes.DWORD),
            ("__alignment1", wintypes.DWORD),
            ("RegionSize", ctypes.c_size_t),
            ("State", wintypes.DWORD),
            ("Protect", wintypes.DWORD),
            ("Type", wintypes.DWORD),
            ("__alignment2", wintypes.DWORD),
        ]
        if _IS_64BIT
        else [
            ("BaseAddress", ctypes.c_void_p),
            ("AllocationBase", ctypes.c_void_p),
            ("AllocationProtect", wintypes.DWORD),
            ("RegionSize", ctypes.c_size_t),
            ("State", wintypes.DWORD),
            ("Protect", wintypes.DWORD),
            ("Type", wintypes.DWORD),
        ]
    )


_kernel32.VirtualQuery.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(_MemoryBasicInformation),
    ctypes.c_size_t,
]
_kernel32.VirtualQuery.restype = ctypes.c_size_t


class SharedMemoryError(OSError):
    """The named section could not be opened or read."""


class SharedMemoryView:
    """A read-only view over an existing named section."""

    def __init__(self, name: str) -> None:
        self.name = name
        handle = _kernel32.OpenFileMappingW(FILE_MAP_READ, False, name)
        if not handle:
            raise SharedMemoryError(
                ctypes.get_last_error(), f"could not open shared memory {name!r}"
            )

        address = _kernel32.MapViewOfFile(handle, FILE_MAP_READ, 0, 0, 0)
        if not address:
            error = ctypes.get_last_error()
            _kernel32.CloseHandle(handle)
            raise SharedMemoryError(error, f"could not map a view of {name!r}")

        self._handle = handle
        self._address = address
        self.size = self._region_size(address)

    @staticmethod
    def _region_size(address: int) -> int:
        info = _MemoryBasicInformation()
        queried = _kernel32.VirtualQuery(
            ctypes.c_void_p(address), ctypes.byref(info), ctypes.sizeof(info)
        )
        if not queried:
            # Without a size the caller cannot bounds-check; treat as unusable.
            raise SharedMemoryError(ctypes.get_last_error(), "VirtualQuery failed")
        return int(info.RegionSize)

    def read(self, offset: int, size: int) -> bytes:
        """Copy ``size`` bytes out of the view.

        Reads are unsynchronised — the publisher may be mid-update. Individual
        aligned 8-byte values are atomic on x64, so a sample can mix values from
        two updates but never a torn number.
        """
        if offset < 0 or size < 0 or offset + size > self.size:
            raise SharedMemoryError(
                0, f"read of {size} bytes at {offset} exceeds the {self.size}-byte view"
            )
        return ctypes.string_at(self._address + offset, size)

    def close(self) -> None:
        if self._address:
            _kernel32.UnmapViewOfFile(ctypes.c_void_p(self._address))
            self._address = 0
        if self._handle:
            _kernel32.CloseHandle(self._handle)
            self._handle = None

    def __enter__(self) -> "SharedMemoryView":
        return self

    def __exit__(self, *_exc) -> None:
        self.close()
