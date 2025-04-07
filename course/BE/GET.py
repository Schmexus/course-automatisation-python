import requests
import json
url = 'https://api.chucknorris.io/jokes/random'
result = requests.get(url)
print(json.dumps(result.json().get('value'), indent = 4, sort_keys=False))
