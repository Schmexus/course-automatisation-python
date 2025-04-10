import requests
import json
url = 'https://api.chucknorris.io/jokes/random'
result = requests.get(url)
print(json.dumps(result.json(), indent = 4, sort_keys=False)) ## Вывод тела ответа
print(json.dumps(result.json().get('value'), indent = 4, sort_keys=False)) ## Выводконкретного поля в теле