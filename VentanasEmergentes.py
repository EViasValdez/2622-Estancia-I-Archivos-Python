# Importamos Tkinter.
from tkinter import *
Raiz = Tk()
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
def SalirApp():
    Valor = messagebox.askokcancel("salir", "¿Desea salir?")
    if Valor == True:
        Raiz.destroy()
# Cerramos el documento.
def CerrarDocumento():
    Valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento")
    if Valor == False:
        Raiz.destroy()
# Creamos la funcion abrir archivo.
def AbreArchivo():
    Archivo = filedialog.askopenfilename(title = "Abrir", initialdir = "/", filetypes = (("Fichero de Excel", ".xlsx"), ("Fichero de texto", ".txt")))
    print(Archivo)

# Creamos una variable para el menú.
BarraMenu = Menu(Raiz)
Raiz.config(menu = BarraMenu, width = 300, height = 300)

# Establecemos cantidad de elementos.
ArchivoMenu = Menu(BarraMenu, tearoff = 0)

ArchivoMenu.add_command(label = "Nuevo")
ArchivoMenu.add_command(label = "Abrir", command = AbreArchivo)
ArchivoMenu.add_separator() # Esta linea genera una linea separadora.
ArchivoMenu.add_command(label = "Cerrar", command = CerrarDocumento)
ArchivoMenu.add_command(label = "Salir", command = SalirApp)

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
AyudaMenu.add_command(label = "Licencia", command = infoLicencia)
AyudaMenu.add_command(label = "Acerca del programa", command = infoAdicional)

# Poner en consola.
BarraMenu.add_cascade(label = "Archivo", menu = ArchivoMenu)
BarraMenu.add_cascade(label = "Edicion", menu = EdicionMenu)
BarraMenu.add_cascade(label = "Herramientas", menu = HerramientaMenu)
BarraMenu.add_cascade(label = "Ayuda", menu = AyudaMenu)

# Mostrar en pantalla.
Raiz.mainloop()