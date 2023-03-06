import tkinter as tk
from tkinter import ttk

ventana= tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')
# Configurar el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)
# Métodos de los eventos
def evento1():
    boton1.config(text='Botón 1 presionado')

def evento():
    boton2.config(text='Botón 2 presionado')

def evento4():
    boton4.config(text='Botón 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')

# Definimos dos botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0, sticky='NSWE',
            padx=40, pady=40, ipadx=20, ipady=50, columnspan=2)

# N,(arriba) E(derecha), S(abajo), W(izq)
boton2 = ttk.Button(ventana, text='Boton2', command=evento)
boton2.grid(row=1, column=0, sticky='NSWE')
# BOTON 3
boton3 = ttk.Button(ventana, text='Boton3', command=evento)
boton3.grid(row=2, column=3, sticky='NSWE')
# BOTON 4
boton4 = tk.Button(ventana, text='Boton4', command=evento4)
boton4.grid(row=1, column=1, sticky='NSWE')
ventana.mainloop()
#para personalizar hay q usar el paquete tk