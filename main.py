#Importando
import io
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from PyPDF2 import PdfReader

#Definicion variables
colorFondo='#F3ECB0'
tamañoVentanaPrincipal="600x400+0+0"
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

#Añadir encabesado
header = tk.Frame(root,height=20, bg=colorSecundario)
header.grid(row=0, column=0, sticky="new", padx=0)
header.columnconfigure(0, weight=1)
header.rowconfigure(0, weight=1)

#Encabezado
tk.Label(header, text="Extraer tablas pdf a excel", font=("Arial", 24, "bold"), padx=20, pady=20, bg=colorSecundario).grid(row=0, column=1, sticky="ew")
tk.Label(header, text="Versión 1.0", font=("Arial", 16), padx=20, pady=20, bg=colorSecundario).grid(row=0, column=2, sticky="ew")


##Creando frame para contenido
contenido  = tk.Frame(root,  height=100, bg=colorFondo)
contenido.grid(row=1, column=0, padx=10, pady=5, sticky='new')
tk.Label(contenido, text="Subir archivo", font=("Arial", 16), padx=20, pady=20, bg=colorFondo).grid(row=0, column=1, sticky="ew")

#Funcion para abrir archivo
def open_file():
     file_path = filedialog.askopenfilename(
        initialdir='./',
        title='Seleccionar archivo',
        filetypes=[('Archivos PDF', '*.pdf')]
    )
   
#Creacion de boton para subir archivo
file_button = tk.Button(contenido, text="Selecciona archivo", command=open_file , font=(Fuente,tamaño_fuente) ,bg=colorTerciario , fg="white")
file_button.grid(row=0, column=2, padx=0, pady=0)
# Definir la variable de control y establecer el valor predeterminado
var = tk.StringVar(value=opciones[0])

# Crear la lista desplegable
tk.Label(contenido, text="Convertir a ", font=("Arial", 16), padx=20, pady=20, bg=colorFondo).grid(row=2, column=1, sticky="ew")

lista_desplegable = tk.OptionMenu(contenido, var, *opciones)
lista_desplegable.grid(row=2, column=2, padx=0, pady=0)

# Configuración de las columnas y filas de la ventana
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# refresca la aplicacion ,recoge los eventos 
root.mainloop()