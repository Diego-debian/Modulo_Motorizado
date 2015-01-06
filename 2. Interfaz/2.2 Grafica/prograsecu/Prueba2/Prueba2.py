#!/usr/bin/python
# -*- coding:utf-8 -*-

import serial
import os
import subprocess
import math
import time
import Gnuplot
from Tkinter import *
import tkMessageBox

class Gramo():
    def Prueba2(self):
        bicho = Tk()
        bicho.geometry("810x500+0+0")
        bicho.config(bg="white")
        bicho.title("Interfaz Proyecto Propiedades, Prueba intensidad sensor lateral")
        bicho.resizable(width=0, height=0)
  
        
        def Salir():
            exit()

        def Verifica():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                tkMessageBox.showinfo("Verificando", message= "Dispositivo Listo")
                arduino.write("@@")
               # time.sleep(1)
                Valido()
                Valido1()
            except:
                tkMessageBox.showinfo("Verificando", message= "Dispositivo no encontrado")
                arduino = serial.Serial(puerto.get(), 9600)
                arduino.close()  
        
        def Valido():
            lblRapidez = Label(bicho, text="PRUEBA DE INTENSIDAD CON RAPIDEZ SIN PAUSA", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=30, y=180)
            btnVelo0= Button(bicho, text= "Rapidez_0", width=5, height=1, command= Sen_Lat0).place(x=20, y=230)         
            btnVelo1= Button(bicho, text= "Rapidez_1", width=5, height=1, command= Sen_Lat1).place(x=90, y=230)
            btnVelo2= Button(bicho, text= "Rapidez_2", width=5, height=1, command= Sen_Lat2).place(x=160, y=230)
            btnVelo3= Button(bicho, text= "Rapidez_3", width=5, height=1, command= Sen_Lat3).place(x=230, y=230)
            btnVelo4= Button(bicho, text= "Rapidez_4", width=5, height=1, command= Sen_Lat4).place(x=300, y=230)
            btnVelo5= Button(bicho, text= "Rapidez_5", width=5, height=1, command= Sen_Lat5).place(x=370, y=230)
   

        def Sen_Lat0():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Tiempo en milesimas de segundos'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set xrange [-10: 80000] ")
            gp("set yrange [-10: 4000] ")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('hh')
            time.sleep(2)
            for i in range(0, 1000):
                archi = open('Datos/dat0/datos_0.dat', 'a+')
            #   time.sleep(0.00005)
                x = arduino.readline()
                z = int(i*60)
                xo = str(z)
                yo = str(x)
                print('{0} {1}').format(xo, yo)
                archi.write ("\t")
                archi.write (xo)
                archi.write ("\t")
                archi.write (yo)
                archi.close()
                gp("plot 'Datos/dat0/datos_0.dat' with lines")
            else:
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                
                
        def Sen_Lat1():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Tiempo en milesimas de segundos'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set xrange [-10: 80000] ")
            gp("set yrange [-10: 4000] ")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('ii')
            time.sleep(2)
            for i in range(0, 1000):
                archi = open('Datos/dat1/datos_1.dat', 'a+')
            #     time.sleep(0.00005)
                x = arduino.readline()
                z = int(i*60)
                xo = str(z)
                yo = str(x)
                print('{0} {1}').format(xo, yo)
                archi.write ("\t")
                archi.write (xo)
                archi.write ("\t")
                archi.write (yo)
                archi.close()
                gp("plot 'Datos/dat1/datos_1.dat' with lines ")
            else:
                gp("exit")
            #time.sleep(1)
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
        
                
        def Sen_Lat2():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Tiempo en milesimas de segundos'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set xrange [-10: 80000] ")
            gp("set yrange [-10: 4000] ")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('jj')
            time.sleep(2)
            for i in range(0, 1000):
                archi = open('Datos/dat2/datos_2.dat', 'a+')
            #        time.sleep(0.00005)
                x = arduino.readline()
                z = int(i*60)
                xo = str(z)
                yo = str(x)
                print('{0} {1}').format(xo, yo)
                archi.write ("\t")
                archi.write (xo)
                archi.write ("\t")
                archi.write (yo)
                archi.close()
                gp("plot 'Datos/dat2/datos_2.dat' with lines")
            else:
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                

        def Sen_Lat3():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Tiempo en milesimas de segundos'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set xrange [-10: 80000] ")
            gp("set yrange [-10: 4000] ")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('kk')
            time.sleep(2)
            for i in range(0, 1000):
                archi = open('Datos/dat3/datos_3.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = int(i*60)
                xo = str(z)
                yo = str(x)
                print('{0} {1}').format(xo, yo)
                archi.write ("\t")
                archi.write (xo)
                archi.write ("\t")
                archi.write (yo)
                archi.close()
                gp("plot 'Datos/dat3/datos_3.dat' with lines")
            else:
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
    

        def Sen_Lat4():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Tiempo en milesimas de segundos'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set xrange [-10: 80000] ")
            gp("set yrange [-10: 4000] ")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('ll')
            time.sleep(2)
            for i in range(0, 1000):
                archi = open('Datos/dat4/datos_4.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = int(i*60)
                xo = str(z)
                yo = str(x)
                print('{0} {1}').format(xo, yo)
                archi.write ("\t")
                archi.write (xo)
                archi.write ("\t")
                archi.write (yo)
                archi.close()
                gp("plot 'Datos/dat4/datos_4.dat' with lines")
            else:
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
        

        def Sen_Lat5():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Tiempo en milesimas de segundos'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set xrange [-10: 80000] ")
            gp("set yrange [-10: 4000] ")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('mm')
            for i in range(0, 1000):
                archi = open('Datos/dat5/datos_5.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = int(i*60)
                xo = str(z)
                yo = str(x)
                print('{0} {1}').format(xo, yo)
                archi.write ("\t")
                archi.write (xo)
                archi.write ("\t")
                archi.write (yo)
                archi.close()
                gp("plot 'Datos/dat5/datos_5.dat' with lines")
            else:
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                
                   
      


        def Valido1():
            lblRapidez = Label(bicho, text="PRUEBA DE INTENSIDAD,  RAPIDEZ CON PAUSA", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=30, y=300)
            btnVelo0= Button(bicho, text= "Rapidez 0", width=5, height=1, command= Velo_0).place(x=20, y=350)         
            btnVelo1= Button(bicho, text= "Rapidez 1", width=5, height=1, command= Velo_1).place(x=90, y=350)
            btnVelo2= Button(bicho, text= "Rapidez 2", width=5, height=1, command= Velo_2).place(x=160, y=350)
            btnVelo3= Button(bicho, text= "Rapidez 3", width=5, height=1, command= Velo_3).place(x=230, y=350)
            btnVelo4= Button(bicho, text= "Rapidez 4", width=5, height=1, command= Velo_4).place(x=300, y=350)
            btnVelo5= Button(bicho, text= "Rapidez 5", width=5, height=1, command= Velo_5).place(x=370, y=350)

        def Velo_0():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write("aa")
            arduino.close()
            
        
        def Res1():
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('hh')
            time.sleep(2)
            for i in range(0, 1000):
                archi = open('Datos/dat0/datos_0.dat', 'a+')
            #   time.sleep(0.00005)
                x = arduino.readline()
                z = int(i*60)
                xo = str(z)
                yo = str(x)
                print('{0} {1}').format(xo, yo)
                archi.write (xo)
                archi.write (" ")
                archi.write (yo)
                archi.close()
                
            else:
                
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                Velo_0()

        def Velo_1():
            arduino= serial.Serial(puerto.get(), 9600)
            for i in range (0, 1):
                print("aca va la pausa")
                arduino.write("bb")
                time.sleep(0.0001)
                Res1()
            
        def Velo_2():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                for i in range (0, 5):
                    arduino.write('dd')
                    time.sleep(0.0001)
                    arduino.write('hh')
                    print "todo salio bien"
                    time.sleep(5)
                    arduino.close()
                arduino = serial.Serial(puerto.get(), 9600)
                arduino.write('bb')
                print "\n El motor se encuentra en la velocidad 2"
                arduino.close()

            except:
                arduino.write('aa')
                print ("EL programa fallo")
                arduino.close()
                Salir()
            
            
            
        def Velo_3():
             try:
                arduino = serial.Serial(puerto.get(), 9600)
                for i in range (0, 5):
                    arduino.write('ee')
                    time.sleep(0.0001)
                    arduino.write('hh')
                    print "todo salio bien"
                    time.sleep(5)
                    arduino.close
                arduino = serial.Serial(puerto.get(), 9600)
                arduino.write('bb')
                print "\n El motor se encuentra en la velocidad 3"
                arduino.close()

             except:
                print ("EL programa fallo")
                arduino.write('aa')
                arduino.close()
                Salir()


        def Velo_4():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                for i in range (0, 5):
                    arduino.write('ff')
                    time.sleep(0.0001)
                    arduino.write('hh')
                    print "todo salio bien"
                    time.sleep(5)
                    arduino.close
                arduino = serial.Serial(puerto.get(), 9600)
                arduino.write('bb')
                print "\n El motor se encuentra en la velocidad 4"
                arduino.close()

            except:
                print ("EL programa fallo")
                arduino.write('aa')
                arduino.close()
                Salir()      


        def Velo_5():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                for i in range (0, 5):
                    arduino.write('gg')
                    time.sleep(0.0001)
                    arduino.write('hh')
                    print "todo salio bien"
                    time.sleep(5)
                    arduino.close
                arduino = serial.Serial(puerto.get(), 9600)
                arduino.write('bb')
                print "\n El motor se encuentra en la velocidad 5"
                arduino.close()

            except:
                arduino.write('aa')
                print ("EL programa fallo")
                arduino.close()
                Salir()


        def Menu():
            os.system("cd ../ && python Gverificar1.py &")
            exit()

# botones con imagenes

        
        imgBoton1=PhotoImage(file="../../Image/cap7.gif")
        btnSalir=Button(bicho, image=imgBoton1, command=Salir, height=50, width =130).place(x=5, y=435)
        imgBoton=PhotoImage(file="../../Image/cap1.gif")
        btnSaludar=Button(bicho, image=imgBoton, command=Menu, height=150, width =280).place(x=500, y=300)
       

#Escribir label
        puerto = StringVar()
        lblPuerto = Label(bicho, text="Ruta al dispositivo: ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=30, y=100)
        txtPuerto = Entry(bicho, textvariable = puerto, width=40).place(x=180, y= 100)
        lblMenu = Label(bicho, text=" -*- Volver al Menu -*- ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=500, y=460)


#Botones normales
        btnProbar= Button(bicho, text= "Verificar", width=5, height=1, command= Verifica).place(x=520, y=100)            
        bicho.mainloop()  


        




    
    def __init__(self):
        self.Prueba2()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")
        
        
        
modulo  = Gramo()
