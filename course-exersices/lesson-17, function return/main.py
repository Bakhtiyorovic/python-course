#1

def user_data(name, email, phone_number):
    data = [name, email, phone_number]
    return f'name: {data[0]}, email: {data[1]}, phone_number: {data[2]}'

print(user_data('Max', 'max@gmail.com', '55555555'))

#2

def numbers(x, y, z):
    if x > y and x > z:
        return f'{x} is greater than {y} and {z}'
    elif y > x and y > z:
        return f'{y} is greater than {x} and {z}'
    elif z > x and z > y:
        return f'{z} is greater than {x} and {y}'
    elif x == y == z:
        return f'all equal'


print(numbers(12, 1, 2))
print(numbers(21,1,3))
print(numbers(1, 2, 23))
print(numbers(1, 1, 1 ))




