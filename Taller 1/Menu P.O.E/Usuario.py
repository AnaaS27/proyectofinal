class Usuario:
    def __init__(self, nombre, apellido, cedula, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
    
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getCedula(self):
        return self.cedula
    def getTelefono(self):
        return self.telefono
    def getCorreo(self):
        return self.correo
    
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setCedula(self, cedula):
        self.cedula = cedula
    def setTelefono(self, telefono):
        self.telefono = telefono
    def setCorreo(self, correo):
        self.correo = correo
    

    def cedula_oculta(self):
        cedula_oculta = '*' * (len(self.cedula) - 4) + self.cedula[-4:]
        return cedula_oculta

    def __str__(self):
        return f"Nombre: {self.nombre}\n Apellido: {self.apellido}\n Cédula: {self.cedula_oculta()}"


