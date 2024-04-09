#1

class People:
    def __init__(self,name, sure_name, age):
        self.name = name
        self.sure_name = sure_name
        self.age = age
    def describe_people(self):
        return f'{self.name} {self.sure_name} is our student'
    def age_info(self):
        return f'He is  {self.age} years old'

class Student(People):
    def __init__(self, name, sure_name, age, student_id):
        super().__init__(name, sure_name, age)
        self.student_id = student_id
    def describe_people(self):
        return f'{self.name} {self.sure_name} and his student id is {self.student_id}'


p1 = People('John', 'Jhonson', 21)
print(p1.describe_people())
p2 = Student('John', 'James', 22, 120000)
print(p2.describe_people())