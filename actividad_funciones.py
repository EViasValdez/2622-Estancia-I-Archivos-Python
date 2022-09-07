print("Conversor de monedas")
print("Por EViasValdez")

def conversor(MonedaActual, Valor, MonedaAConvertir):
    if MonedaActual == 1:
        def ToDolar():
            if MonedaAConvertir == "1":
                print(f"{Valor} dolares equivale a ${Valor * 0.49} pesos colombianos")
            elif MonedaAConvertir == "2":
                print(f"{Valor} dolares equivale a ¥{Valor * 6.37} yuanes")
            elif MonedaAConvertir == "3":
                print(f"{Valor} dolares equivale a £{Valor * 0.76} libras")
            else:
                print("Moneda no reconocida")
        
        ToDolar()

    elif MonedaActual == 2:
        def ToEuro():
            if MonedaAConvertir == "1":
                print(f"{Valor} dolares equivale a ${Valor * 4000} pesos colombianos")
            elif MonedaAConvertir == "2":
                print(f"{Valor} dolares equivale a ¥{Valor * 6.93} yuanes o yenes")
            elif MonedaAConvertir == "3":
                print(f"{Valor} dolares equivale a £{Valor * 0.83} libras")
            else:
                print("Moneda no reconocida")

        ToEuro()
    else:
        print("Moneda no reconocida")

MonedaActual = int(input("Ingrese su moneda actual; \n 1. Dolar \n 2. Euro \n"))
Valor = float(input("Ingrese el valor a convertir: \n"))
MonedaAConvertir = input("¿A que valor desea convertirlo? \n 1. Pesos Colombianos \n 2. Yuanes \n 3. Libras esterlinas \n")
conversor(MonedaActual, Valor, MonedaAConvertir)