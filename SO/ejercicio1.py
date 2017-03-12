#! /usr/bin/python
import sys,os

if __name__ == '__main__':
    cont = 0
    archivos = 0
    carpetas = 0
    if len(sys.argv) == 2:
        path = sys.argv[1]
        dirs = os.listdir(path)
        for file in dirs:
            cont =1;
            print file

            if os.path.isfile(file):
                archivos+=1
            else:
                carpetas+=1


        print ("El numero de archivos = "+str(archivos))
        print("El numero de carpetas = "+str(carpetas))

        if cont == 0:
            print("directorio no encontrado")
    else:
        print("Introduce un directorio")

def otraFunc():
    resultado = subprocess.check_output("ls -a",sysargv[1])
    otro = resultado.split("\n")
