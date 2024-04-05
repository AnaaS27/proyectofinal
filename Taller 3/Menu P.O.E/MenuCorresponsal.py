import tkinter as tk
from tkinter import *
from tkinter import messagebox

from CrearCliente import CrearCliente
from ModificarCliente import ModificarCliente
from EliminarCliente import EliminarCliente

class MenuCorresponsal():
    def salirApp(self):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def registrarCliente(self):
        crearCliente = CrearCliente(self.ventana, self.corresponsal)
    def modificarCliente(self):
        cliente = None
        editarCliente = ModificarCliente(self.ventana, self.corresponsal, cliente)
    def eliminarCliente(self):
        eliminarCliente = EliminarCliente(self.ventana, self.corresponsal)
    

    def __init__(self, loggin, corresponal, cliente):
        self.ventana = tk.Toplevel(loggin)
        self.ventana.geometry("400x450")
        self.ventana.focus_set() #Esta función asigna el foco a la ventana secundaria
        self.ventana.title("Menu Principal")
        self.ventana.resizable(0,0)

        self.corresponsal = corresponal
        self.cliente = cliente

        self.menu = tk.Menu(self.ventana)#Creamos barra de herramientas y ubicamos en ventana
        self.ventana.config(menu=self.menu)
        menuClientes = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Clientes", menu=menuClientes)
        menuClientes.add_command(label="Crear Cliente", command=lambda: self.registrarCliente())
        menuClientes.add_separator()
        menuClientes.add_command(label="Modificar Cliente", command=lambda: self.modificarCliente())
        menuClientes.add_separator()
        menuClientes.add_command(label="Eliminar Cliente", command=lambda: self.eliminarCliente())

        menuCuentas = tk.Menu(self.menu)#Creamos opcion de menu y ubicamos en la barra
        self.menu.add_cascade(label="Gestionar Cuentas", menu=menuCuentas)
        menuCuentas.add_command(label="Crear Cuenta")
        menuCuentas.add_separator()
        menuCuentas.add_command(label="Eliminar Cuenta")
        
        menuTransacciones = tk.Menu(self.menu)
        self.menu.add_cascade(label="Gestionar Transacciones", menu=menuTransacciones)
        menuTransacciones.add_command(label="Realizar Retiro")
        menuTransacciones.add_separator()
        menuTransacciones.add_command(label="Realizar Depósito")
        
        menuConsultas = tk.Menu(self.menu)
        self.menu.add_cascade(label="Consultar Información", menu=menuConsultas)

        salirMenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Salir", menu=salirMenu)
        salirMenu.add_command(label="Salir", command=lambda: self.salirApp())

        messagebox.showinfo("Saludo", "Bienvenido "+self.corresponsal.getNombre()+" "+self.corresponsal.getApellido())

        self.ventana.mainloop()