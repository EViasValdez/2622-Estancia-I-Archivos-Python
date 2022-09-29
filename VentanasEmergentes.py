# Importamos Tkinter.
from tkinter import *
raiz = Tk()
# Importamos messagebox.
from tkinter import messagebox
# Importamos filedialog.
from tkinter import filedialog

# Creamos una ventana con información.
def infoAdicional():
    messagebox.showinfo("Titulo del programa", "Inserte titulo aqui")
# Creamos una ventana con advertencia.
def infoLicencia():
    messagebox.showwarning("Licencia", "Licencia activada")
# Creamos una ventana de pregunta.
def salirApp():
    valor = messagebox.askokcancel("salir", "¿Desea salir?")
    if valor == True:
        raiz.destroy()
# Cerramos el documento.
def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar","No es posible cerrar el documento")
    if valor == False:
        raiz.destroy()
# Creamos la funcion abrir archivo.
def abreArchivo():
    archivo = filedialog.askopenfilename(title = "Abrir", initialdir = "/", filetypes = (("Fichero de Excel", ".xlsx"), ("Fichero de texto", ".txt")))
    print(archivo)

# Creamos una variable para el menú.
barraMenu = Menu(raiz)
raiz.config(menu = barraMenu, width = 300, height = 300)

# Establecer cantidad de elementos.
archivoMenu = Menu(barraMenu, tearoff = 0)

archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Abrir", command = abreArchivo)
archivoMenu.add_separator() # Genera una linea separadora.
archivoMenu.add_command(label = "Cerrar", command = cerrarDocumento)
archivoMenu.add_command(label = "Salir", command = salirApp)

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
ayudaMenu.add_command(label = "Licencia", command = infoLicencia)
ayudaMenu.add_command(label = "Acerca del programa", command = infoAdicional)

# Poner en consola.
barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Edicion", menu = edicionMenu)
barraMenu.add_cascade(label = "Herramientas", menu = herramientaMenu)
barraMenu.add_cascade(label = "Ayuda", menu = ayudaMenu)

# Mostramos en pantalla.
raiz.mainloop()