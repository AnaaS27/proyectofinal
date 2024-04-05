from Usuario import Usuario

class Corresponsal(Usuario):
    def __init__(self, nombre, apellido, cedula, telefono, correo, nombre_corresponsal, direccion):
        Usuario.__init__(self, nombre, apellido, cedula, telefono, correo)
        self.nombre_corresponsal = nombre_corresponsal
        self.direccion = direccion
        self.listaClientes = []
        self.listaCuentas = []

    


