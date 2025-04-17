import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Norris_jokes():
    """Класс по работе с АПИ - шутки про Чака Норриса"""

    def __init__(self):
        self.base_url = 'https://api.chucknorris.io/jokes/'

    def get_categories(self, printer):  # Метод для получения списка категорий
        categories = requests.get(self.base_url + 'categories', verify=False)
        assert categories.status_code == 200, "Запрос не выполнен, статус код не равен 200."
        # print('Категории получены.')
        if printer:
            print('Список категорий:', ', '.join(categories.json()))
        return categories.json()

    def get_joke_by_category(self, category):  # Метод для получения шутки по определенной категории
        joke = requests.get(f'{self.base_url}random?category={category}', verify=False)
        assert joke.status_code == 200, "Запрос не выполнен, статус код не равен 200."
        return joke.json().get('value')


categories = Norris_jokes().get_categories(True)
category = input('Введите категорию для получения по ней шутки: ')
if category in categories: # Проверка на то, что введенная категория есть в списке
    print(Norris_jokes().get_joke_by_category(category))
else:
    print('Данной категории не существует')
