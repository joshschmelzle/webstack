import dataclasses
from typing import Optional

from pydantic import BaseModel, Field


@dataclasses.dataclass
class Ping:
    jitter: float = Field(example=3.971)
    latency: float = Field(example=11.151)


@dataclasses.dataclass
class Download:
    bandwidth: int = Field(example=19780836)
    dl_bytes: int = Field(example=226938080)
    elapsed: int = Field(example=11707)


@dataclasses.dataclass
class Upload:
    bandwidth: int = Field(example=1364478)
    ul_bytes: int = Field(example=5226800)
    elapsed: int = Field(example=3813)


@dataclasses.dataclass
class Interface:
    internal_ip: str = Field(example="192.168.1.21")
    name: str = Field(example="eth0")
    macAddr: str = Field(example="02:01:78:00:00:00")
    isVpn: bool = Field(example=False)
    externalIp: str = Field(example="46.156.79.21")


@dataclasses.dataclass
class Server:
    server_id: int = Field(example=20398)
    name: str = Field(example="Rando LLC")
    location: str = Field(example="NYC")
    country: str = Field(example="United States")
    host: str = Field(example="speedtest.rando-llc.com")
    port: int = Field(example=8080)
    ip: str = Field(example="243.238.215.215")


@dataclasses.dataclass
class Result:
    result_id: str = Field(example="949308a2-e34e-2fe0-81f7-8d12cc02daab")
    url: str = Field(
        example="https://www.speedtest.net/result/c/949308a2-e34e-2fe0-81f7-8d12cc02daab"
    )


class OoklaSpeedtest(BaseModel):
    resp_type: str = Field(example="result")
    timestamp: str = Field(example="2021-01-04T04:01:06Z")
    ping: Optional[Ping]
    download: Optional[Download]
    upload: Optional[Upload]
    isp: str = Field(exmaple="Awesome ISP")
    interface: Optional[Interface]
    server: Optional[Server]
    result: Optional[Result]

    class Config:
        arbitrary_types_allowed = True
