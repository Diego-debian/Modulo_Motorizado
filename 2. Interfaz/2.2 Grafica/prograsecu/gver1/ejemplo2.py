#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import os
import subprocess
import math
import time
import  Gnuplot

def Prueba():
    try:
        arduino=serial.Serial('/dev/rfcomm0', 9600) 
        print"conexion exitosa"
    except:
        print "Termino programa"
        arduino.exit()

def Capturar():
    arduino=serial.Serial('/dev/rfcomm0', 9600)
    time.sleep(2)
    arduino.write("i")
    for i in range(0, 400):
        archi = open('datos.txt', 'a+')
        time.sleep(0.00001)
        x=arduino.readline()
        z= int(i*60)
        xo=str(z)
        yo=str(x)
        print('{0} {1}').format(xo, yo)
        archi.write(xo )
        archi.write(yo )
        archi.close()
        
    else:
        print "El ciclo termino"
        os.system('sync')
        arduino.write("a")
        arduino.exit()
        os.system('sync')

Prueba()
Capturar()
