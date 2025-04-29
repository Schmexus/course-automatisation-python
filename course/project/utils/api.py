import requests
from faker import Faker

from project.utils.http_methods import Http_methods

"""Методы для тестирования гугл карт апи"""
base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'
class Google_maps_api():

        """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():
        json_create_new_place = {
            "location":{
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name" : Faker().company(), #для того, чтобы в будущем не сооздавать одну и ту же компанию, названия разные
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        resource = '/maps/api/place/add/json'
        post_url = base_url+resource+key
        return Http_methods.post(post_url, json_create_new_place)

    """Метод для получения данных о локации"""
    @staticmethod
    def get_place(place_id):
        resource = '/maps/api/get/json'
        url = base_url +resource + key + "&place_id=" + place_id
        return Http_methods.get(url)