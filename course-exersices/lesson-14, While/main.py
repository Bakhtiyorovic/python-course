#1

# books = []
# while True:
#     a = input("Enter your favourite book: ")
#     books.append(a)
#     if a.lower() == "":
#         print(books)
#         break

#2
while True:
    a = int(input("Enter your age): "))
    if a <= 4 or a == 0:
        print("It is free")
    elif a < 18:
        print("It would be $2")
    elif a >= 18:
        print("It would be $3")



