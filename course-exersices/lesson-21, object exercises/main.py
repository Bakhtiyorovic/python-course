#1

class cars:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km = 10000
    def get_info(self):
        return f"year: {self.year} company: {self.make} model: {self.model}"

car1 = cars("Porsche", 911, 2019)
car2 = cars("Ford", 'Mustang', 2017)
print(car1.get_info())

print(car2.get_info())
print(car1.km)


#2
print(dir(cars))
print(car1.__dict__)
print(car1.__dict__.keys())