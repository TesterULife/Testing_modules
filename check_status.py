import requests
import json


from src.configurations import SERVICE_URL

resp = requests.get(SERVICE_URL)
print(json.dumps(resp.json(), indent=4))