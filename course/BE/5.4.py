import requests


class Norris_jokes():
    """Класс по работе с АПИ - шутки про Чака Норриса"""

    def __init__(self):
        self.base_url = 'https://api.chucknorris.io/jokes/'

    def get_categories(self):  # Метод для получения списка категорий
        categories = requests.get(self.base_url + 'categories')
        assert categories.status_code == 200, "Запрос не выполнен, статус код не равен 200."
        print('Категории получены.')
        return categories.json()

    def get_jokes_by_category(self, category):  # Метод для получения шутки по определенной категории
        joke = requests.get(f'{self.base_url}random?category={category}')
        assert joke.status_code == 200, "Запрос не выполнен, статус код не равен 200."
        # print(joke.json())
        # print('Шутка получена.')
        return joke.json().get('value')


categories = Norris_jokes().get_categories()
try:
    for category in categories: # перебираем все категории и получаем по ним шутки
        print(Norris_jokes().get_jokes_by_category(category))
except:
    print('Какую-то из шуток не удалось получить')
