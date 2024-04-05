from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nombre, apellido, cedula, telefono, correo):
        super().__init__(nombre, apellido, cedula, telefono, correo)
        self.__listaCuentas = []

    def getListaCuentas(self):
        return self.__listaCuentas
    
    def setListaCuentas(self, nueva_lista):
        self.__listaCuentas = nueva_lista
    
    def getInfo(self):
        return [self.getNombre(), self.getApellido(), self.getCedula(), self.getTelefono(), self.getCorreo()]
    
    def agregar_cuenta(self, cuenta):
        self.__listaCuentas.append(cuenta)



  

       
