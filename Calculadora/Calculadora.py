print("....................");
print("Calculadora");
print("Por EViasValdez");
print("....................");

Numero1 = int(input("Ingrese el primer número: "));
Numero2 = int(input("Ingrese el segundo número: "));

Opcion = 0
while True:
    print("""---- Elija una opción ----
          1. Suma
          2. Resta
          3. Multiplicación
          4. División
          5. Salir del programa""")
    Opcion = int(input("Seleccione una opción: "))

    if Opcion == 1:
        print(" ")
        print("El resultado de la suma es: ")
        print(Numero1 + Numero2)
    elif Opcion == 2:
        print(" ")
        print("El resultado de la resta es: ")
        print(Numero1 - Numero2)
    elif Opcion == 3:
        print(" ")
        print("El resultado de la multiplicación es: ")
        print(Numero1 * Numero2)
    elif Opcion == 4:
        print(" ")
        print("El resultado de la división es: ")
        print(Numero1 - Numero2)
    elif Opcion == 5:
        break
    else:
        print("El valor colocado no es válido")