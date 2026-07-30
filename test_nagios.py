from nagios_client import get_service_status
import json

data = get_service_status()

print(json.dumps(data, indent=4))
