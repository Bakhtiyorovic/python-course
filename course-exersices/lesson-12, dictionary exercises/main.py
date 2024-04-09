#1

words = {
    'apple': 'apple',
    'banana': 'banana',
    'orange': 'orange',
    'grape': 'grape',
    'cherry':'blue'
}
for x in words.items():
    print(x)

#2

countries = {
    'USA':'Washington',
    'France':'Paris',
    'Germany':'Berlin',
    'Ireland':'Dublin',
    'Japan':'Tokyo'
}

for x in countries.keys():
    print(f'countries: {x} ')
for y in countries.values():
    print(f'and their capitals:{y}')

#3


countries = {
    'USA':'Washington',
    'France':'Paris',
    'Germany':'Berlin',
    'Ireland':'Dublin',
    'Japan':'Tokyo'
}

a = input('Enter a country name: ')
if a.title() in countries:
    print(countries[a.title()])
else:
    print('not founded')

#4

meals = {
    'chicken':'$12',
    'tomato pasta':'$10',
    'chicken pasta':'$21',
    'pizza':'$7',
    'sushi':'$11',
    'burger':'$3.2'
}

a = input('First meal: ')
b = input('Second meal: ')
c = input('Third meal: ')
d = [a, b, c]
for x in d:
    if x in meals:
     print(f'that would be {meals[x]}')
    elif x not in meals:
     print('we dont have that')

