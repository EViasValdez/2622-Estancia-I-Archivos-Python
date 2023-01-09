from random import *

def genNum(Minim, Maxim):
    try:
        if Minim > Maxim:
            Aux = Minim
            Minim = Maxim
            Maxim = Aux
        return randint(Minim, Maxim)
    except TypeError:
        print("Debes de escribir numeros")
        return -1

i = 0
while i < 20:
    print(genNum(1,100))
    i = i + 1
