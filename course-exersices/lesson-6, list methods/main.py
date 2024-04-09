#1

countries = ['Brazil', 'France', 'USA', 'Germany', 'Italy', 'Uzbekistan']

print(countries)
print(len(countries))

#2

print(sorted(countries))


#3
countries.sort(reverse=True)
print(countries)


#4
numbers = list(range(120, 1200, 2 ))


print(numbers)

#5

x = sum(numbers)
y = min(numbers)
z = max(numbers)
print(x)
print(y)
print(z)

#6

first = numbers[20:]
second = numbers[:20]
print(first)
print(second)


#7


meals = ['pizza', 'cheese', 'burger', 'sausage', 'sushi']
breakfast = meals
print(breakfast)


#8

breakfast.append('vodka')
print(breakfast)