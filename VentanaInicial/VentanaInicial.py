from tkinter import *

principal = Tk()
principal.title("Ventana")

# principal.resizable(False, False)

principal.iconbitmap("python.ico")
principal.geometry("650x580")
principal.config(bg = "red")

FrameNuevo = Frame()
FrameNuevo.pack(fill = "x")
FrameNuevo.config(bg = "yellow")
FrameNuevo.config(width = "325", height = "290")
FrameNuevo.config(bd = 8)
FrameNuevo.config(relief = "sunken")
FrameNuevo.config(cursor = "hand2")
principal.mainloop()