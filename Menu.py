from tkinter import *
Raiz = Tk()

BarraMenu = Menu(Raiz)
Raiz.config(menu = BarraMenu, width = 300, height = 300)

ArchivoMenu = Menu(BarraMenu, tearoff = 0)
ArchivoMenu.add_command(label = "Elemento1")
ArchivoMenu.add_command(label = "Elemento2")
ArchivoMenu.add_separator()
ArchivoMenu.add_command(label = "Elemento3")
ArchivoMenu.add_command(label = "Elemento4")

EdicionMenu = Menu(BarraMenu, tearoff = 0)
EdicionMenu.add_command(label = "SubElemento 1")
EdicionMenu.add_command(label = "SubElemento 2")
EdicionMenu.add_command(label = "SubElemento 3")
EdicionMenu.add_command(label = "SubElemento 4")

HerramientaMenu = Menu(BarraMenu, tearoff = 0)
HerramientaMenu.add_command(label = "SubElemento 1")
HerramientaMenu.add_command(label = "SubElemento 2")
HerramientaMenu.add_command(label = "SubElemento 3")
HerramientaMenu.add_command(label = "SubElemento 4")

AyudaMenu = Menu(BarraMenu, tearoff = 0)
AyudaMenu.add_command(label = "SubElemento 1")
AyudaMenu.add_command(label = "SubElemento 2")
AyudaMenu.add_command(label = "SubElemento 3")
AyudaMenu.add_command(label = "SubElemento 4")

BarraMenu.add_cascade(label = "Archivo", menu = ArchivoMenu)
BarraMenu.add_cascade(label = "Edicion", menu = EdicionMenu)
BarraMenu.add_cascade(label = "Herramientas", menu = HerramientaMenu)
BarraMenu.add_cascade(label = "Ayuda", menu = AyudaMenu)

Raiz.mainloop()