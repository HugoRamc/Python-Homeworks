from Cuenta import *
from CuentaDeCheques import *
from CuentaDeAhorros import *
class cliente(object):

    def __init__(self,nombre):
        self.nombre = nombre
        self.numCuentas = None
        self.cuentas = None

    def obtenerInfo(self):
        print("El nombre de cliente es: "+self.nombre)
        #for cont in self.Cuenta
        #    self.numCuentas = self.numCuentas + 1
        print("El numero de cuentas que tiene es: "+self.numCuentas)

    def obtenerCuenta():
        pass
