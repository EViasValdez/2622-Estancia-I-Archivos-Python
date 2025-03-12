print("Conversor de monedas")
print("Por EViasValdez")

def Conversor(MonedaActual, Valor, MonedaaConvertir):
    if MonedaActual == 1:
        def ToDolar():
            if MonedaaConvertir == "1":
                print(f"{Valor} dólares equivalen a ${Valor * 0.49} pesos colombianos")
            elif MonedaaConvertir == "2":
                print(f"{Valor} dólares equivalen a ¥{Valor * 6.37} yuanes o yenes")
            elif MonedaaConvertir == "3":
                print(f"{Valor} dólares equivalen a £{Valor * 0.76} libras")
            else:
                print("Moneda no reconocida")
        ToDolar()

    elif MonedaActual == 2:
        def ToEuro():
            if MonedaaConvertir == "1":
                print(f"{Valor} dólares equivalen a ${Valor * 4000} pesos colombianos")
            elif MonedaaConvertir == "2":
                print(f"{Valor} dólares equivalen a ¥{Valor * 6.93} yuanes o yenes")
            elif MonedaaConvertir == "3":
                print(f"{Valor} dólares equivalen a £{Valor * 0.83} libras")
            else:
                print("Moneda no reconocida")
        ToEuro()
    else:
        print("Moneda no reconocida")

MonedaActual = int(input("Ingrese su moneda actual; \n 1. Dólar \n 2. Euro \n"))
Valor = float(input("Ingrese el valor a convertir: \n"))
MonedaaConvertir = input("¿A qué valor desea convertirlo? \n 1. Pesos Colombianos \n 2. Yuanes \n 3. Libras esterlinas \n")
Conversor(MonedaActual, Valor, MonedaaConvertir)