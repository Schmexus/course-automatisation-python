numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))
print(str(numbers_1&numbers_2-numbers_3))

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers_3 = set(map(int, input().split()))
if numbers_1&numbers_2&numbers_3: print('Good')
else: print('Bad')

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
for i in sorted(numbers_1 | numbers_2):
    print(i)

numbers_1 = set(map(int, input().split()))
numbers_2 = set(map(int, input().split()))
numbers= sorted(numbers_1&numbers_2)
for i in numbers:
    print(i)

dict1 = {'a': 1, 'b': 2, 'c': 3}
for key, val in list(dict1.items()): #юзаю лист потому что словарь будет изменяться в процессе
    dict1[val] = key
    del dict1[key]
for k, v in dict1.items():
    print(str(k) + " - " + str(v))

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4} # можно было просто решить как dict1.update(dict2)
for key_1, val_1 in list(dict1.items()):
    for key_2, val_2 in dict2.items():
        if key_2 == key_1:
            continue
        else:
            dict1[key_2] = val_2
for k, v in dict1.items():
    print(str(k) + " - " + str(v))

new_dict = {'Имя': 'Светлана', 'Пароль': 'qwer1234', 'Код': 1984}
new_dict['Имя'] = 'С#######'
new_dict['Пароль'] = '#######'
new_dict['Код'] = '###4'
print(new_dict["Имя"])
print(new_dict["Пароль"])
print(new_dict["Код"])

new_dict = {'file1.txt': 10, 'file2.txt': 100, 'file3.txt': 101, 'file4.txt': 200, 'file5.txt': 5, 'file6.txt': 305}
for k,v in new_dict.items():
    if v>100:
        print(k)

# список
family_1 = ["Vasya", "Petya"]

# Множества
family_2 = {"Vasya", "Petya", "Vasya"}

# Словарь (ключ: значение)
family_3 = {"Папа": "Вася", "Мама":"Петя"}
print(family_3)
print(family_3.keys())
family_3.get('Папа')
family_3['Папа']
for k,v in family_3.items():
    print(k)