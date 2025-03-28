new_list = input().split()
lol= 1
for i in new_list:
    print(str(lol)+'.'+str(i))
    lol+=1

new_list = input().split()
for i in new_list:
    if i in '0123456789!@#$%^&*()_+':
        continue
    else:
        print('я люблю', i)

films = input().split()
chet = 0
for i in films:
    try:
        i=float(i)
        chet+=1
    except:
        continue
print(chet)

string = input()
lol = 0
for letter in string:
    if letter in r"!@#$%^&*()_+=-/\.',;:][}{|":
       lol+=1
print(lol)

films = input().split()
chet = 0
for i in films:
    if i.isdigit():
        chet+=0
    else:
        chet+=1
print(chet)

from statistics import mode
numbers = list(map(int, input().split()))
print(mode(numbers))

files = input().split()
py = '.py'
for file in files:
    if file.endswith('.py'):
        print(file)

numbers = list(map(int, input().split()))
para = 0
for i in numbers:
    for j in numbers:
        print(i,j)
        if numbers[i]==numbers[j]:
            para+=1
print(para)

films = input().split()
chet = 0
for i in films:
    if i.isdigit():
        chet+=int(i)
    else:
        chet+=len(i)
print(chet)

films = input().split()
for i in films:
    if len(i) >5:
        print(i)

numbers = list(map(int, input().split()))
summa = 0
for i in numbers:
    if i < 0:
        break
    summa+=i
print(summa)

numbers = list(map(int, input().split()))
for i in numbers:
    if i < 0:
        continue
    print(i)

numbers = list(map(int, input().split()))
max = max(numbers)
premax = 0
for i in numbers:
    if premax > max:
        continue
    elif i > premax and i < max:
        premax=i
print(premax)

numbers = list(map(int, input().split()))
for i in numbers:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
    continue

numbers = list(map(int, input().split()))
max= 0
min=0
for i in numbers:
    if i>0:
        max+=1
    elif i<0:
        min+=1
print(max)
print(min)

numbers = list(map(int, input().split()))
for i in numbers:
    if i % 2 == 0:
        continue
    else:
        print(i)

numbers = list(map(int, input().split()))
for i in numbers:
    if i < 0:
        print(i)
        break

