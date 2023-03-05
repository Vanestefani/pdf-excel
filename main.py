#Importando
import tkinter as tk
from tkinter import filedialog
#ventana principal
root = tk.Tk()
#definir tañano de la ventana  ( anchura x altura)
root.geometry("600x300")
#definir color
root.configure(background="#F3ECB0")
#Nombre de ventana
tk.Wm.wm_title(root,"Extraer tablas pdf a excel")


# refresca la aplicacion ,recoge los eventos 
root.mainloop()