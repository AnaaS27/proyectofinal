from Corresponsal import Corresponsal

class SerializadorCorresponsal():
    def __init__(self):
        self.__archivo = open("corresponsales.txt", "a")

    def getArchivo(self):
        return self.__archivo
    
    #Se utiliza cuando creo objetos
    def escribirArchivo(self, texto):
        self.__archivo = open("corresponsales.txt", "a")
        self.__archivo.write(texto)
        self.__archivo.close()

    #Se utiliza cuando modifico o elimino objetos
    def sobreEscribirArchivo(self, texto):
        self.__archivo = open("corresponsales.txt", "w")
        self.__archivo.write(texto)
        self.__archivo.close()

    #Se utiliza cuando inicia la aplicación 
    def leerArchivo(self):
        nombre = "" # i=0
        apellido = "" # i=1
        cedula = "" # i=2
        telefono = "" # i=3
        correo = "" # i=4
        nombre_corresponsal = "" # i=5
        direccion = "" # i=6
        listaCorresponsal = []
        i = 0
        self.__archivo = open("corresponsales.txt", "r")
        for linea in self.__archivo:
            if(i==0):
                nombre = linea.strip()
                i+=1
            elif(i==1):
                apellido = linea.strip()
                i+=1
            elif(i==2):
                cedula = linea.strip()
                i+=1
            elif(i==3):
                telefono = linea.strip()
                i+=1
            elif(i==4):
                correo = linea.strip()
                i+=1
            elif(i==5):
                nombre_corresponsal = linea.strip()
                i+=1
            else:
                direccion = linea.strip()
                i=0


                i=0 # Esto indica al lector que la siguiente linea es un nombre
                miCorresponsal = Corresponsal(nombre, apellido, cedula, telefono, correo, nombre_corresponsal,direccion)
                listaCorresponsal.append(miCorresponsal)
        self.__archivo.close()
        return listaCorresponsal