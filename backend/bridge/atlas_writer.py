"""
AtlasWriter — writes telemetry data to Atlas via the Stream API's gRPC services.

  1. SessionManagementService to create/end sessions
  2. DataFormatManagerService to register per-parameter data format IDs
  3. PacketWriterService to write all packets

The packet ordering and one-parameter-per-packet rules encoded here are
transport-level and independent of the data source — see the Critical Rules in
CLAUDE.md before changing anything in this file.
"""
import logging
import os
import sys
import time

import grpc

from bridge.sample_value import SampleValue

# Add the generated gRPC stubs to the path
GENERATED_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_generated")
if GENERATED_DIR not in sys.path:
    sys.path.insert(0, os.path.normpath(GENERATED_DIR))

from ma.streaming.api.v1 import api_pb2, api_pb2_grpc
from ma.streaming.key_generator.v1 import key_generator_pb2, key_generator_pb2_grpc
from ma.streaming.open_data.v1 import open_data_pb2

from bridge.channel_registry import ATLAS_GROUP, ChannelDef

logger = logging.getLogger(__name__)

DEFAULT_STREAM_API = "localhost:13579"
KEY_GENERATOR_ADDRESS = "localhost:15379"
DATA_SOURCE = "Default"
STREAM = "Stream1"
MAIN_STREAM = ""  # empty string = main/default stream


def _pkt_type(obj) -> str:
    """Derive the packet type string from the protobuf class name."""
    n = obj.__class__.__name__
    return n[:-6] if n.endswith("Packet") else n


