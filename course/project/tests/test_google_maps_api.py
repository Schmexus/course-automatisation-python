import requests
from requests import Response

from project.utils.api import Google_maps_api


"""Создание изменения и удаления новой локации"""
class Test_create_place():

    def test_create_new_place(self):
        print('Method POST')
        result_post: Response = Google_maps_api.create_new_place()
        # print(result_post)
        assert result_post.status_code == 200
        assert result_post.json()["status"] == "OK"

    def test_hyiusa(self):
        url = "https://reqres.in/api/login"
        json_post = json_post = [
    {
        "email": "peter@klaven"
    }
]

        response = requests.post(url, json=json_post, headers={'x-api-key': 'reqres-free-v1'})
        data = response.json()

        # Заполняем пропуски:
        print(response.status_code)  # Статус-код (например: 201)
        print(data)  # Тип данных поля id (будет: <class 'int'> или <class 'str'>)
