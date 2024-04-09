#1


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def __str__(self):
        return f'name: {self.first_name}, second name: {self.last_name} and email {self.email}'


user1 = User('John', 'Doe', 'jhon@localhost')
user2 = User('Max', 'James', 'mail@localhost')
print(user1)
print(user2)

#2

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

