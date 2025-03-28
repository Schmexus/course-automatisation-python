# films = input().split('')
# print(films)

# films = input().split()
# print(films[1]+films[3])

# films = input().split()
# films.pop(-2)
# print(films)

# films = input().split()
# films.append(films[2])
# print(films)

# films = input().split()
# films.insert(3, 'Титаник')
# print(films)

numbers = [1, 2.5, 5, 7, 8, 3.9]
numbers.sort()
int_list= []
float_list= []
for item in numbers:
    if type(item) == int:
        int_list.append(item)
    elif type(item) == float:
        float_list.append(item)
print(int_list)
print(float_list)

