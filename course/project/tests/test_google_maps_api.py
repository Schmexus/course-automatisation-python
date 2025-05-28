from project.utils.api import Google_maps_api
from project.utils.http_methods import Http_methods
import allure
from project.utils.checking import Check

"""Создание изменения и удаления новой локации"""

@allure.epic('Тест создает новую локацию, изменяет, удаляет')
class Test_create_place():

    @allure.description('Тест на основной флоу локации: создания, обновление, получение данных, удаление')
    def test_new_place(self):
        print('Method POST')
        result_post = Google_maps_api.create_new_place()
        assert result_post.status_code == 200
        assert result_post.json()["status"] == "OK"
        place_id = result_post.json().get('place_id')

        print('Method GET')
        result_get = Google_maps_api.get_place(place_id)
        print(result_get.text)

        print('Method PUT')
        json = { 'address': '100 Lenina street< RU'}
        result_put = Google_maps_api.change_place(json, place_id)
        print(result_put.text)

        print('Method Delete')
        result_delete = Google_maps_api.delete_place(place_id)
        Check.fields(result_delete,['status           '])
        Check.values_in_fields(result_delete, 'status', 'OK')





