import dataclasses
from typing import Optional

from pydantic import BaseModel


@dataclasses.dataclass
class Ping:
    jitter: float
    latency: float


@dataclasses.dataclass
class Download:
    bandwidth: int
    dl_bytes: int
    elapsed: int


@dataclasses.dataclass
class Upload:
    bandwidth: int
    ul_bytes: int
    elapsed: int


@dataclasses.dataclass
class Interface:
    internal_ip: str
    name: str
    macAddr: str
    isVpn: bool
    externalIp: str


@dataclasses.dataclass
class Server:
    server_id: int
    name: str
    location: str
    country: str
    host: str
    port: int
    ip: str


@dataclasses.dataclass
class Result:
    result_id: str
    url: str


class OoklaSpeedtest(BaseModel):
    resp_type: str
    timestamp: str
    ping: Optional[Ping]
    download: Optional[Download]
    upload: Optional[Upload]
    packetLoss: int
    interface: Optional[Interface]
    server: Optional[Server]
    result: Optional[Result]
