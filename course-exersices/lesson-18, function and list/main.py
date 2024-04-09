#1

def First_big(text):
    for x in range(len(text)):
        text[x] = text[x].title()

name = ['Mary', 'had', 'a', 'little']
First_big(name)
print(name)


#2


students = ['ali', 'vali', 'hasan', 'husan']


def mark(names):
    mark = {}
    for name in names:
        mar = input(f"Talaba {name.title()}ning bahosini kiriting: ")
        mark[name] = mar
    return mark


mark = mark(students)
print(mark)
print(students)