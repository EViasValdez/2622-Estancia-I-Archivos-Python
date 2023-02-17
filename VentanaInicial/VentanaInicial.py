from tkinter import *

Principal = Tk()
Principal.title("Ventana")

# Principal.resizable(False, False)

Principal.iconbitmap("python.ico")
Principal.geometry("650x580")
Principal.config(bg = "red")

FrameNuevo = Frame()
FrameNuevo.pack(fill = "x")
FrameNuevo.config(bg = "yellow")
FrameNuevo.config(width = "325", height = "290")
FrameNuevo.config(bd = 8)
FrameNuevo.config(relief = "sunken")
FrameNuevo.config(cursor = "hand2")
Principal.mainloop()