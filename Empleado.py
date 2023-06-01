class Empleado():
    
    def __init__(self, Dni, nomb, dire, tel):
        self.__DNI = Dni
        self.__nombre = nomb
        self.__direccion = dire
        self.__telefono = tel     
    def __str__(self):
        return "Dni: " + self.__DNI + " - Nombre: " + self.__nombre + " - Direccion: " + self.__direccion
    def getDni(self):
        return self.__DNI
    def getNom (self):
        return self.__nombre  
    def getTel(self):
        return self.__telefono
    def getDire (self):
        return self.__direccion
    
        
    
    
    