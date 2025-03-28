numbers = list(map(int, input().split()))
i=0
while numbers[i]>7:
    print(numbers[i])
    i+=1

numbers = list(map(int, input().split()))
i=0
while i<len(numbers):
    if numbers[i] %2 !=0 and numbers[i]%3 !=0:
        print(numbers[i])
    elif numbers[i] == 2 or numbers[i] ==3 :
        print(numbers[i])
    i+=1

number = int(input())
i=1
while i<number+1:
   print(i)
   i+=1

word = input()
a=0
b=len(word)-1
c=0
while a<b:
    if word[a] != word[b]:
        print('Bad')
        break
    a+=1
    b-=1
else: print('Good')

a = int(input())
b = int(input())
result = 0
while a<=b:
    result+=a
    a+=1
print(result)

v_bake = int(input())
min_v_bake = int(input())
rashod = v_bake/10
i = 0
while v_bake >= min_v_bake:
    v_bake-=rashod
    i+= 1
print(i)

number = int(input())
i = 1
while i<=number:
    if number%i == 0:
        print(i)
    i+=1

numbers = input().split()
i = 0
while numbers[i].isalpha() and i<len(numbers):
    print(numbers[i])
    i+=1



import math

numbers = list(map(int, input().split()))
i = 0
while i < len(numbers):
    if numbers[i]%2 !=0:
        print(int(math.pow(numbers[i], 2)))
    i+=1


numbers = list(map(int, input().split()))
i=0
while numbers[i]%2 == 0:
    print(numbers[i])
    i+=1


numbers = list(map(int, input().split()))
i=0
while i != len(numbers):
    if numbers[i] > 7:
        print(str(numbers[i]))
    i+=1