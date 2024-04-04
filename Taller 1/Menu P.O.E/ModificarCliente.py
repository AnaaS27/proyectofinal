import tkinter as tk
from tkinter import messagebox
from Tooltip import Tooltip

class ModificarCliente():

    def salir2(self, event=None):
        respuesta = messagebox.askquestion("Confirmación", "¿Está seguro de salir?")
        if respuesta == "yes":
            self.ventana.destroy()

    def mostrarAyuda(self, event):
        ayuda_texto = "Bienvenido al formulario de modificación de cliente.\nPor favor modifique los campos requeridos."
        messagebox.showinfo("Ayuda", ayuda_texto)

    def __init__(self, menu, corresponsal, cliente):
        self.ventana = tk.Toplevel(menu)
        self.ventana.title("Gestionar Clientes")
        self.ventana.resizable(0,0)
        self.ventana.config(width=350, height=300)
        
        self.corresponsal = corresponsal
        self.cliente = cliente
        
        self.lblTitulo = tk.Label(self.ventana, text="Modificar Cliente")
        self.lblTitulo.place(relx=0.5, y=40, anchor="center")

        iconoAyuda = tk.PhotoImage(file= r"Menu P.O.E\icons\help.png")
        self.btnAyuda = tk.Button(self.ventana, image=iconoAyuda)
        self.btnAyuda.place(relx=1, x=-45, y=25, width=25,height=25)
        Tooltip(self.btnAyuda, "Presioname para obtener ayuda!\nAlt+a")
        self.btnAyuda.bind("<Button-1>", self.mostrarAyuda)
        self.ventana.bind('<Alt-a>', self.mostrarAyuda)

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

        self.txtCedula = tk.Entry(self.ventana, width=25, state="disabled")
        self.txtCedula.place(x=130, y=60)
        
        self.txtNombre = tk.Entry(self.ventana, width=25, state="disabled")
        self.txtNombre.place(x=130, y=90)
        
        self.txtApellido = tk.Entry(self.ventana, width=25, state="disabled")
        self.txtApellido.place(x=130, y=120)
        
        self.txtTelefono = tk.Entry(self.ventana, width=25, state="disabled")
        self.txtTelefono.place(x=130, y=150)
        
        self.txtCorreo = tk.Entry(self.ventana, width=25, state="disabled")
        self.txtCorreo.place(x=130, y=180)

        iconoBuscar = tk.PhotoImage(file= r"Menu P.O.E\icons\magnifier.png")
        self.btnBuscar = tk.Button(self.ventana, image=iconoBuscar)
        self.btnBuscar.place(x=285, y=60, width=25,height=20)
        Tooltip(self.btnBuscar, "¡Clic para Buscar!")

        self.btnGuardar = tk.Button(self.ventana, text="Guardar")
        self.btnGuardar.place(x=80, y=220)
        Tooltip(self.btnGuardar, "¡Clic para Guardar Cambios!")

        self.btnLimpiar = tk.Button(self.ventana, text="Limpiar")
        self.btnLimpiar.place(x=150, y=220)
        Tooltip(self.btnLimpiar, "¡Clic para Limpiar los Campos!")

        self.btnSalir = tk.Button(self.ventana, text="Salir", command=self.salir2)
        self.btnSalir.place(x=220, y=220)
        Tooltip(self.btnSalir, "¡Clic para Salir!\nControl+s")
        self.ventana.bind("<Control-s>", self.salir2)

        self.ventana.mainloop()