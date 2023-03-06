# GUI- Graphical User Interface
# Tkinter - TK Interface
# Importamos el módulo de tkinter
import tkinter as tk
#importamos el modulo del tema de tkinter
from tkinter import ttk
#creamos un objeto usando la clase tk
ventana= tk.Tk()
#Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x800')
# Cambiamos el nombre de la ventana
ventana.title('VentanaRelax')
# Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')

#Creamos un metodo evento_click
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecución del evento click')
    # Creamos un nuevo boton y lo mostramos
    boton2 = ttk.Button(ventana, text='nuevo boton')
    boton2.pack()
    
# Creamos un boton (widget), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Darclick', command=evento_click)
# Utilizar el pack layout manager para mostrar el boton1.pack()
boton1.pack()

# Iniciamos la ventana(esta línea la ejecutamos al final)
#si lo ejecutamos antes, no se muestan los cambios anteriores
ventana.mainloop()