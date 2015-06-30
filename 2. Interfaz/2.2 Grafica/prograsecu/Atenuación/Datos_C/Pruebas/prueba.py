#!/usr/bin/python
# -*- coding:utf-8 -*-
#Creado por Diego Alberto Parra Garzón
#Bogotá - Colombia 
import os
import time 
import shutil

class Archivo():
    def c_Carpeta(self):
	self.Carpeta = str(time.asctime())
   	os.mkdir(self.Carpeta)
    	shutil.move("Datos_C/dat1/xy.dat",  self.Carpeta)
    	shutil.move("Datos_C/dat1/datos1_.dat",  self.Carpeta)
    	shutil.move("Datos_C/dat1/prom.dat",  self.Carpeta)
        shutil.move("Datos_C/dat1/conclusión.dat",  self.Carpeta)

    	#os.mkdir("Datos_C/dat1")
    def Limpiar(self):
	os.system("rm 	Datos_C/dat1/a.dat")
	os.system("rm Datos_C/dat1/A.dat")

    def Estadistica(self):
	os.system("octave Datos_C/estadistica.m")
#	LEYENDO ARCHIVO UNO
	archi1 = open('Datos_C/dat1/a.dat', 'a+')
	print 'leyendo archivo ...'
	self.a = archi1.read()
	archi1.close()
#	LEYENDO ARCHIVO DOS 
	archi2 = open('Datos_C/dat1/A.dat', 'a+')
        print 'leyendo archivo ...'
        self.A = float(archi2.read())
	self.relacion = -2/self.A
	archi2.close()
#	PORCENTAJE DE ERROR
	if self.relacion < 1:
	    error = (1 - self.relacion)*100
	    archi3 = open('Datos_C/dat1/conclusión.dat', 'a+') 
	    archi3.write("A = ")
	    A = str(self.A)
	    archi3.write(A)
	    archi3.write("\n")
	    archi3.write("a = ")
	    a = str(self.a)
	    archi3.write(a)
	    archi3.write("\n \n") 
	    archi3.write("El error en el exponente es de ")
	    err1 = str(error)
	    archi3.write(err1)
	    archi3.write(" %; el exponente es ")
	    archi3.write(A)
	    archi3.close()
	    print "El error en el exponente es de ", error , "%"
	    self.c_Carpeta()	
	    self.Limpiar()

        else:
	    error = (self.relacion - 1)*100
	    archi3 = open('Datos_C/dat1/conclusión.dat', 'a+') 
	    archi3.write("A = ")
	    A = str(self.A)
	    archi3.write(A)
	    archi3.write("\n")
	    archi3.write("a = ")
	    a = str(self.a)
	    archi3.write(a)
	    archi3.write("\n \n") 
	    archi3.write("El error en el exponente es de ")
	    err1 = str(error)
	    archi3.write(err1)
	    archi3.write(" %; el exponente es ")
	    archi3.write(A)
	    archi3.close()
	    print "El error en el exponente es de ", error , "%"
	    self.c_Carpeta()
	    self.Limpiar()

    def __init__(self):
	self.Estadistica()
	self.__del__()

    def __del__(self):	
	print ("PROGRAMA TERMINADO")

manejo = Archivo()