class AtlasWriter:
    def __init__(
        self,
        stream_api_address: str = DEFAULT_STREAM_API,
        data_source: str = DATA_SOURCE,
        stream: str = STREAM,
        key_generator_address: str = KEY_GENERATOR_ADDRESS,
    ) -> None:
        self._stream_api_address = stream_api_address
        self._data_source = data_source
        self._stream = stream
        self._key_generator_address = key_generator_address

        self._channel: grpc.Channel | None = None
        self._keygen_channel: grpc.Channel | None = None
        self._session_stub: api_pb2_grpc.SessionManagementServiceStub | None = None
        self._dfmt_stub: api_pb2_grpc.DataFormatManagerServiceStub | None = None
        self._writer_stub: api_pb2_grpc.PacketWriterServiceStub | None = None
        self._keygen_stub: key_generator_pb2_grpc.UniqueKeyGeneratorServiceStub | None = None

        self._session_key: str | None = None
        self._connected = False

        # Per-parameter data format IDs: { atlas_identifier: data_format_id }
        self._data_format_ids: dict[str, int] = {}
        # Ordered list of channel defs for this session
        self._channels: list[ChannelDef] = []
        # Incrementing packet ID (matching sample_writer pattern)
        self._next_packet_id: int = 0

    def connect(self) -> bool:
        try:
            self._channel = grpc.insecure_channel(self._stream_api_address)
            self._session_stub = api_pb2_grpc.SessionManagementServiceStub(self._channel)
            self._dfmt_stub = api_pb2_grpc.DataFormatManagerServiceStub(self._channel)
            self._writer_stub = api_pb2_grpc.PacketWriterServiceStub(self._channel)

            self._keygen_channel = grpc.insecure_channel(self._key_generator_address)
            self._keygen_stub = key_generator_pb2_grpc.UniqueKeyGeneratorServiceStub(self._keygen_channel)

            # Verify connectivity by listing current sessions
            self._session_stub.GetCurrentSessions(
                api_pb2.GetCurrentSessionsRequest(data_source=self._data_source)
            )
            logger.info("Connected to Stream API at %s", self._stream_api_address)
            self._connected = True
            return True
        except Exception as e:
            logger.error("Failed to connect to Stream API: %s", e)
            return False

    def disconnect(self) -> None:
        try:
            if self._keygen_channel:
                self._keygen_channel.close()
                self._keygen_channel = None
            if self._channel:
                self._channel.close()
                self._channel = None
        except Exception as e:
            logger.warning("Error during disconnect: %s", e)
        self._connected = False
        self._session_key = None
        self._data_format_ids = {}
        logger.info("Disconnected from Atlas")

    def is_connected(self) -> bool:
        return self._connected

    def _generate_key(self) -> str:
        """Get a unique key from the KeyGenerator service."""
        return self._keygen_stub.GenerateUniqueKey(
            key_generator_pb2.GenerateUniqueKeyRequest(type=key_generator_pb2.KEY_TYPE_STRING)
        ).string_key

    def _write_pkt(self, content_bytes: bytes, ptype: str, stream: str, essential: bool = False) -> None:
        """Write a packet through the Stream API's PacketWriterService."""
        pkt_id = self._next_packet_id
        self._next_packet_id += 1
        msg = open_data_pb2.Packet(
            type=ptype,
            content=content_bytes,
            session_key=self._session_key,
            is_essential=essential,
            id=pkt_id,
        )
        self._writer_stub.WriteDataPacket(
            api_pb2.WriteDataPacketRequest(
                detail=api_pb2.DataPacketDetails(
                    message=msg,
                    data_source=self._data_source,
                    stream=stream,
                    session_key=self._session_key,
                )
            )
        )

    def create_session(self, identifier: str, channels: list[ChannelDef]) -> str | None:
        if not self._connected:
            return None

        try:
            self._channels = channels

            # 1. Create session via gRPC SessionManagementService
            resp = self._session_stub.CreateSession(
                api_pb2.CreateSessionRequest(
                    data_source=self._data_source,
                    identifier=identifier,
                    type="Session",
                    version=1,
                )
            )
            self._session_key = resp.session_key
            logger.info("Session created: %s (key: %s)", identifier, self._session_key)

            # 2. NewSessionPacket — send to both streams
            new_sess = open_data_pb2.NewSessionPacket(data_source=self._data_source)
            pt = _pkt_type(new_sess)
            self._write_pkt(new_sess.SerializeToString(), pt, self._stream)
            self._write_pkt(new_sess.SerializeToString(), pt, MAIN_STREAM)
            time.sleep(1)

            # 3. ConfigurationPacket — single packet, all parameters
            config_id = self._generate_key()

            param_defs = []
            for ch in channels:
                param_defs.append(
                    open_data_pb2.ParameterDefinition(
                        identifier=ch.atlas_identifier,
                        name=ch.atlas_name,
                        application_name=ch.atlas_app,
                        description=ch.description,
                        units=ch.units,
                        data_type=open_data_pb2.DATA_TYPE_FLOAT64,
                        format_string=ch.format_string,
                        min_value=ch.min_value,
                        max_value=ch.max_value,
                        frequencies=[ch.frequency],
                    )
                )

            # Exactly one group — ATLAS silently drops a config packet carrying
            # several (see CLAUDE.md rule 3). Per-sensor grouping stays in the UI.
            group_defs = [
                open_data_pb2.GroupDefinition(
                    identifier=ATLAS_GROUP,
                    application_name=ATLAS_GROUP,
                    name=ATLAS_GROUP,
                    description="Hardware sensor readings from HWiNFO",
                )
            ]

            config_pkt = open_data_pb2.ConfigurationPacket(
                config_id=config_id,
                parameter_definitions=param_defs,
                group_definitions=group_defs,
            )
            config_bytes = config_pkt.SerializeToString()
            config_type = _pkt_type(config_pkt)
            self._write_pkt(config_bytes, config_type, MAIN_STREAM, essential=True)
            self._write_pkt(config_bytes, config_type, self._stream, essential=True)
            logger.info(
                "Configuration published (%d params, config_id=%s)",
                len(param_defs), config_id,
            )

            # 4. Register per-parameter data format IDs via DataFormatManagerService
            self._data_format_ids = {}
            for ch in channels:
                dfmt_resp = self._dfmt_stub.GetParameterDataFormatId(
                    api_pb2.GetParameterDataFormatIdRequest(
                        data_source=self._data_source,
                        parameters=[ch.atlas_identifier],
                    )
                )
                self._data_format_ids[ch.atlas_identifier] = dfmt_resp.data_format_identifier
            logger.info("Data format IDs registered: %d", len(self._data_format_ids))

            return self._session_key

        except Exception as e:
            logger.error("Failed to create Atlas session: %s", e)
            return None

    def send_periodic_data(
        self,
        data: dict[str, list[SampleValue]],
        timestamp_ns: int,
        interval_ns: int,
    ) -> bool:
        if not self._connected or not self._session_key or not self._data_format_ids:
            return False

        try:
            # One PeriodicDataPacket per parameter (see CLAUDE.md rule 2)
            for ch in self._channels:
                values = data.get(ch.metric_key, [])
                if not values:
                    continue

                samples = [
                    open_data_pb2.DoubleSample(
                        value=v.value, status=open_data_pb2.DATA_STATUS_VALID
                    )
                    for v in values
                ]
                col = open_data_pb2.SampleColumn(
                    double_samples=open_data_pb2.DoubleSampleList(samples=samples)
                )

                dfmt_id = self._data_format_ids.get(ch.atlas_identifier)
                if dfmt_id is None:
                    continue

                data_pkt = open_data_pb2.PeriodicDataPacket(
                    data_format=open_data_pb2.SampleDataFormat(
                        data_format_identifier=dfmt_id
                    ),
                    start_time=timestamp_ns,
                    interval=interval_ns,
                    columns=[col],
                )
                dt = _pkt_type(data_pkt)
                self._write_pkt(data_pkt.SerializeToString(), dt, self._stream)

            return True
        except Exception as e:
            logger.error("Failed to send periodic data: %s", e)
            return False

    def send_marker(
        self,
        timestamp_ns: int,
        label: str,
        marker_type: str,
        description: str,
        value: int,
    ) -> bool:
        if not self._connected or not self._session_key:
            return False

        try:
            marker = open_data_pb2.MarkerPacket(
                timestamp=timestamp_ns,
                label=label,
                type=marker_type,
                description=description,
                source="0",
                value=value,
            )
            marker_bytes = marker.SerializeToString()
            marker_type_str = _pkt_type(marker)
            self._write_pkt(marker_bytes, marker_type_str, MAIN_STREAM, essential=True)
            self._write_pkt(marker_bytes, marker_type_str, self._stream, essential=True)
            logger.info(
                "Marker sent: label=%s type=%s value=%d ts=%d",
                label, marker_type, value, timestamp_ns,
            )
            return True
        except Exception as e:
            logger.error("Failed to send marker: %s", e)
            return False

    def end_session(self) -> bool:
        if not self._connected or not self._session_key:
            return False

        try:
            # Send EndOfSession packets to both streams
            end_pkt = open_data_pb2.EndOfSessionPacket(data_source=self._data_source)
            et = _pkt_type(end_pkt)
            self._write_pkt(end_pkt.SerializeToString(), et, self._stream)
            self._write_pkt(end_pkt.SerializeToString(), et, MAIN_STREAM)

            # End the session via gRPC SessionManagementService
            self._session_stub.EndSession(
                api_pb2.EndSessionRequest(
                    data_source=self._data_source,
                    session_key=self._session_key,
                )
            )

            logger.info("Atlas session ended: %s", self._session_key)
            self._session_key = None
            self._data_format_ids = {}
            return True
        except Exception as e:
            logger.error("Failed to end session: %s", e)
            return False
