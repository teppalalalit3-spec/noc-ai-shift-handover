import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

USERNAME = os.getenv("NAGIOS_USERNAME")
PASSWORD = os.getenv("NAGIOS_PASSWORD")

BASE_URL = os.getenv(
    "NAGIOS_URL",
    "http://host.docker.internal/nagios/cgi-bin/statusjson.cgi"
)

HOST_URL = (
    f"{BASE_URL}?query=hostlist&formatoptions=enumerate"
)

SERVICE_URL = (
    f"{BASE_URL}?query=servicelist&formatoptions=enumerate"
)


def get_live_alerts():

    alerts = []

    try:

        host_response = requests.get(
            HOST_URL,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        host_response.raise_for_status()

        host_data = host_response.json()

        hosts = host_data["data"]["hostlist"]

        for host, status in hosts.items():

            if status.lower() != "up":

                alerts.append({
                    "host": host,
                    "service": "HOST",
                    "status": status.upper(),
                    "message": f"Host {host} is {status.upper()}"
                })

        service_response = requests.get(
            SERVICE_URL,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            timeout=10
        )

        service_response.raise_for_status()

        service_data = service_response.json()

        services = service_data["data"]["servicelist"]

        for host, service_list in services.items():

            for service_name, status in service_list.items():

                status = status.upper()

                if status != "OK":

                    alerts.append({
                        "host": host,
                        "service": service_name,
                        "status": status,
                        "message": f"{service_name} is {status}"
                    })

    except Exception as e:

        print(f"Nagios Error: {e}")

        return []

    return alerts
