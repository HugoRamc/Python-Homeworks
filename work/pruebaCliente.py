from Cliente import *

print("Bienvenido al banco")
nom = input("Ingresa el nombre del cliente: ")


class pruebaCliente(object):


    def __init__(self,nom):
        print("Bienvenido al banco")

        self.nomCliente = nom
        self.ncliente = Cliente(nom)


    def menu(self):
        while True:
            print("Elige una opción: "+self.nomCliente)
            print("1.- Obtener información")
            print("2.- Obtener Cuenta")
            print("3.- Agregar Cuenta")
            print("4.- Obtener numero de cuentas")
            print("5.- Salir")
            opc = input()

            if opc == '1':
                print("obtenerInfo")
            elif opc == '2':
                print("obtener cuenta")
            elif opc == '3':
                self.agregarCuenta()
            elif opc == '4':
                print("obtener numCuenta")
            elif opc == '5':
                print("Salir")
                break
            else:
                print("Agrega una opción válida")

    def agregarCuenta(self):
        print("Elige el tipo de cuenta a agregar")
        print("1.- Cuenta normal")
        print("2.- Cuenta de Ahorros")
        print("3.- Cuenta de Cheques")

        opc = input()

        if opc == '1':
            chq = Cuenta(5000)
            self.ncliente.agregarCuenta(chq)
        elif opc== '2':
            chq = CuentaDeCheques(5000)
        elif opc == '3':
            chq = CuentaDeCheques(5000)
        else:
            print ("Ingresa una opción válida")


var = pruebaCliente(nom)
var.menu()
