from Cliente import *

print("Bienvenido al banco")

nomCliente = input("Ingresa el nombre del cliente: ")

ncliente = cliente(nomCliente)
def menu():
    while True:
        print("Elige una opción: "+ncliente.nombre)
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
            print("Agregar Cuenta")
        elif opc == '4':
            print("obtener numCuenta")
        elif opc == '5':
            print("Salir")
            break
        else:
            print("Agrega una opción válida")
menu()





print("adiosis")
