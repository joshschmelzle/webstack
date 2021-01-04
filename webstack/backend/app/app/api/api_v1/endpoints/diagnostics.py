import fcntl
import json
import os
import socket
import struct
from shutil import which
from typing import List, Optional

from fastapi import APIRouter, HTTPException

# from .helpers import run

router = APIRouter()

"""
First ask for diagnostics is around capture/scan sensor function of the WLAN Pi.

For example, assuming the user can reach the WLAN Pi-

- Is the adapter plugged in? 
- What USB port?
- Does the adapter support monitor mode? 
- Is the wifiexplorer-sensor running? 
- Is tcpdump installed?
- Does it need sudo to run?

For diagnostics endpoints include a HTTP status code, if problem, return "false", and "error" with message.

2xx: good
4xx: bad - client’s fault (like providing a name for an non-existing interface)
5xx: bad - server’s fault (like not having tcpdump properly installed)

Example:
{“success”: true, “response”: [{“name”: “wlan0"}, {“name”: “wlan1"}]}, { “success”: false, “error”: { “code”: 1001, “message”: “interface not found”}
"""


def is_tool(name: str):
    """
    Check whether `name` is on PATH and marked as executable.
    """
    return which(name) is not None


async def get_wifi_interfaces() -> List:
    interfaces = []
    path = "/sys/class/net"
    for net, ifaces, files in os.walk(path):
        for iface in ifaces:
            for dirpath, dirnames, filenames in os.walk(os.path.join(path, iface)):
                if "phy80211" in dirnames:
                    interfaces.append(iface)
    return interfaces


async def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        return socket.inet_ntoa(
            fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack("256s", bytes(ifname[:15], "utf-8")),
            )[20:24]
        )
    except OSError:
        return None


async def test_wifi_interface(interface: str) -> dict:
    test = {}

    test["mac"] = (await run(f"cat /sys/class/net/{interface}/address")).strip()

    test["local_ip"] = await get_ip_address(interface)

    test["driver"] = (
        (await run(f"readlink -f /sys/class/net/{interface}/device/driver"))
        .strip()
        .rsplit("/", 1)[1]
    )

    """
https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net

What:		/sys/class/net/<iface>/operstate
Date:		March 2006
KernelVersion:	2.6.17
Contact:	netdev@vger.kernel.org
Description:
		Indicates the interface RFC2863 operational state as a string.

		Possible values are:

		"unknown", "notpresent", "down", "lowerlayerdown", "testing",
		"dormant", "up".
    """
    operstate = await run(f"cat /sys/class/net/{interface}/operstate")
    test["operstate"] = operstate.strip()

    _type = await run(f"cat /sys/class/net/{interface}/type")

    _type = int(_type)
    if _type == 1:
        test["mode"] = "managed"
    elif _type == 801:
        test["mode"] = "monitor"
    elif _type == 802:
        test["mode"] = "monitor"
    elif (
        _type == 803
    ):  # https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/if_arp.h#L90
        test["mode"] = "monitor"
    else:
        test["mode"] = "unknown"

    return test


@router.get("/interfaces")
async def diagnostics(interface: Optional[str] = None):
    interfaces = await get_wifi_interfaces()
    if interface:
        if interface not in interfaces:
            raise HTTPException(status_code=404, detail=f"{interface} not found")
        return json.dumps(await test_wifi_interface(interface))
    else:
        combined = []
        for interface in interfaces:
            combined.append(await test_wifi_interface(interface))
        return json.dumps(combined)


@router.get("/")
async def diagnostics():
    """
    Return diagnostic tests for probe
    """
    diag = {}

    regdomain = await run("iw reg get")

    diag["regdomain"] = [line for line in regdomain.split("\n") if "country" in line]
    diag["tcpdump"] = is_tool("tcpdump")
    diag["iw"] = is_tool("iw")
    diag["ip"] = is_tool("ip")
    diag["ifconfig"] = is_tool("ifconfig")
    diag["airmon-ng"] = is_tool("airmon-ng")

    return json.dumps(diag)
