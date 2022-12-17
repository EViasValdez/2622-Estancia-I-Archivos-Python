Nombre = input("Introduzca el nombre: ")
Horas = int(input("Introduzca las horas laborales: "))
Sueldo = int(input( "Introduzca el sueldo por hora: "))

Total = horas * sueldo

if Total > 0 and Total <= 150:
    sueldo = Total - (0.05 * Total)
    print("Empresa: ", Nombre,"\n""El sueldo neto es:   ", Sueldo)

if Total > 150 and Total <= 300:
    sueldo = (Total - (0.07 * Total))
    print("Empresa: ", Nombre,"\n""El sueldo neto es:  ", Sueldo)

if Total > 300 and Total <= 450:
    Sueldo = Total - (0.09 * Total)
    print("Empresa: ", Nombre,"\n""El sueldo neto es:   ", Sueldo)