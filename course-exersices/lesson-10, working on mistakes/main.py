#1

son = int(input("Juft son kiriting: "))
if son%2==0:
    print("Raxmat.")
else:
    print("Bu son juft emas")

#2

yosh = int((input("Yoshingiz nechida?: ")))

if yosh<=4 or yosh>=60:
    print('narh = 0')
elif yosh < 18:
    print('narh = 10000')
elif yosh >= 18:
    print("Chipta 20000 so'm")

#3

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

#4

mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

mahsulot = []
for n in range(5):
    mahsulot.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

for savat in mahsulot:
    if savat in mahsulotlar:
        print(f"Do'konimizda {savat} bor")
    elif savat not in mahsulotlar:
        print(f"Do'konimizda {savat} yo'q")

#5

users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")


