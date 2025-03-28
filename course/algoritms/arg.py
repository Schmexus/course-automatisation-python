

def summa_chisel_v_stroke(string):
    summa =0
    for i in string:
        try:
            i = int(i)
            summa+=i
        except:
            continue
    print(summa)
summa_chisel_v_stroke(input())

def pochti_max(numbers):
    number = 0
    for i in numbers:
        if i>number and i<max(numbers):
            number = i
    print(number)
pochti_max(list(map(int, input().split())))

def kolvo_glasnih(string):
    s=0
    for i in string:
        if i in 'юияэоаыуе':
            s+=1
    print(s)
kolvo_glasnih(input())

def perevorot_str(string):
    print(string[::-1])

perevorot_str(input())

def proverka_na_chet(number):
    if number % 2 == 0:
        print('Good')
    else:
        print('Bad')


proverka_na_chet(int(input()))



def description(name, age, sex):
    print(f"имя {name}, возраст {age}, гендер {sex}")

description('Anna', 30, 'woman')
description(name='anna', age=20, sex=2)
