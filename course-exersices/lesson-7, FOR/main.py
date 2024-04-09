#1

names = ['Max', 'Alex', 'Joseph', 'Ron', 'Daniel']
for name in names:
    print(f'{name},how are you?')
print('the code repeated', len(names), ' times')

#2

for x in range(11, 100, 2):
    y = x**3
    print(y)

#3

a = input('First movie: ')
b = input('Second movie: ')
c = input('Third movie: ')
d = input('Fourth movie: ')
e = input('Fifth movie: ')
movies = []
movies.append(a)
movies.append(b)
movies.append(c)
movies.append(d)
movies.append(e)
for movie in movies:
    print(f'movies: {movie}')


