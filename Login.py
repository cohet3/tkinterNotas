import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        # Ventana config main
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0,0)
        # ventana grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()
        # Definir el método crear_componentes
    def _crear_componentes(self):
        # etiquetas de entradas
        etiqueta_usuario = ttk.Label(self, text='Usuario:')
        etiqueta_usuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        etiqueta_password = ttk.Label(self, text='Password:')
        etiqueta_password.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        # entradas de datos
        self.entrada_usuario = ttk.Entry(self)
        self.entrada_usuario.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        self.entrada_password = ttk.Entry(self, show='*')
        self.entrada_password.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
# Creamos un boton login
        login_boton = ttk.Button(self, text='Login', command=self._login)
        login_boton.grid(row=3, column=0, columnspan=2)

    def _login(self):
        messagebox.showinfo('Datos Login',
                    f'{self.entrada_usuario.get()}, Password: {self.entrada_password.get()}')

if __name__ == '__main__':
    login_ventana = Login()
    login_ventana.mainloop()