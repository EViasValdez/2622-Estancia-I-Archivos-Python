agenda = {
    "Maria": 395478,
    "Yolanda": 102395,
    "Monserrat": 481293,
    "Ana": 121298,
    "Jose": 302902,
    "Mario": 829855,
    "Angel": 829105,
    "Luis": 930297
}

consultando = True
while consultando:
    print("")
    print("Mi agenda")
    print("----------------")
    print("1. Consultar \n2. Añadir \n3. Modificar \n4. Borrar \n5. Salir")

    opcion = ""

    while opcion not in ("1", "2", "3", "4", "5"):
        opcion = input("-> ")

    if opcion == "1":
        nombre = input("Nombre: ")
        if nombre not in agenda:
            print("Este nombre no existe en la agenda")
        else:
            telefono = agenda[nombre]
            print(nombre, ":", telefono)
    elif opcion == "2":
        nombre = input("Nombre: ")
        if nombre in agenda:
            print("Este nombre ya esta en la agenda")
        else:
            telefono = int(input("Ingrese el telefono: "))
            agenda[nombre] = telefono
            print("El telefono se ha añadido correctamente")
    elif opcion == "3":
        nombre = input("Nombre: ")
        if nombre not in agenda:
            print("Este nombre no existe en la agenda")
        else:
            telefono = int(input("Ingrese el telefono: "))
            agenda[nombre] = telefono
            print("El telefono se ha modificado correctamente")
    elif opcion == "4":
        nombre = input("Nombre: ")
        if nombre not in agenda:
            print("Este nombre no existe en la agenda")
        else:
            del agenda[nombre]
            print("El telefono se ha borrado correctamente")
    elif opcion == "5":
        consultado = False
        print("Gracias por usar este programa")
    
