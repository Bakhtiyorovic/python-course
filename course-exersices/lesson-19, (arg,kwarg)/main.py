#1


def number(x):
    print(x*x)

number(1)
number(2)
number(4)

#2

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')

print(talaba)