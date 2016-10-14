from Cuenta import *
from CuentaDeCheques import *
from CuentaDeAhorros import *
class Cliente(object):

    def __init__(self,nombre):
        self.nombre = nombre
        self.numCuentas = None
        self.cuentas = None

    def obtenerInfo(self):
        print("El nombre de cliente es: "+self.nombre)
        print(self.cuentas)
        print("El numero de cuentas que tiene es: ")

    def obtenerCuenta(self,indice):
        print(lista[indice])

    def agregarCuenta(self,cnta):
        #self.cuentas.append(cnta)
        print("Cuenta agregada exitosamente")
