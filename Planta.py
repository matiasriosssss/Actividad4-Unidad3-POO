from Empleado import Empleado
class Planta(Empleado):
    def __init__(self, Dni, nomb, dire, tel, suel, ant):
        super().__init__(Dni, nomb, dire, tel)
        self.__sueldoBasico = float(suel)
        self.__antiguedad = int(ant)
    def getSueldo(self):
        return self.__sueldoBasico + (self.__sueldoBasico / 100) * self.__antiguedad
    def getAnti(self):
        return self.__antiguedad
    def __str__(self):
        return super().__str__()
    def op4(self):
        print(f"Nombre: {super().getNom()} - Telefono: {super().getTel()} - Sueldo: {self.getSueldo()}")
    