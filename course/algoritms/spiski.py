# movies = input().split('')
# print(movies)

# movies = input().split()
# print(movies[1]+movies[3])

# movies = input().split()
# movies.pop(-2)
# print(movies)

# movies = input().split()
# movies.append(movies[2])
# print(movies)

# movies = input().split()
# movies.insert(3, 'Титаник')
# print(movies)

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

