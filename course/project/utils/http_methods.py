import requests

"""Список методов"""

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        return requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)

    @staticmethod
    def post(url, body):
        return requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie, verify=False)

    @staticmethod
    def put(url, body):
        return requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)

    @staticmethod
    def delete(url, body):
        return requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie, verify=False)
