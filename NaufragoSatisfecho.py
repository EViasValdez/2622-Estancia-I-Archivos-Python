print("---- El naufrago satisfecho ----")
print("---- Puesto de hamburgesas ----")
input()

def Hamburguesas():
    F = 1
    Total = 0
    Cantidad = int(input("Ingresar la cantidad de hamburgesas:  "))    

    while F <= Cantidad:
        N = int(input ("Eliga el tipo de hamburgesa \n 1 - Sencilla $20 \n 2 - Doble $25 \n 3.- Triple $28 \n"))
        
        if N == 1:
            Total = Total + 20
        else:
            if N == 2:
                Total = Total + 25
            else:
                Total = Total + 28
        F = F + 1
    Pago = int(input("Ingrese el tipo de pago \n  1- Efectivo  \n 2- Tarjeta \n"))

    if Pago == 1:
        print("El total a pagar de " + str(Cantidad) + " hamburgesas es de: $" + str(Total) + " pesos")
    else:
        if Pago == 2:
            total = total + (total * .05)
            print("El total a pagar de " + str(Cantidad) + " hamburgesas es de : $" + str(Total) + " pesos con aplicacion del 5%")
Hamburguesas()