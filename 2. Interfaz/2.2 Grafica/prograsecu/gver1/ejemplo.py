#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import os
import subprocess
import math
import time
import  Gnuplot

def Graficar():
    gp =Gnuplot.Gnuplot()
    for i in range (0, 1800):
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [0: 120000] ")
        gp("set yrange [0: 600] ")
        gp("plot 'datos.txt' with lines ")
        time.sleep(0.0001)
        gp("replot")
      # gp("exit")
    else:
        print"PROGRAMA FALLO"
        gp("exit")
        exit()
    

def Llamar():
    os.system("python ejemplo2.py &")
    time.sleep(2)
    Graficar()
    exit()

Llamar()

