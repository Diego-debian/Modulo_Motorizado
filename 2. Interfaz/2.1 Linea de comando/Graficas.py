#!/usr/bin/python
# -*- coding:utf-8 -*-

#importar modulos
import serial
import os
import subprocess
from math import *
import Gnuplot 
import time

#COMIENZA EL PROGRAMA
#clase termometro
class Termometro:
    def Presentacion(self):
        os.system("clear")
        os.system("rm datos.dat")
        print "\n \t GRAFICADOR PARA LA TEMPERATURA DE UN TERMOMETRO EN ARDUINO"
        print "   \t              DIEGO ALBERTO PARRA GARZON"
        print "   \t                 COLOMBIA, BOGOTA D.C"
        print " \n\n POR FAVOR ESPERE UNOS SEGUNDOS MIENTRAS EL PROGRAMA CARGA"
        time.sleep(5)
        self.puerto = raw_input('\n INGRESE LA UBICACION DONDE SE ENCUENTRA EL DISPOSITIVO:  ')
    def Test(self):
        try:
            arduino = serial.Serial(self.puerto, 9600)
            time.sleep(3)
            arduino.write('@')
            print "el dispositivo esta listo, se procede a tomar los datos y graicarlos \n"
        except:
            arduino.close()
            print('no se encontro ningun puerto')
            
    def Adquirir(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [0: 120000] ")
        gp("set yrange [0: 100] ")
        arduino=serial.Serial(self.puerto, 9600)
        for i in range(0, 1000):
            archi = open('datos.dat', 'a+')
            time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            archi.write( self.xo )
            archi.write(" \t ")
            archi.write( self.yo )
            archi.close()
            gp("plot 'datos.dat' with lines")
        
        else:
            gp("exit")
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
    
    def __init__(self):
        self.Presentacion()
        self.Test()
        self.Adquirir()
        self.__del__()

    def __del__(self):
        print "termino el programa"

termometro = Termometro()
            
     
