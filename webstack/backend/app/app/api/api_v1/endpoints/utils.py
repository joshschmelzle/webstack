import json
import platform
from socket import gethostname

import psutil
from dbus import Interface, SystemBus
from dbus.exceptions import DBusException
from fastapi import APIRouter

router = APIRouter()


def check_service_status(service):
    """ queries systemd through dbus to see if the service is running """
    service_running = False
    bus = SystemBus()
    systemd = bus.get_object("org.freedesktop.systemd1", "/org/freedesktop/systemd1")
    manager = Interface(systemd, dbus_interface="org.freedesktop.systemd1.Manager")
    try:
        service_unit = (
            service
            if service.endswith(".service")
            else manager.GetUnit(f"{service}.service")
        )
        service_proxy = bus.get_object("org.freedesktop.systemd1", str(service_unit))
        service_props = Interface(
            service_proxy, dbus_interface="org.freedesktop.DBus.Properties"
        )
        service_load_state = service_props.Get(
            "org.freedesktop.systemd1.Unit", "LoadState"
        )
        service_active_state = service_props.Get(
            "org.freedesktop.systemd1.Unit", "ActiveState"
        )
        if service_load_state == "loaded" and service_active_state == "active":
            service_running = True
    except DBusException:
        pass
    return service_running


services = [
    "profiler",
    "fpms",
    "iperf3",
    "ufw",
    "tftpd-hpa",
    "hostapd",
    "wpa_supplicant",
]


@router.get("/service")
async def get_systemd_service_status(name: str):
    """
    Queries systemd via dbus to get status of a given service.
    """
    status = ""
    name = name.strip().lower()
    if name in services:
        status = check_service_status(name)
        return {"name": name, "active": status}
    return {"error": f"{name} access restricted or does not exist"}


# @router.get("/reachability")
# def get_reachability():
#    return "TBD"


# @router.get("/mist_cloud")
# def test_mist_cloud_connectivity():
#    return "TBD"

# @router.get("/usb_devices")
# def get_usb_devices():
#    return "TBD"


# @router.get("/ufw_ports")
# def get_ufw_ports():
#    return "TBD"

# @router.get("/wpa_password")
# def get_wpa_password():
#    return "TBD"

# @router.put("/wpa_password")
# def update_wpa_password():
#    return "TBD"


@router.get("/hostname")
async def read_wlanpi_hostname():
    return gethostname()


# @router.put("/hostname")
# def set_wlanpi_hostname(name: str):
#    """
#    Need to change /etc/hostname and /etc/hosts
#    socket.sethostname(name) does not seem to work
#    """
#    return "TODO"

# @router.put("/dns_test")
# def dns_performance_test(name: str):
#    """
#    Example: https://github.com/cleanbrowsing/dnsperftest
#    """
#    return "TODO"


def get_wlanpi_version():
    wlanpi_version = ""
    try:
        with open("/etc/wlanpi-release") as _file:
            lines = _file.read().splitlines()
            for line in lines:
                if "VERSION" in line:
                    wlanpi_version = "{0}".format(
                        line.split("=")[1].replace('"', "").strip()
                    )
    except OSError:
        pass
    return wlanpi_version


@router.get("/system_info")
async def get_system_summary():
    uname = platform.uname()
    summary = {}
    summary["system"] = uname.system
    summary["build"] = get_wlanpi_version()
    summary["node_name"] = uname.node
    summary["release"] = uname.release
    summary["version"] = uname.version
    summary["machine"] = uname.machine
    summary["processor"] = uname.processor
    return json.dumps(summary)


@router.get("/psutil_info")
async def get_psutil_info():
    stats = {}
    stats["cpu_count"] = psutil.cpu_count()
    stats["cpu_freq"] = psutil.cpu_freq()
    stats["cpu_percent"] = psutil.cpu_percent()
    stats["cpu_stats"] = psutil.cpu_stats()
    stats["getloadavg"] = psutil.getloadavg()
    stats["sensors_battery"] = psutil.sensors_battery()
    stats["sensors_fans"] = psutil.sensors_fans()
    stats["sensors_temperatures"] = psutil.sensors_temperatures()
    stats["disk_usage"] = psutil.disk_usage("/")
    stats["boot_time"] = psutil.boot_time()
    # stats['virtual_memory'] = psutil.virtual_memory()
    # stats['swap_memory'] = psutil.swap_memory()
    # stats['net_if_addrs'] = psutil.net_if_addrs()
    return json.dumps(stats)
