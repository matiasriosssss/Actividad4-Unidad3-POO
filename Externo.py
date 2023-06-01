from Empleado import Empleado
class Externo(Empleado):
    def __init__(self, Dni, nomb, dire, tel, tarea, inicio, fin, montoViatico, costoObra, seguro):
        super().__init__(Dni, nomb, dire, tel)
        self.__inicio = inicio
        self.__fin = fin
        self.__tarea = tarea
        self.__viatico = float(montoViatico)
        self.__costoObra = float(costoObra)
        self.__seguro = float(seguro)
        
    def getInicio(self):
        return self.__inicio
    def getFin(self):
        return self.__fin   
    def getTarea(self):
        return self.__tarea  
    def getCostoObra(self):
        return self.__costoObra 
    def getSueldo(self):
        return self.__costoObra - self.__viatico - self.__seguro  
    def __str__(self):
        print(self.getDni())
        return super().__str__() + " - Tarea: " + str(self.__tarea)
    def op4(self):
        print(f"Nombre: {super().getNom()} - Telefono: {super().getTel()} - Sueldo: {self.getSueldo()}")