

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
    __num_students = 0
    def __init__(self, name, sure_name, age, student_id):
        super().__init__(name, sure_name, age)
        self.student_id = student_id
        Student.__num_students += 1
    def describe_people(self):
        return f'{self.name} {self.sure_name} and his student id is {self.student_id}'
    @classmethod
    def get_cl_num(cls):
        return cls.__num_students

p1 = People('John', 'Jhonson', 21)
print(p1.describe_people())
p2 = Student('John', 'James', 22, 120000)
print(p2.describe_people())


p3 = Student('Max', 'Jhonson', 23, 218736178)
p4 = Student('Micheal', 'Dorman', 19, 21870078)
p5 = Student('Mike', 'Liman', 20, 218736178)
print(Student.get_cl_num())
