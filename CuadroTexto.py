from tkinter import *

VentanaPrincipal = Tk()

FramePrincipal = Frame(VentanaPrincipal, width = 800, height = 400)
FramePrincipal.pack()

CuadroTexto1 = Entry(FramePrincipal)
CuadroTexto1.grid(row = 0, column = 1, padx = 10, pady = 10)
CuadroTexto1.config(fg = "red", justify = "center")
CuadroTexto2 = Entry(FramePrincipal)
CuadroTexto2.grid(row = 1, column = 1, padx = 10, pady = 10)
CuadroTexto3 = Entry(FramePrincipal)
CuadroTexto3.grid(row = 2, column = 1, padx = 10, pady = 10)
CuadroPass = Entry(FramePrincipal)
CuadroPass.grid(row = 3,column = 1, padx = 10, pady = 10)
CuadroPass.config(show = "*")

NombreLabel1 = Label(FramePrincipal, text = "Nombre: ")
NombreLabel1.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)
NombreLabel2 = Label(FramePrincipal, text = "Apellido: ")
NombreLabel2.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)
NombreLabel3 = Label(FramePrincipal, text = "Dirección: ")
NombreLabel3.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)
PassLabel3 = Label(FramePrincipal, text = "Contrasenia: ")
PassLabel3.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)

VentanaPrincipal.mainloop()