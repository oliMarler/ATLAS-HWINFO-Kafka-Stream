@echo off
setlocal

rem ensure we're running from the repo root even when the script is double-clicked
pushd "%~dp0.."

echo ========================================
echo   HWiNFO ATLAS Bridge - Starting Up
echo ========================================
echo.

echo [1/3] Starting Docker containers (Kafka, Stream API, Key Generator)...
docker compose up -d --wait
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Docker failed to start. Make sure Docker Desktop is running.
    pause
    exit /b 1
)
echo       Docker containers are healthy.
echo.

echo [2/3] Installing Python dependencies...
cd backend
py -m pip install -r requirements.txt --quiet
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Failed to install Python dependencies.
    echo Make sure Python 3.10+ is installed and on your PATH.
    pause
    exit /b 1
)
echo       Dependencies installed.
echo.

echo [3/3] Starting the bridge server...
echo.
echo ========================================
echo   Open your browser to:
echo   http://localhost:8888
echo ========================================
echo.
echo   Reminder: HWiNFO must be running with
echo   Settings ^> Main Settings ^> Shared Memory
echo   Support enabled.
echo.
echo   Press Ctrl+C to stop the server.
echo.
py -m uvicorn main:app --host 0.0.0.0 --port 8888

echo.
echo Server stopped. Shutting down Docker containers...
cd ..
docker compose down
echo Docker containers stopped.
pause
popd
