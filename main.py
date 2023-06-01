from coleccion import coleccion
import numpy as np


if __name__ == '__main__':
    cant = int(input("Ingrese la cantidad de empleados: "))
    manejador = coleccion(cant)
    manejador.lecArchivo()
    ##manejador.impr()
    o=1
    while o != 0:
        print("""
----MENU----
1_ Registrar horas
2_ Total de tarea
3_ Listar empleados necesitados de ayuda economica
4_ Listar sueldos
0_ Fin
""")
        o = int(input("Ingrese opcion: "))
        if o == 1:
            manejador.opcion1()
        elif o == 2:
            manejador.opcion2()
        elif o == 3:
            manejador.opcion3()
        elif o == 4:
            manejador.opcion4()
        elif o == 0:
            print("FIN...")
        else:
            print("Opcion no valida, intentalo otra vez...")
            
            