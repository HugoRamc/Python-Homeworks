#! /usr/bin/python
import subprocess

if __name__ == '__main__':
    if len(sys.argv)==2:
        for i in range(254):
            if i == 0:
                print("")
            else:
                proceso = subprocess.check_call(["ping",("192.168.43"+str(i))])
    else:
        print("Ingresa una direccion ip");
