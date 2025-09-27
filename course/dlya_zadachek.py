def delete_char_from_string(string,char):
    return string.replace(char,'')

def delete_numbers_from_string(string):
    text = string
    for number in '0123456789':
        text = text.replace(number,'')
    return text

def delete_dublicated_char(string):
    return ''.join(dict.fromkeys(string))

def polindrom(string):
    text = string.replace(' ','').lower()
    if text == text[::-1]:
        print(' данный текст - полиндром')

def kolvo_glasnih(string):
    i=0
    for char in string.lower():
        if char in {'a', 'e', 'i', 'o', 'u', 'y'}:
            i+=1
    return i

string = input('Введите строку: ')
print(kolvo_glasnih(string))


def rand_massiv():
    massiv = set()
    while massiv.__len__() !=9:
        massiv.add(random.randint(1,50))
    massiv = list(massiv)
    for i,v in enumerate(massiv):
        if i%3==0:
            print('\n')
            print(v, massiv[i+1], massiv[i+2])

rand_massiv()