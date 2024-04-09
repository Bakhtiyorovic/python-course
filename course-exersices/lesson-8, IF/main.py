#1

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

#2

a = input('Enter your nickname: ')
if a == 'admin':
    print('Hello Admin, you want to see your users')
else:
    print(f'Hello {a}, we nice to see you in our server')

#3

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
if a == b:
    print('It is equal')
else:
    print('not equal')


#4

a = int(input('Enter first number: '))
if a > 0 or a == 0 :
    print('it is positive number')
else:
    print('it is negative number')


#5

a = int(input('Enter a number: '))
if a > 0:
    print(a**(1/2))
else:
    print('Not negative number or zero')