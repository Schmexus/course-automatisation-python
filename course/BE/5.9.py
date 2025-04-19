import requests
from faker import Faker # генератор для наименования компании, мб в будущем все генерить можно будет

class Google_maps:
    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'

    def test_create_new_location(self):
        """Создание новой локации"""
        post_resource = '/maps/api/place/add/json'
        post_url = self.base_url + post_resource + self.key
        json_for_create_new_location = {
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
        result_post = requests.post(post_url, json= json_for_create_new_location)
        # if result_post.json().get('status') == 'OK': print('Локация создана')
        assert 200 == result_post.status_code and result_post.json().get('status') == 'OK', f'Статус код = {result_post.status_code}, локация не создана'
        return result_post.json().get('place_id')

    def check_location(self, place_id):
        """Проверка существования локации"""
        get_resource = '/maps/api/place/get/json'
        get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
        result_get = requests.get(get_url)
        print("Локация: " + str(result_get.json().get('name')))
        assert 200 == result_get.status_code, f'Статус код = {result_get.status_code}, локация не найдена'

maps = Google_maps()
with open('place_id.txt','w') as file:
    try:
        number = 5
        for i in range(number):
            file.write(maps.test_create_new_location()+'\n')
        print(f"Создано {number} локаций")
    except: print('Ошибки при создании локаций')
with open('place_id.txt','r') as file:
    try:
        for i, v in enumerate(file.readlines(), 1):
            maps.check_location(v.strip()) # strip для того, чтобы удалить в place_id \n
    except: print("Возникла ошибка при поиске локаций")