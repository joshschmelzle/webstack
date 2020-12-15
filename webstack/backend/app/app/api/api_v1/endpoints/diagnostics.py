import json
import os
from shutil import which

from fastapi import APIRouter, HTTPException

from .helpers import run

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

"""


def is_tool(name: str):
    """
    Check whether `name` is on PATH and marked as executable.
    """
    return which(name) is not None


@router.get("/")
async def diagnostics(interface: str):
    """
    Return diagnostic tests for WLAN sensors
    """
    if not os.path.isdir(f"/sys/class/net/{interface}/"):
        raise HTTPException(status_code=404, detail=f"{interface} not found")

    diag = {}

    regdomain = await run("iw reg get")

    diag["regdomain"] = [line for line in regdomain.split("\n") if "country" in line]

    diag["driver"] = (
        await run(f"readlink -f /sys/class/net/{interface}/device/driver")
    ).strip()

    diag["mac"] = (await run(f"cat /sys/class/net/{interface}/address")).strip()

    diag["tcpdump"] = is_tool("tcpdump")

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
    diag["operstate"] = operstate.strip()

    _type = await run(f"cat /sys/class/net/{interface}/type")

    _type = int(_type)
    if _type == 1:
        diag["mode"] = "managed"
    elif _type == 801:
        diag["mode"] = "monitor"
    elif _type == 802:
        diag["mode"] = "monitor"
    elif (
        _type == 803
    ):  # https://elixir.bootlin.com/linux/latest/source/include/uapi/linux/if_arp.h#L90
        diag["mode"] = "monitor"
    else:
        diag["mode"] = "unknown"

    return json.dumps(diag)
