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
        # if result_post.json().get('status') == 'OK': print(f'Локация создана {self.check_location(result_post.json().get("place_id"))}')
        assert 200 == result_post.status_code and result_post.json().get('status') == 'OK', f'Статус код = {result_post.status_code}, локация не создана'
        return result_post.json().get('place_id')

    def check_location(self, place_id):
        """Проверка локации"""
        get_resource = '/maps/api/place/get/json'
        get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
        result_get = requests.get(get_url)
        # print("Локация: " + str(result_get.json().get('name')))
        assert 200 == result_get.status_code, f'Статус код = {result_get.status_code}, локация не найдена'
        return str(result_get.json().get('name'))

    def change_location(self, place_id):
        """Изменение локации"""
        put_resources = "/maps/api/place/update/json"
        put_url = self.base_url + put_resources + self.key
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        assert 200 == result_put.status_code, f'Статус код = {result_put.status_code}, локация не изменена'
        check_put = result_put.json()
        check_put_info = check_put.get('msg')
        print('MESSAGE:' + check_put_info)
        assert check_put_info == "Address successfully updated"

    def delete_location(self, place_id):
        """Удаление локации"""
        name_company = self.check_location(place_id)
        delete_resources = "/maps/api/place/delete/json"
        delete_url = self.base_url + delete_resources + self.key
        json_for_delete_location = {"place_id": place_id}
        result_delete = requests.delete(delete_url, json=json_for_delete_location)
        assert 200 == result_delete.status_code and result_delete.json().get("status") == 'OK', f'Статус код = {result_delete.status_code}, локация не удалена'
        print(f'Локация: {name_company} удалена')


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
        for i, place_id in enumerate(file.readlines(), 1):
            if i%2==0:
                maps.delete_location(place_id.strip())
    except: print("Возникла ошибка при удалении локаций")
with open('place_id.txt','r') as file, open('place_id_new.txt', 'w') as file_new:
    for line in file:
        place_id = line.strip()
        try:
                name = maps.check_location(place_id) # для красивого вывода, что записали компанию и проверке ее на существование
                file_new.write(place_id+'\n')
                print(f'компания {name} записана')
        except: continue