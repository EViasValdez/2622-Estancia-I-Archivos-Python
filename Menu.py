from tkinter import *
raiz = Tk()

barraMenu = Menu(raiz)
raiz.config(menu = barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Elemento1")
archivoMenu.add_command(label = "Elemento2")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Elemento3")
archivoMenu.add_command(label = "Elemento4")

edicionMenu = Menu(barraMenu, tearoff = 0)
edicionMenu.add_command(label = "SubElemento 1")
edicionMenu.add_command(label = "SubElemento 2")
edicionMenu.add_command(label = "SubElemento 3")
edicionMenu.add_command(label = "SubElemento 4")

herramientaMenu = Menu(barraMenu, tearoff = 0)
herramientaMenu.add_command(label = "SubElemento 1")
herramientaMenu.add_command(label = "SubElemento 2")
herramientaMenu.add_command(label = "SubElemento 3")
herramientaMenu.add_command(label = "SubElemento 4")

ayudaMenu = Menu(barraMenu, tearoff = 0)
ayudaMenu.add_command(label = "SubElemento 1")
ayudaMenu.add_command(label = "SubElemento 2")
ayudaMenu.add_command(label = "SubElemento 3")
ayudaMenu.add_command(label = "SubElemento 4")

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Edicion", menu = edicionMenu)
barraMenu.add_cascade(label = "Herramientas", menu = herramientaMenu)
barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)

raiz.mainloop()