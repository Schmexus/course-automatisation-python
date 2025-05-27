import requests
"""Не стал выносить все в отдельные методы (получение данных по фильму, по персонажу), 
т к единоразовое использование, если было бы переиспользование логики, то вынес бы в метод"""

def req_get(url):
    return requests.get(url, headers={'Content-Type': 'application/json'},
                        verify=False)  # игнорируем серртификат, чтоб можно было отправлять запросы на этот сервис


"""Не стал выделать URL отдельной переменной, т к использование единично"""
movies = req_get('https://swapi.dev/api/people/4/').json().get('films')
characters = set()
for movie in movies:
    characters_in_movie = req_get(movie).json().get('characters')  # Ищем всех персонажей в фильме
    for character in characters_in_movie:
        characters.add(req_get(character).json().get('name'))  # Выносим имя персонажа и добавляем его в множество
with open('characters.txt', 'w',
          encoding="utf-8") as file:  # добавляем кодировку utf-8, чтобы все персонажи записались без исключений
    """Исключаем Дарта Вейдера, т к очевидно, что он есть в фильмах с собой,
     делаем это после сбора множества, на случай, если он вдруг перестанет быть people/4"""
    characters.discard("Darth Vader")
    file.write("\n".join(characters))
