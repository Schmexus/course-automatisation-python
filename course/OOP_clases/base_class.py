class Alphabet:
    """Класс по созданию и работе с алфавитом"""
    def __init__(self, title, abbreviation, list_letters):
        """Атрибуты класса"""
        self.title = title         
        self.abbreviation = abbreviation
        self.list_letters = list_letters
        print("Новый алфавит создан")



    def description(self):
        """Получение описания алфавита"""
        description = (f"Название данного алфавита - {self.title}, его аббревиатура - {self.abbreviation},"
                       f" список букв - {self.list_letters}")
        print(description)



    def count_letter(self):
        """Получение количества букв в алфавите"""
        count = (len(self.list_letters))
        print(f"Количество букв в алфавите равно: {count}")




class Cyrillic(Alphabet):
    """Языки группы Кириллица"""

    def __init__(self, title, abbreviation, list_letters):
        super().__init__(title, abbreviation, list_letters)
        """Указываем какие атрибуты имеет Класс-наследник"""
        self.language_group = "Cyrl"

    def description(self):
        """Получение описания алфавита"""
        description = (f"Название данного алфавита - {self.title}, группа языков - {self.language_group},"
                          f"его аббревиатура - {self.abbreviation}, список букв - {self.list_letters}")
        print(description)


    def get_language_group(self):
        """Метод возвращающий абревиатуру языковой группы"""
        print(f"Абревиатура языковой группы {self.language_group}")
        return self.language_group