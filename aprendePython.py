# este programa es para aprender python
from arreglos import *
monty = 23  # el perro es el que no hace nada
perro = 24

var = ("la wea fome de tu madre" + "es la que molesta mucho")

print(len(var))

perro2 = monty + perro + 1

print (perro2)

d = {'clave1':23,'clave2':34}

print (d)
cont = 0;
while True:
    cont +=1
    if cont == 5:
        print ('ya salimos')
        break
    else:
        print ('el contador va en: '+str(cont))

print ("Esto se imprime siempre")


for n in range(0,5):
    print(n)

def saludar():
    print("Hola")
    
saludar()

persona1 = persona("ian")
persona1.numeros()
