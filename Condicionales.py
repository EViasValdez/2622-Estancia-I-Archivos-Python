# Condicional if / elif / else
numero = int(input("Ingrese un numero: "));

if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero no es positivo o negativo")
else:
    print("El numero es negativo")

# Condicional anidadas / combinadas
numerorequerido = int(input("Ingrese un numero: "));

if numerorequerido > 0 and numerorequerido < 98:
    # 0 < numerorequerido < 98:
    print("Esta correcto")
    if numerorequerido >= 20:
        print("Puede pasar")
else:
    print("No esta correcto")
    print("No puede pasar")
