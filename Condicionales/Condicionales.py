# Condicional if / elif / else.
Numero = int(input("Ingrese un numero: "));

if Numero > 0:
    print("El número es positivo")
elif Numero == 0:
    print("El número no es positivo o negativo")
else:
    print("El número es negativo")

# Condicional anidadas / combinadas.
NumeroRequerido = int(input("Ingrese un numero: "));

if NumeroRequerido > 0 and NumeroRequerido < 98:
    # 0 < NumeroRequerido < 98:
    print("Esta correcto")
    if NumeroRequerido >= 20:
        print("Puede pasar")
else:
    print("No esta correcto")
    print("No puede pasar")