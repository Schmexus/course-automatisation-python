from base_class import Alphabet, Cyrillic   # импортирование классов

russian = Alphabet("Русский", "RU", "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
russian.description()
russian.count_letter()


serbian = Cyrillic("Сербский", "SR", "абвгдђежзијклмнњопрстћуфхцчџшыэ")
serbian.description()
serbian.count_letter()