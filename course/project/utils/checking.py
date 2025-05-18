"""Методы для общих проверок запросов"""
import json


class Check():

    """Метод для проверки статус кода"""
    @staticmethod
    def status_code(request, status_code):
        assert status_code == request.status_code, f'ОШИБКА, Статус-код = {request.status_code()}, ожидаемый {status_code}'
        print(f"Проверка статус кода успешна! {status_code} = {request.status_code}")


    """Метод для проверки наличия обязательных полей"""
    @staticmethod
    def fields(request, expected_fields):
        fields = set(json.loads(request.text).keys())
        expected_fields = set(expected_fields)
        missing_fields = expected_fields - fields
        assert not missing_fields, f'Есть недостающие поля в ответе: {missing_fields}'

    """Метод для проверки значений обязательных полей"""
    @staticmethod
    def values_in_fields(request, field_name, expected_value):
        value= request.json().get(field_name)
        assert value == expected_value
        print(f'{field_name} - корректный')