import requests

url = "https://reqres.in/api/users/3"

headers = {
    "x-api-key": "reqres-free-v1"
}

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]

response = requests.put(url,headers=headers, json=json_put, verify=False)
data = response.json()

print(f"[{data}]")