from Empleado import Empleado
class Contratado(Empleado):
    def __init__(self, Dni, nomb, dire, tel, inicio, fin, cantH, valH):
        super().__init__(Dni, nomb, dire, tel)
        self.__inicio = inicio
        self.__fin = fin
        self.__cantHoras = int(cantH)
        self.__valorHoras = float(valH)
    def getInicio(self):
        return self.__inicio
    def getFin(self):
        return self.__fin   
    def getSueldo(self):
        return self.__cantHoras * self.__valorHoras
    def __str__(self):
        return super().__str__() 
    def sumarHoras(self, cant):
        self.__valorHoras += cant
        print("Horas sumadas...")
    def op4(self):
        print(f"Nombre: {super().getNom()} - Telefono: {super().getTel()} - Sueldo: {self.getSueldo()}")