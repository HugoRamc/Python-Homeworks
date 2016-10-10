from Cuenta import *
class CuentaDeAhorros(Cuenta):

    def __init__(self,saldoInicial,tasaDeInteres=0.3):
        self.saldo
        self.tasaDeInteres = tasaDeInteres

    def consultarDinero(self,monto):
        print("El dinero que hay: "+self.saldo)
        self.saldo = float(self.saldo) * (1+self.tasaDeInteres)
        print("El dinero generado por los intereses es: "+self.saldo)
