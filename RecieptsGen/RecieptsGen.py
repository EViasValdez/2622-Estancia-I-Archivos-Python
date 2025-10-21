from tkinter import *

# Ventana generada.
Ventana = Tk() 

# Dimensiones de la ventana.
Ventana.geometry("1000x700")

# Icono de la ventana.
Ventana.iconbitmap("RG.ico")

# Titulo de la ventana.
Ventana.title("RecieptsGen")

# Primer frame y dimensiones.
Frame1 = Frame(width = 1000, height = 700)

# Campo de nombres.
Label1 = Label(Ventana, text = "Nombre (s)", font = "Tahoma, 12")
Label1.place(x = 60, y = 48)
CampoTexto1 = Entry(Ventana)
CampoTexto1.pack()
CampoTexto1.place(x = 60, y = 80)

# Campo de apellidos.
Label1 = Label(Ventana, text = "Apellidos (s)", font = "Tahoma, 12")
Label1.place(x = 200, y = 48)
CampoTexto1 = Entry(Ventana)
CampoTexto1.pack()
CampoTexto1.place(x = 60, y = 80)