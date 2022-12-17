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

Consultando = True
while Consultando:
    print("")
    print("Mi agenda")
    print("----------------")
    print("1. Consultar \n 2. Añadir \n 3. Modificar \n 4. Borrar \n 5. Salir")

    Opcion = ""

    while Opcion not in ("1", "2", "3", "4", "5"):
        Opcion = input("-> ")

    if Opcion == "1":
        Nombre = input("Nombre: ")
        if Nombre not in Agenda:
            print("Este nombre no existe en la agenda")
        else:
            telefono = Agenda[Nombre]
            print(Nombre, ":", telefono)
    elif Opcion == "2":
        Nombre = input("Nombre: ")
        if Nombre in Agenda:
            print("Este nombre ya esta en la agenda")
        else:
            telefono = int(input("Ingrese el telefono: "))
            Agenda[Nombre] = telefono
            print("El telefono se ha añadido correctamente")
    elif Opcion == "3":
        Nombre = input("Nombre: ")
        if Nombre not in Agenda:
            print("Este nombre no existe en la agenda")
        else:
            telefono = int(input("Ingrese el telefono: "))
            Agenda[Nombre] = telefono
            print("El telefono se ha modificado correctamente")
    elif Opcion == "4":
        Nombre = input("Nombre: ")
        if Nombre not in Agenda:
            print("Este nombre no existe en la agenda")
        else:
            del Agenda[Nombre]
            print("El telefono se ha borrado correctamente")
    elif Opcion == "5":
        Consultado = False
        print("Gracias por usar este programa")