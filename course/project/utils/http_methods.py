import allure
import requests
from project.utils.logger import Logger

"""Список методов"""

class Http_methods:
    headers = {'Content-Type': 'application/json'}
    cookie = ''

    @staticmethod
    def get(url):
        with allure.step('GET-request'):
            Logger.add_request(url, method='GET')
            result =  requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie, verify=False)
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step('POST-request'):
            Logger.add_request(url, method='POST')
            result = requests.post(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie, verify=False)
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step('PUT-request'):
            Logger.add_request(url,method='PUT')
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie, verify=False)
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url, body):
        with allure.step('DELETE-request'):
            Logger.add_request(url,method='DELETE')
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie, verify=False)
            Logger.add_response(result)
            return result
