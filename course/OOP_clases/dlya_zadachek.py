import json

import requests

url = "https://catfact.ninja/facts?max_length=100&limit=5"

headers = {
    "x-api-key": "reqres-free-v1"
}

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]

response = requests.get(url,headers=headers, verify=False)
data = response.text

print(f"{list(json.loads(data))}")