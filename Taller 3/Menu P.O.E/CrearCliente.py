import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class CrearCliente:

    def salir1(self, event=None):
        respuesta = messagebox.askquestion("Confirmación", "¿Está seguro de salir?")
        if respuesta == "yes":
            self.ventana.destroy()

    def mostrarAyuda(self, event):
        messagebox.showinfo("Ayuda", "Bienvenido al formulario de creación de cliente.\nPor favor complete los campos requeridos.")
        

    def __init__(self, menu, corresponsal):
        self.ventana = tk.Toplevel(menu)
        self.ventana.title("Gestionar Clientes")
        self.ventana.resizable(0,0)
        self.ventana.config(width=350, height=300)

        self.corresponsal = corresponsal
        
        self.lblTitulo = tk.Label(self.ventana, text="Crear Usuario")
        self.lblTitulo.place(relx=0.5, y=40, anchor="center")

        self.lblCedula = tk.Label(self.ventana, text="Cédula*:")
        self.lblCedula.place(x=50, y=60)

        self.lblNombre = tk.Label(self.ventana, text="Nombre*:")
        self.lblNombre.place(x=50, y=90)

        self.lblApellido = tk.Label(self.ventana, text="Apellido*:")
        self.lblApellido.place(x=50, y=120)

        self.lblTelefono = tk.Label(self.ventana, text="Teléfono*:")
        self.lblTelefono.place(x=50, y=150)

        self.lblCorreo = tk.Label(self.ventana, text="Correo*:")
        self.lblCorreo.place(x=50, y=180)

        self.txtCedula = tk.Entry(self.ventana, width=25)
        self.txtCedula.place(x=130, y=60)
        Tooltip(self.txtCedula, "Ingrese su numero de cedula, sin espacios")

        self.txtNombre = tk.Entry(self.ventana, width=25)
        self.txtNombre.place(x=130, y=90)
        Tooltip(self.txtNombre, "Ingrese sus nombres, solo letras de a-z")

        self.txtApellido = tk.Entry(self.ventana, width=25)
        self.txtApellido.place(x=130, y=120)
        Tooltip(self.txtApellido, "Ingrese sus apellidos, solo letras de a-z")

        self.txtTelefono = tk.Entry(self.ventana, width=25)
        self.txtTelefono.place(x=130, y=150)
        Tooltip(self.txtTelefono, "Ingrese su numero de telefono,\n sin espacios, min 10 digitos")

        self.txtCorreo = tk.Entry(self.ventana, width=25)
        self.txtCorreo.place(x=130, y=180)
        Tooltip(self.txtCorreo, "Ingrese su correo electronico,\n puede usar caracteres especiales como: @, (.) y numeros")

        iconoAyuda = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=25, width=25,height=25)
        Tooltip(self.btnAyuda, "Presioname para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)
        
        iconoAgregar = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\user_add.png")
        self.btnAgregar = tk.Button(self.ventana, text="Agregar",  image=iconoAgregar, compound="left")
        self.btnAgregar.place(x=80, y=220)
        Tooltip(self.btnAgregar, "¡Clic para Agregar Cliente!")

        iconoLimpiar = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\textfield_delete.png")
        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar",  image=iconoLimpiar, compound="left")
        self.btnLimpiar.place(x=150, y=220)
        Tooltip(self.btnLimpiar, "¡Clic para Limpiar los Campos!")

        iconoSalir = tk.PhotoImage(file= r"Taller 3\Menu P.O.E\icons copy\cancel.png") 
        self.btnSalir = tk.Button(self.ventana, text="Salir",  image=iconoSalir, compound="left", command=self.salir1)
        self.btnSalir.place(x=220, y=220)
        Tooltip(self.btnSalir, "¡Clic para Salir!\nControl+s")
        self.ventana.bind("<Control-s>", self.salir1)

        self.ventana.mainloop()

