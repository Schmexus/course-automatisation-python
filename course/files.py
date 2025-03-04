with open('file.txt', 'w') as file:
    films = input().split()
    for i in films:
        file.write(i + "\n")
with open('file.txt', 'r') as file:
    for v in file.readlines():
        if films[len(films)-1] in v:
            print(v)
            continue
        print(v + '*****')


with open('file.txt', 'w') as file:
    films = input().split()
    for i in films:
        file.write(i + "\n")
with open('file.txt', 'r') as file:
    value_1 = input()
    for i, v in enumerate(file.readlines(), 1):
        if value_1 in v:
            print(i)


import shutil
value_1 = input()
with open('file_1.txt','w') as file:
    file.write(value_1)
with open('file_2.txt', 'w') as file:
    shutil.copy('file_1.txt', 'file_2.txt')
with open('file_2.txt', 'r') as file:
    print(file.readline())

films = input().split()
file = open('file.txt', 'w')
for i in films:
    file.write(i + '\n')
file.close()
file = open('file.txt','r')
string = file.readlines()
print(len(string))

value_1 = input()
value_2 = input()
file = open('file.txt', 'w')
file.write(value_1 +'\n')
file.close()
file = open('file.txt', 'a')
file.write(value_2)
file.close()
file = open('file.txt', 'r')
string = file.readlines()
for i in range(len(string)):
    print(string[i].strip())

var = input()
fw = open('file.txt', 'w')
fw.write(var)
fw.close()
fw = open('file.txt', 'r')
print(fw.read())


