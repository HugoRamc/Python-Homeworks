class Cuenta(object):

    def __init__(self,saldoInicial  =  500.0):
        self.saldo = saldoInicial

    def consultar(self):
        return float(cuenta)

    def depositar(self,monto=0.0):
        self.saldo = self.saldo + monto

    def retirar(self,monto):
        if self.saldo >= 0:
            self.saldo = self.saldo - float(monto)
        else:
            print ("No puedes retirar mas dinero")
