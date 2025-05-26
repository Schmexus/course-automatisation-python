"""Методы для общих проверок запросов"""
import json


class Check():


    @staticmethod
    def status_code(request, status_code):
        """Метод для проверки статус кода"""
        assert status_code == request.status_code, f'ОШИБКА, Статус-код = {request.status_code()}, ожидаемый {status_code}'
        print(f"Проверка статус кода успешна! {status_code} = {request.status_code}")



    @staticmethod
    def fields(request, expected_fields):
        """Метод для проверки наличия обязательных полей"""
        fields = set(json.loads(request.text).keys())
        expected_fields = set(expected_fields)
        missing_fields = expected_fields - fields
        assert not missing_fields, f'Есть недостающие поля в ответе: {missing_fields}'


    @staticmethod
    def values_in_field(request, field_name, expected_value):
        """Метод для проверки значений обязательных полей"""
        value = request.json().get(field_name)
        assert value == expected_value
        print(f'{field_name} - корректный')

    @staticmethod
    def word_in_field(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса при помощи поиска по определенному слову"""
        value = result.json().get(field_name)
        assert search_word in value
        print(f" {search_word} присутствует")