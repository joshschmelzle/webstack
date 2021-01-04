import json

from fastapi import APIRouter

# from .helpers import run

router = APIRouter()


# @router.get("/interfaces")
# def get_interfaces():
#    return "TBD"


# @router.get("/wlan_interfaces")
# def get_wlan_interfaces():
#    return "TBD"


# @router.get("/interface/ip_config")
# def get_interface_ip_config(interface: str):
#    return "TBD"


# @router.get("/interface/vlan")
# def get_interface_vlan(interface: str):
#    return "TBD"


@router.get("/neighbors")
async def show_neighbors():
    """
    Run `lldpcli show neighbors -f json` and return results

    Test psuedo code:

    ```
    import urllib.request,json,pprint
    with urllib.request.urlopen('http://127.0.0.1:8000/api/v1/network/neighbors') as resp:
        data = json.loads(resp.read().decode())
    pprint.pprint(data)
    ```
    """

    results = await run("sudo lldpcli show neighbors -f json")

    if "[stderr]" not in results:
        return results
    else:
        results = "Problem running lldpcli show neighbors -f json"


import urllib.request


@router.get("/publicip")
async def retrieve_public_ip_information():
    """
    Uses `ifconfig.co/json` to retrieve Public IP information.
    """
    url = "https://ifconfig.co/json"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read())

    return json.dumps(data)
