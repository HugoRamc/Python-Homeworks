#lo que heredan las clases van adentro del paréntesis
class persona(object):

    def __init__(self,nombre="persona"):
        self.nombre = nombre

    def numeros(self):
        num1 = input("Ingresa un numero para las operaciones: ")
        num2 = input("Ingresa otro numero para hacer mas operaciones: ")

        num1 = int(num1)
        num2 = int(num2)

        print(num1+num2)
        print(num1-num2)
        print(num1*num2)
        print(num1**num2)
        print(num1/num2)
        print(str(num1)+str(num2)+"la wea fomé")
