#! /usr/bin/python3
import subprocess

def procesador():
	#cpuinfo
	flag=0;
	print("\nBienvenido monitor de recursos del procesador")
	print("Información del procesador")
	#leemos el archivo del procesador de información del procesador
	procesador = open("/proc/cpuinfo","r")
	for linea in procesador:
		flag+=1
		print(linea,end="")

		if flag==15:
			break

		#mpstat all
		#ejecutamos el comando que traiga la informacion de uso del procesador
	print("Informacion porcentaje de uso del procesador")
	uso = subprocess.check_output(["mpstat","-P","ALL"])
	

	#al ejecutar el comando el resultado lo separa por saltos de linea, esta parte es un pequeño automata para separar los saltos de linea 
	if True:
		cad=""
		#lista = []
		for cr in str(uso):
			var = ord(cr)
			if cr=="b" and flag==0:
				flag=1
				continue
			elif cr=="\\":
				flag = 2
			elif (cr == "n" and flag == 2):
				cad = cad.replace("usr","nucleo")
				#lista.append(cad)
				print(cad)
				cad = ""
				flag=1
				continue
			elif cr=="t" and flag==2:
				flag=3
				cad+=" "

			elif (var>=65 and var<=90) or (var>=97 and var<=122) or (var==46)or (var==32) or (var==58) or (var==37) or (var>=48 and var<=57) or (var == 164):
				cad+=cr
			else:
				flag = 1
				continue


def memoria():
	#meminfo
	print("\nBienvenido monitor de recursos de la memoria")
	flag = 0
	procesador = open("/proc/meminfo","r")
	for linea in procesador:
		flag+=1
		print(linea,end="")

		if flag==15:
			break




def HDD():
	print("\nBienvenido monitor de recursos del disco duro")
	#df -h
	proceso = subprocess.check_output(["df","-h"])
	flag = 0
	cad=""
	#lista = []
	for cr in str(proceso):
		var = ord(cr)
		if cr=="b" and flag==0:
			flag=1
			continue
		elif cr=="\\":
			flag = 2
		elif (cr == "n" and flag == 2):
			cad = cad.replace("Tamaxc3xb1o","Tamaño")
			#lista.append(cad)
			print(cad)
			cad = ""
			flag=1
			continue
		elif cr=="t" and flag==2:
			flag=3
			cad+=" "
		elif (var>=65 and var<=90) or (var>=97 and var<=122) or (var==46)or (var==32) or (var==58) or (var==37) or (var>=48 and var<=57) or (var == 164) or (var == 47):
			cad+=cr
			flag = 1
		else:
			flag=1
			continue




if __name__ == '__main__':
	while 1:
		#declaramos un menu para que el usuario pueda escoger 
		print("\nBienvenido al monitor de recursos");
		print("Selecciona una opcion")
		print("1.-Información del procesador")
		print("2.-Información de memoria")
		print("3.-Información del Disco Duro")
		print("4.-Salir");

		opc = input()

		if opc == "1":
			procesador()
		elif opc == "2":
			memoria()
		elif opc=="3":
			HDD()
		elif opc=="4":
			print("Adios")
			break
		else:
			print("Ingresa una opción válida")




#cpuinfo
#meminfo