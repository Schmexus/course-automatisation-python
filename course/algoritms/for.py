if sum(list(map(int, input().split()))) > sum(list(map(int, input().split()))):
    print(1)
else:
    print(2)

numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i < 6:
        print(i)

lol = 0
for i in input():
    if i in ('abi'):
        lol+=1
print(lol)

str = input()
a = input()
lol = 0
for i in str:
    if i == a:
      lol+=1
print(lol)

str = input()
for i in str:
    if i in ('0','1','2','3','4','5','6','7','8','9'):
        continue
    print(i)


numbers =  list(map(int, input().split()))
f = 0
for i in numbers:
    f+=i
print(f/len(numbers))

print(*[num for i, num in enumerate(list(map(int, input().split()))) if i % 2 ==0], sep='\n')
# * после принта для распаковки массива по элементам, а sep для указания разделителя между элементами


for i in range(1,11):
    print(i*7)

summa = 0 # можно было так решить: print(sum(map(len, input().split())))
for i in input().split():
    summa += len(i)
print(summa)



films = input().split()
for i, film in enumerate(films):
    print(f"Индекс {i}: {film}")

numbers = list(map(int, input().split())) # Считывание списка чисел
result = 0
for i in numbers:
    if i % 2 == 0:
        result += i
print(result)

numbers = list(map(int, input().split())) # Считывание списка чисел
result = 0
for i in numbers:
    result += i
print(result)


for i in range(1,11): # от 1 до 10
    print(i**2) # возведение в степень

