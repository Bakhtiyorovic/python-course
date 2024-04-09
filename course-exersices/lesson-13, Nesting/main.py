#1


# George_washington = {
#     'first_name': 'George',
#     'last_name': 'Washington',
#
# }

# Inami_Ishu = {
#     'first_name': 'Inami',
#     'last_name': 'Ishi'
# }
#
# Jhon_Kennedy = {
#     'first_name': 'Jhon',
#     'last_name': 'Kennedy'
# }
#
# politcs = [George_washington, Inami_Ishu, Jhon_Kennedy]
#
#
# plotic = politcs
# print(plotic)


#2


# first_person = {
#     'first_name': 'Jhon',
#     'last_name': 'Anthony',
#     'age':21
# }
#
# second_person = {
#     'first_name': 'Max',
#     'last_name': 'Williams',
#     'age':19
#
# }
# two_people = [first_person, second_person]
# for person in two_people:
#     name = person['first_name']
#     second_name = person['last_name']
#     age = person['age']
#     print(f'{name} {second_name} is {age} years old')


#3

James_movies = {
    'The_first': 'The_godfather',
    'The_second': 'Fury',
    'The_third': 'Fight_club'
}

Max_movies = {
    'The_first': 'The_founder',
    'The_second': 'The_social_network',
    'The_third': 'The_wolf_of_wallstreet'
}

Micheal_movies = {
    'The_first': 'la_la_land',
    'The_second': 'The_notebook',
    'The_third': 'Titanic'
}

people = [James_movies, Max_movies, Micheal_movies]
for person in people:
    first_movie = person["The_first"]
    second_movie = person['The_second']
    third_movie = person['The_third']
    print(f'{person} and their three favorite movies are: {first_movie} and {second_movie} and {third_movie}')