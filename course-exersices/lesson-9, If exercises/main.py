#1

a = int(input('Enter a even number: '))
if a % 2 == 0 and a != 0:
    print('Thanks')
else:
    print('Not a odd number or zero')

#2

age = int(input('Enter your age: '))
if age < 4 or age > 60:
    print('It is free')
elif age < 18:
    print('It would be $1')
elif age >= 18:
    print('It would be $2')

#3

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
if a == b:
    print('they are equal')
elif a > b:
    print('first number bigger than second')
elif a < b:
    print('first number smaller than second number')

#4

products = ['apple', 'banana', 'cherry', 'grape', 'orange', 'potato', 'pear', 'tomato', 'watermelon', 'malen']
basket = ['apple', 'banana', 'onion', 'cherry', 'garlic']
for basket in basket:
 if basket in products:
    print(f'{basket} is a in the market')
 else:
    print(f'sorry, {basket} is not in the market right now')

#5

products = ['apple', 'banana', 'cherry', 'grape', 'orange', 'potato', 'pear', 'tomato', 'watermelon', 'malen']
a = input('Enter first product name: ')
b = input('Enter second product name: ')
c = input('Enter third product name: ')
d = input('Enter fourth product name: ')
e = input('Enter fifth product name: ')
new_basket = [a, b, c, d, e]
for basket in new_basket:
    if basket in products:
        print(f'{basket} is a available in our market')
    else:
        print(f'sorry, {basket} is not available in our market, right now')

#6

user = ['Max66', 'Jhonny_12', 'micheal_01', 'wolfie', 'panda_dragon']
a = input('Enter a login nickname: ')
new_users = [a]
for i in new_users:
    if i not in user:
        print(f'welcome {i}')
    else:
        print('This nickname exist')

#7

a = int(input('Enter a number: '))
for x in range(2, 10):
    if a % x == 0:
        print(f'{a} is divisible by {x}')
    else:
        print(f'{a} is not divisible by {x}')