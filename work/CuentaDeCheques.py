from Cuenta import *
class CuentaDeAhorros(Cuenta):
    def __init__(self,saldoInicial,sobregiro=0):
        self.saldo = saldoInicial
        self.montoSobregiro = sobregiro

    def retirar(monto=0):
        if self.saldo >= 0:
            self.saldo = self.saldo - monto
        else:
            self.montoSobregiro = self.montoSobregiro + monto

    def consultarDinero():
        dinero = self.consultar()
        print("La cuenta tiene de saldo: "+str(dinero))
        print("El dinero por sobregiro es: "+str(self.montoSobregiro))
