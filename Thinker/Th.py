from tkinter import *

VentanaPrincipal = Tk()

PrimerFrame = Frame(VentanaPrincipal, width = 500, height = 400)
PrimerFrame.pack()

label = Label(PrimerFrame, text = "Esto es un texto")
label.pack()

imagen = PhotoImage(file = "PH.png")
Label (PrimerFrame, image = imagen).place(x = 100, y = 200)

VentanaPrincipal.mainloop()