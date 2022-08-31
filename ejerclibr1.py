Nombre = input("Introduzca el nombre: ")
Horas = int(input("Introduzca las horas laborales: "))
Sueldo = int(input( "Introduzca el sueldo por hora: "))

total = horas * sueldo

if total > 0 and total <= 150:
    sueldo = total - (0.05 * total)
    print("Empresa: ", nombre,"\n""El sueldo neto es:   ", sueldo)

if total > 150 and total <= 300:
    sueldo = (total - (0.07 * total))
    print("Empresa: ", nombre,"\n""El sueldo neto es:  ", sueldo)

if total > 300 and total <= 450:
    sueldo = total - (0.09 * total)
    print("Empresa: ", nombre,"\n""El sueldo neto es:   ", sueldo)
