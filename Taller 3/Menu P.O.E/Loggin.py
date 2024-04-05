import tkinter as tk
from tkinter import *
from tkinter import messagebox

from MenuCorresponsal import MenuCorresponsal
from SerializadorCorresponsal import SerializadorCorresponsal
from MenuCliente import MenuCliente
from SerializadorCliente import SerializadorCliente

from Tooltip import Tooltip

class Loggin():
    def salirSistema(self, event=None):
        respuesta = messagebox.askquestion("Confirmación", "Esta seguro de Salir?")
        if respuesta == "yes":
            self.ventana.destroy()
        else:
            pass

    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Debe diligenciar todos los campos marcados con *\nluego presione el boton Ingresar")

    def verCaracteres(self, event):
        self.txtPassword.configure(show='')
        self.btnVer.configure(text="Ocultar")
    
    def ocultarCaracteres(self, event):
        self.txtPassword.configure(show='*')
        self.btnVer.configure(text="Ver")
    
    def validarLongitud(self, event):
        longitud = len(self.txtPassword.get())
        if(longitud >= 8):
            self.btnIngresar.configure(state="normal")
        
        else:
            self.btnIngresar.configure(state="disable")

    def validarIngreso(self, event=None):
        usuario = self.txtUsuario.get()
        password = self.txtPassword.get()
        cliente = None
        if(len(usuario) >= 8 and len(password) >= 8):
            miSerializadorCliente = SerializadorCliente()
            listaClientes = miSerializadorCliente.leerArchivo()
            encontrado = False
            for cliente in listaClientes:
                if(cliente.getNombre()+"."+cliente.getApellido() == usuario and cliente.getCedula() == password):
                    miMenu = MenuCliente(self.ventana, cliente)
                    encontrado = True
                    break
            if(encontrado == False):
                miSerializadorCorresponsal = SerializadorCorresponsal()
                listaCorresponsales = miSerializadorCorresponsal.leerArchivo()
                for corresponsal in listaCorresponsales:
                    if(corresponsal.getNombre()+"."+ corresponsal.getApellido() == usuario and corresponsal.getCedula() == password):
                        miMenu = MenuCorresponsal(self.ventana, corresponsal, cliente)
                        encontrado = True
                        break
                if(encontrado == False):
                    messagebox.showwarning("Advertencia", "Usuario y/o Password incorrectos, verifique de nuevo.")
        else:
            messagebox.showwarning("Advertencia", "El Usuario y Contraseña deben terner mínimo 8 caracteres.")

    def limpiarCampos(self, event=None):
        self.txtUsuario.delete(0, tk.END)
        self.txtPassword.delete(0, tk.END)

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de Sesión")
        self.ventana.resizable(0,0)
        self.ventana.config(width=350, height=250)

        self.lblTitulo = tk.Label(self.ventana, text="Inicio Sesión")
        self.lblTitulo.place(relx=0.5, y=65, anchor="center")
        iconoAyuda = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=25, width=25,height=25)
        Tooltip(self.btnAyuda, "Presioname para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)

        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

        self.lblUsuario = tk.Label(self.ventana, text="Usuario*:")
        self.lblUsuario.place(x=60, y=100)
        self.lblPassword = tk.Label(self.ventana, text="Password*:")
        self.lblPassword.place(x=50, y=130)

        self.btnVer =  tk.Button(self.ventana, text="Ver")
        self.btnVer.place(x=270, y=125)

        self.btnVer.bind("<Enter>", self.verCaracteres)
        self.btnVer.bind("<Leave>", self.ocultarCaracteres)

        self.txtUsuario = tk.Entry(self.ventana, width=25)
        self.txtUsuario.place(x=115, y=100)
        Tooltip(self.txtUsuario, "Ingrese su Nombre seguido de un punto(.) y luego su Apellido.\nsin espacios y en minuscula")
    
        self.txtPassword = tk.Entry(self.ventana, width=25, show='*')
        self.txtPassword.place(x=115, y=130)
        Tooltip(self.txtPassword, "Su contraseña es el Numero de Identificacion!\nminimo 8 caracteres")
        self.txtPassword.bind("<KeyRelease>", self.validarLongitud)
        
        iconoIngresar = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\door_in.png")
        self.btnIngresar = tk.Button(self.ventana, text="Ingresar", image=iconoIngresar, compound=LEFT, command=lambda: self.validarIngreso())
        self.btnIngresar.place(x=80, y=170)
        Tooltip(self.btnIngresar, "¡Clic para Ingresar!\nEnter")
        self.ventana.bind("<Return>", self.validarIngreso)

        iconoLimpiar = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\textfield_delete.png")
        self.btnLimpiar =  tk.Button(self.ventana, text="Limpiar", image=iconoLimpiar, compound=LEFT, command=lambda: self.limpiarCampos())
        self.btnLimpiar.place(x=150, y=170)
        Tooltip(self.btnLimpiar, "¡Clic para Limpiar!\nControl+l")
        self.ventana.bind("<Control-l>", self.limpiarCampos)

        iconoSalir = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\cancel.png")
        self.btnSalir = tk.Button(self.ventana, text="Salir", image=iconoSalir, compound=LEFT, command=lambda: self.salirSistema())
        self.btnSalir.place(x=220, y=170)
        Tooltip(self.btnSalir, "¡Clic para Salir!\nControl+s")
        self.ventana.bind("<Control-s>", self.salirSistema)


        self.ventana.mainloop()