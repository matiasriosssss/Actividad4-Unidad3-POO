from Empleado import Empleado
from Planta import Planta
from Contratado import Contratado
from Externo import Externo 
import csv
import numpy as np

class coleccion:
    
    def __init__(self, cantidad):
        self.__empleados = np.empty(cantidad, dtype=Empleado)
        self.__cantidad = cantidad
        self.__i = 0
        
    def agregar(self, nuevo):
        if self.__i == self.__cantidad:
            self.__cantidad +=1
            self.__empleados.resize(self.__cantidad)
        self.__empleados[self.__i] = nuevo
        self.__i+=1
    def getArre(self):
        return self.__empleados
        
    def lecArchivo(self):
        archivo1 = open('C:\\Users\\Laura\\Desktop\\mati facultad\\Segundo año\\Programación orientada a objetos\\UNIDAD 3\\Ejercicios unidad 3\\ACTIVIDAD 4\\planta.csv')
        reader = csv.reader(archivo1)
        next(reader)
        for fila in reader:
            nuevoObjeto = Planta(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            self.agregar(nuevoObjeto)
        archivo2 = open('contratados.csv')
        reader = csv.reader(archivo2)
        next(reader)
        for fila in reader:
            nuevoObjeto = Contratado(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
            self.agregar(nuevoObjeto)    
        archivo3 = open('externos.csv')
        reader = csv.reader(archivo3)
        next(reader)
        for fila in reader:
            nuevoObjeto = Externo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7], fila[8], fila[9])
            self.agregar(nuevoObjeto)
    
    def impr(self):
        for i in range(len(self.getArre())):
            print(self.getArre()[i])
    def opcion1(self):
        dni = input("Ingrese dni: ")
        newHoras = int(input("Ingrese la cantidad de horas a registrar: "))
        i = 0
        centinela = True
        while i < len(self.getArre()) and centinela:
            if self.getArre()[i].getDni() == dni:
                if isinstance(self.getArre()[i], Planta) or isinstance(self.getArre()[i], Externo):
                    print("Este empleado no trabaja por horas...")
                else:
                    self.getArre()[i].sumarHoras(newHoras)
                centinela = False
            i+=1
        if centinela:
            print("No se encontro el empleado buscado...")
    def opcion2(self):
        tar = input("Ingrese tarea: ")
        i = 0
        total = 0
        centinela = True
        for i in range(len(self.getArre())):
            if isinstance(self.getArre()[i], Externo):
                if self.getArre()[i].getTarea() == tar:
                    total += self.getArre()[i].getCostoObra()
                    centinela = False
            i+=1
        if centinela:
            print("No se encontro la tarea buscada...")
        else:
             print(f"El costo de las tareas de {tar} es: {total}")
    def opcion3(self):
        for i in range(len(self.getArre())):
            if isinstance(self.getArre()[i], Planta) or isinstance(self.getArre()[i], Contratado):
                if self.getArre()[i].getSueldo() < 150000:
                    print(self.getArre()[i])
    def opcion4(self):
        for i in range(len(self.getArre())):
            self.getArre()[i].op4()
            
    