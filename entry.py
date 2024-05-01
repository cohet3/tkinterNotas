import sys
import tkinter as tk

from tkinter import ttk, messagebox, Menu



ventana= tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')


# Definimos una variable q podreamos modificar posteriormente(set), (get)
# width es la cantidad de caracteres q ocupa la caja de texto
#state = tk.DISABLED desabilita la inpu
# entrada_var1= tk.StringVar(value='valor POR default')
entrada1 = ttk.Entry(ventana, width=30)
# Para los password show='*',
entrada1.grid(row=0, column=0)

# Etiqueta(label)
etiqueta1= tk.Label(ventana, text='Aqui se mostara el contenidode la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)
# insert agrega un texto
# entrada1.insert(0,'Introduce una cadena')
# entrada1.insert(5,'---')
# entrada1.insert(tk.END, '---')
# entrada1.config(state='readonly')
def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos...')
    sys.exit()
def enviar():
    # recuperamos la informacion a partir de la variable asociada con el texto
    # boton1.config(text=entrada_var1.get())
    # Modificación utilizamos la variable de texto y el método set
    # entrada_var1.set('Cambio...')
    # Recuperar la informacion
    # print(entrada_var1.get())
    # Modificamos el texto del label
    etiqueta1.config(text=entrada1.get())
    # messagebox(cajas de mensajes)
    mensaje1= entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + ' -> Infomativo')
        # messagebox.showerror('Hay un problema papa', mensaje1 + 'Errir')
        # messagebox.showwarning('alerta', mensaje1 + 'alertaa')
def crear_menu():
    # Configurar el menu principal
    menu_principal = Menu(ventana)
    #tearoff =False para evitar que se separe el menu de la interfaz
    submenu_archivo = Menu(menu_principal, tearoff=False)
    # Agregamos una nuevo opción al menu de archivo
    submenu_archivo.add_command(label='nuevo')
    # Agregar un separador
    submenu_archivo.add_separator()
    # Agragamos la opcion de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # Agregamos el submenu al menu principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    # submenu de ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=False)
    # agregamos una nueva opción al submenu
    submenu_ayuda.add_command(label='Acerca De')
    # Agregamois al menu principal este nuevo submenu
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # Mostramos el menu a la ventana principal
    ventana.config(menu=menu_principal)


''' print(entrada1.get())
    boton1.config(text=entrada1.get())
    #Eliminar contenido
    # entrada1.delete(0, tk.END)
    # seleccionar el texto de la caja
    entrada1.select_range(0, tk.END)
    # para hacer efectiva la seleccion de texto
entrada1.focus()'''

crear_menu()
# Creamos un boton
boton1= ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1, sticky='NSWE')

ventana.mainloop()