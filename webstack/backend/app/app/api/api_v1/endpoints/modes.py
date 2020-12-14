from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_current_mode():
    return "TBD"


@router.get("/wifi_console")
def switch_to_wifi_console_mode():
    return "TBD"


@router.get("/hotspot")
def switch_to_hotspot_mode():
    return "TBD"


@router.get("/wiperf")
def switch_to_wiperf_mode():
    return "TBD"


@router.get("/server")
def switch_to_server_mode():
    return "TBD"


@router.get("/beacon_collector/start")
def start_beacon_collector():
    """
    The idea:

    1. Enable the audit tool via the FPMS and walk around the area being audited.
    2. WLAN Pi collects beacons
    3. End audit collection via FPMS
    4. WLAN Pi dumps a local file of unique beacons in a PCAP
    5. File can be retrieved when return to base, and inspected in WFE or similar tool to report on networks detected in audit area.
    """
    return "START COLLECTOR"


@router.get("/beacon_collector/stop")
def stop_beacon_collector():
    """
    Stops the beacon collector and stores the data locally.
    """


@router.get("/beacon_collector/")
def list_beacon_collector_data():
    pass


@router.get("/beacon_collector/:object")
def get_beacon_collector_data():
    pass
