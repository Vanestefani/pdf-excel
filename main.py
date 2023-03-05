#Importando
import io
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from PyPDF2 import PdfReader

#Definicion variables
colorFondo='#F3ECB0'
tamañoVentanaPrincipal="600x400"
colorPrimario='#344D67'
colorSecundario='#ADE792'
colorTerciario='#6ECCAF'
Fuente='Courier'
tamaño_fuente=14
opciones = ["CSV", "Excel"]
#ventana principal
root = tk.Tk()
# Cargar el archivo .ico
imagen_icono = Image.open("./Img/icono.ico")
icono = ImageTk.PhotoImage(imagen_icono)
# Establecer el icono de la ventana
root.iconphoto(True, icono)

#definir tañano de la ventana  ( anchura x altura)
root.geometry(tamañoVentanaPrincipal)
#definir color
root.configure(background=colorFondo)
#Nombre de ventana

tk.Wm.wm_title(root,"Extraer tablas pdf a excel")

header =tk.Frame(root, height=20, bg=colorSecundario)
header.pack(side="top", fill=tk.BOTH)
tk.Label(header, text="Extraer tablas pdf a excel", font=("Arial", 24, "bold"), padx=20, pady=20, bg=colorSecundario).pack(side="left")

tk.Label(header, text="Versión 1.0", font=("Arial", 16), padx=20, pady=20, bg=colorSecundario).pack(side="left")



#Funcion para abrir archivo
def open_file():
    file_path = filedialog.askopenfilename(title="Selecciona archivo")
    print("Archivo seleccionado :", file_path)
#Creacion de boton para subir archivo
file_button = tk.Button(root, text="Selecciona archivo", command=open_file , font=(Fuente,tamaño_fuente) ,bg=colorTerciario , fg="white")
file_button.pack(
   
    expand=True
)

# Definir la variable de control y establecer el valor predeterminado
var = tk.StringVar(value=opciones[0])

# Crear la lista desplegable
lista_desplegable = tk.OptionMenu(root, var, *opciones)
lista_desplegable.pack()

# refresca la aplicacion ,recoge los eventos 
root.mainloop()