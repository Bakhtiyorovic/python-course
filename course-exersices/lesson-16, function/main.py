#1

def user_data(name, age):
    born_year = 2024 - age
    return f"Hello {name}, you were born in {born_year} years"
print(user_data("Max", 18))
print(user_data("Micheal", 19))

#2

def number(first):
    a = first**2
    b = first**3
    print(f'The square of {first} is {a} and th cub is {b}')


number(2)

#3

def number(a):
    if a % 2 == 0:
        print(f'It is even number')
    else:
        print(f'It is odd number')
number(12)
number(1)

#4

def numbers(x, y):
    if x > y:
        print(f'{x} is greater than {y}')
    elif x < y:
        print(f'{x} is less than {y}')
    elif x == y :
        print(f'{x} is equal to {y}')

numbers(1, 2)
numbers(2, 3)

numbers(3, 3)