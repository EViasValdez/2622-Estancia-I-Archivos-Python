print("....................");
print("Calculadora");
print("Por EViasValdez");
print("....................");

Numero1 = int(input("Ingrese el primer numero: "));
Numero2 = int(input("Ingrese el segundo numero: "));

opcion = 0
while True:
    print("""---- Eliga una opcion ----
          1. Suma
          2. Resta
          3. Multiplicacion
          4. Division
          5. Salir del programa""")
    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        print(" ")
        print("El resultado de la suma es ")
        print(Numero1 + Numero2)
    elif opcion == 2:
        print(" ")
        print("El resultado de la resta es ")
        print(Numero1 - Numero2)
    elif opcion == 3:
        print(" ")
        print("El resultado de la multiplicacion es ")
        print(Numero1 * Numero2)
    elif opcion == 4:
        print(" ")
        print("El resultado de la division es ")
        print(Numero1 - Numero2)
    elif opcion == 5:
        break
    else:
        print("El valor colocado no es valido")