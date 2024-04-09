#1

my_bro = {
    'Name': 'Max',
    'Age':18,
    'Gender': 'Male'
}

print(f'my homies name is {my_bro["Name"]} and he is {my_bro["Age"]}')

#2

keywords = {
    'string':'uses for words',
    'integer':'uses for integers'
}
print(keywords)


#3


words = {
    'apple': 'olma',
    'banana': 'banan',
    'table':'stul'
}

a = input('Enter a word: ')
if a in words.keys():
    print(words[a])
else:
    print('Not found')
