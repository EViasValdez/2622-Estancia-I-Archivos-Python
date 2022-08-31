from random import *

def genNum(minim, maxim):
    try:
        if minim > maxim:
            aux = minim
            minim = maxim
            maxim = aux
        return randint(minim, maxim)
    except TypeError:
        print("Debes de escribir numeros")
        return -1

i = 0
while i < 20:
    print(genNum(1,100))
    i = i + 1
