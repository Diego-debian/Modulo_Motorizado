#!/usr/bin/python
# -*- coding:utf-8 -*-
#Programa creado por Diego ALberto Parra Garzon 
#Universidad Distrital Francisco Jose de Caldas
#Colombia, Bogota.

import serial
import os
import subprocess
import math
import time
import Gnuplot
from Tkinter import *
import tkMessageBox
import Tkinter

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
            rx = 0
            ry = 0
#------------------------------------------------Botones----------------------------------------------------------
            lblRapidez = Label(bicho, text="PRUEBA DE INTENSIDAD, RAPIDEZ SIN PAUSA", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=30, y=180-ry/2)
            btnVelo0= Button(bicho, text= "Rapidez_0", width=5, height=1, command= Sen_Lat0).place(x=20+rx, y=230+ry)         
            btnVelo1= Button(bicho, text= "Rapidez_1", width=5, height=1, command= Sen_Lat1).place(x=90+rx, y=230+ry)
            btnVelo2= Button(bicho, text= "Rapidez_2", width=5, height=1, command= Sen_Lat2).place(x=160+rx, y=230+ry)
            btnVelo3= Button(bicho, text= "Rapidez_3", width=5, height=1, command= Sen_Lat3).place(x=230+rx, y=230+ry)	
            btnVelo4= Button(bicho, text= "Rapidez_4", width=5, height=1, command= Sen_Lat4).place(x=300+rx, y=230+ry)
            btnVelo4= Button(bicho, text= "Reiniciar todo", width=10, height=1, command= Reiniciar).place(x=300+rx, y=440+ry)
            

#=========================================================REINICIAR TODO ====================================================       
        def Reiniciar():
            os.system("rm Datos/dat0/datos_0.dat")
            os.system("rm Datos/dat0/promRad.dat")
            os.system("rm Datos/dat1/datos_1.dat")
            os.system("rm Datos/dat2/datos_2.dat")
            os.system("rm Datos/dat2/promRad.dat")
            os.system("rm Datos/dat3/datos_3.dat")
            os.system("rm Datos/dat3/promRad.dat")
            os.system("rm Datos/dat4/datos_4.dat")
            os.system("rm Datos/dat4/promRad.dat")
            os.system("rm Datos_C/dat1/datos_1.dat Datos_C/dat1/datos1_.dat Datos_C/dat1/prom.dat")
            os.system("rm Datos_C/dat2/datos_2.dat Datos_C/dat2/datos2_.dat Datos_C/dat2/prom.dat")
            os.system("rm Datos_C/dat3/datos_3.dat Datos_C/dat3/datos3_.dat Datos_C/dat3/prom.dat")
            os.system("rm Datos_C/dat4/datos_4.dat Datos_C/dat4/datos4_.dat Datos_C/dat4/prom.dat")
            os.system("rm Datos_C/dat5/datos_5.dat Datos_C/dat5/datos5_.dat Datos_C/dat5/prom.dat")

#=============================================================Estadistica====================================================

        def Esta_0():
            os.system("rm Datos/estadistica0.m")
            archi = open('Datos/estadistica0.m', 'a+')
            archi.write("f = load ('Datos/dat0/datos_0.dat');")
            archi.write("\n")
            archi.write("Y = f(:,2)/1000; \n")
            archi.write("Yp = sum(Y) /200")
            archi.write("; \n")
            archi.write("save -ascii 'Datos/dat0/promRad.dat' Yp");
            archi.close()     
        
        def Esta_1():
            os.system("rm Datos/estadistica1.m")
            z = str(self.N1)
            archi = open('Datos/estadistica1.m', 'a+')
            archi.write("f = load ('Datos/dat1/datos_1.dat');")
            archi.write("\n")
            archi.write("Y = f(:,2)/1000; \n")
            archi.write("Yp = sum(Y) /")
            archi.write(z)
            archi.write("; \n")
            archi.write("save -ascii 'Datos/dat1/promRad.dat' Yp");
            archi.close()      

        def Esta_2():
            os.system("rm Datos/estadistica2.m")
            z = str(self.N2)
            archi = open('Datos/estadistica2.m', 'a+')
            archi.write("f = load ('Datos/dat2/datos_2.dat');")
            archi.write("\n")
            archi.write("Y = f(:,2)/1000; \n")
            archi.write("Yp = sum(Y) /")
            archi.write(z)
            archi.write("; \n")
            archi.write("save -ascii 'Datos/dat2/promRad.dat' Yp");
            archi.close() 

        def Esta_3():
            os.system("rm Datos/estadistica3.m")
            z = str(self.N3)
            archi = open('Datos/estadistica3.m', 'a+')
            archi.write("f = load ('Datos/dat3/datos_3.dat');")
            archi.write("\n")
            archi.write("Y = f(:,2)/1000; \n")
            archi.write("Yp = sum(Y) /")
            archi.write(z)
            archi.write("; \n")
            archi.write("save -ascii 'Datos/dat3/promRad.dat' Yp");
            archi.close() 

        def Esta_4():
            os.system("rm Datos/estadistica4.m")
            z = str(self.N4)
            archi = open('Datos/estadistica4.m', 'a+')
            archi.write("f = load ('Datos/dat4/datos_4.dat');")
            archi.write("\n")
            archi.write("Y = f(:,2)/1000; \n")
            archi.write("Yp = sum(Y) /")
            archi.write(z)
            archi.write("; \n")
            archi.write("save -ascii 'Datos/dat4/promRad.dat' Yp");
            archi.close() 

#=======================================================Pruebas en sensores sin pausa ==================================

        def Sen_Lat0():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Dato '") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set yrange[0:4000]")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('hh')
            time.sleep(2)
            self.t1 = float(time.time())
            for i in range(0, 200):
                archi = open('Datos/dat0/datos_0.dat', 'a+')
            #   time.sleep(0.00005)
                x = arduino.readline()
                z = int (i)
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
                self.t2 = float(time.time())
                self.tt = self.t2 -self.t1
                self.Cd = 200/self.tt
                self.t0 = float(self.tt/200)
                print "El tiempo total en la captura de datos fue",self.tt
                print "Se captura 1 dato cada" , self.t0 , "segundos"
                gp("plot 'Datos/dat0/datos_0.dat' with lines")
                gp("pause mouse")
                gp("set term png")
                gp("set output '../../prograsecu/Articulos/Montaje Modulo/img/graf10.png'")
                gp("replot")
                gp("pause mouse")
                os.system("rm '../../prograsecu/Articulos/Montaje Modulo/img/graf10.gif' ")
                os.system("convert  '../../prograsecu/Articulos/Montaje Modulo/img/graf10.png' '../../prograsecu/Articulos/Montaje Modulo/img/graf10.gif'  &")
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
            self.t0 = float(self.tt/200)
            #            self.N1 = (5/self.to)
            #            self.N2 = (5/self.to)
            #            self.N3 = (5/self.to)
            #            self.N4 = (5/self.to)
            #Rapidez sin pausa
            self.R1 = 0.0795
            self.R2 = 0.0965
            self.R3 = 0.1005
            self.R4 = 0.1180
            #Rapidez con pausa
            self.R5 = 0.45
            self.R6 = 0.35
            self.R7 = 0.27
            self.R8 = 0.309
            self.R9 = 0.37
            self.M1=float((0.3/self.R1))
            self.M2=float((0.3/self.R2))
            self.M3=float((0.3/self.R3))
            self.M4=float((0.3/self.R4))
            self.N1=int(self.M1/self.t0)
            self.N2=int(self.M2/self.t0)
            self.N3=int(self.M3/self.t0)
            self.N4=int(self.M4/self.t0)
            Esta_0()
            os.system("octave Datos/estadistica0.m")
            archi1 = open('Datos/dat0/promRad.dat',  'a+')
            self.Dat0 = archi1.read()
            archi1.close()

            print "El tiempo total en captura de datos es: ", self.tt, " Segundos"
            print "Se captura 1 dato cada" , self.t0 , "Segundos" 
            print "El ruido promedio en el diodo lateral es de: ", self.Dat0 , " Voltios "
                       
        def Sen_Lat1():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Distancia en metros'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set yrange[0:4000]")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('ii')
            time.sleep(2)
            for i in range(0, self.N1):
                archi = open('Datos/dat1/datos_1.dat', 'a+')
            #     time.sleep(0.00005)
                x = arduino.readline()
                z = float(self.R1*i*self.t0)
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
                gp("plot 'Datos/dat1/datos_1.dat' with lines")
                gp("pause mouse")
                gp("set term png")
                gp("set output '../../prograsecu/Articulos/Montaje Modulo/img/graf11.png'")
                gp("replot")
                gp("pause mouse")
                os.system("rm '../../prograsecu/Articulos/Montaje Modulo/img//graf11.gif' ")
                os.system("convert  '../../prograsecu/Articulos/Montaje Modulo/img/graf11.png' '../../prograsecu/Articulos/Montaje Modulo/img/graf11.gif'  &")
                gp("exit")
            #time.sleep(1)
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                Esta_1()
                os.system("octave Datos/estadistica1.m")
                archi1 = open('Datos/dat1/promRad.dat',  'a+')
                self.Dat1 = archi1.read()
                archi1.close()
                print "El tiempo total en captura de datos es: ", self.M1, " Segundos"
                print "el total de datos capturados fue: ", self.N1
                print "El ruido promedio en el diodo lateral es de: ", self.Dat1 , " Voltios "
       
                
        def Sen_Lat2():

            print "la falla esta aca pendejo"
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Distancia en metros'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set yrange[0:4000]")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('jj')
            time.sleep(2)
            for i in range(0,   self.N2):
                archi = open('Datos/dat2/datos_2.dat', 'a+')
            #        time.sleep(0.00005)
                x = arduino.readline()
                z = float(self.R2*i*self.t0)
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
                gp("plot 'Datos/dat2/datos_2.dat' with lines")
                gp("pause mouse")
                gp("set term png")
                gp("set output '../../prograsecu/Articulos/Montaje Modulo/img/graf12.png'")
                gp("replot")
                gp("pause mouse")
                os.system("rm '../../prograsecu/Articulos/Montaje Modulo/img/graf12.gif' ")
                os.system("convert  '../../prograsecu/Articulos/Montaje Modulo/img/graf12.png' '../../prograsecu/Articulos/Montaje Modulo/img/graf12.gif'  &")
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                Esta_2()
                os.system("octave Datos/estadistica2.m")
                archi1 = open('Datos/dat2/promRad.dat',  'a+')
                self.Dat2 = archi1.read()
                archi1.close()
                print "El tiempo total en captura de datos es: ", self.M2, " Segundos"
                print "el total de datos capturados fue: ", self.N2
                print "El ruido promedio en el diodo lateral es de: ", self.Dat2 , " Voltios "

                

        def Sen_Lat3():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Distancia en metros'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set yrange[0:4000]")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('kk')
            time.sleep(2)
            for i in range(0,   self.N3):
                archi = open('Datos/dat3/datos_3.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = float(self.R3*i*self.t0)
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
                gp("plot 'Datos/dat3/datos_3.dat' with lines")
                gp("pause mouse")
                gp("set term png")
                gp("set output '../../prograsecu/Articulos/Montaje Modulo/img/graf13.png'")
                gp("replot")
                gp("pause mouse")
                os.system("rm '../../prograsecu/Articulos/Montaje Modulo/img/graf13.gif' ")
                os.system("convert  '../../prograsecu/Articulos/Montaje Modulo/img/graf13.png' '../../prograsecu/Articulos/Montaje Modulo/img/graf13.gif'  &")
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                Esta_3()
                os.system("octave Datos/estadistica3.m")
                archi1 = open('Datos/dat3/promRad.dat',  'a+')
                self.Dat3 = archi1.read()
                archi1.close()
                print "El tiempo total en captura de datos es: ", self.M3, " Segundos"
                print "el total de datos capturados fue: ", self.N3
                print "El ruido promedio en el diodo lateral es de: ", self.Dat3, " Voltios "

        def Sen_Lat4():
            gp = Gnuplot.Gnuplot()
            gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
            gp("set xlabel 'Distancia en metros'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set yrange[0:4000]")
            arduino=serial.Serial(puerto.get(), 9600)
            time.sleep(2)
            arduino.write('ll')
            time.sleep(2)
            for i in range(0,   self.N4):
                archi = open('Datos/dat4/datos_4.dat', 'a+')
                time.sleep(0.00005)
                x = arduino.readline()
                z = float(self.R4*i*self.t0)
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
                gp("plot 'Datos/dat4/datos_4.dat' with lines")
                gp("pause mouse")
                gp("set term png")
                gp("set output '../../prograsecu/Articulos/Montaje Modulo/img/graf14.png'")
                gp("replot")
                gp("pause mouse")
                os.system("rm '../../prograsecu/Articulos/Montaje Modulo/img/graf14.gif' ")
                os.system("convert  '../../prograsecu/Articulos/Montaje Modulo/img/graf14.png' '../../prograsecu/Articulos/Montaje Modulo/img/graf14.gif'  &")
                gp("exit")
                arduino.write('aa')
                print "El ciclo termino"
                os.system('sync')
                arduino.close()
                arduino.close()
                Esta_4()
                os.system("octave Datos/estadistica4.m")
                archi1 = open('Datos/dat4/promRad.dat',  'a+')
                self.Dat4 = archi1.read()
                archi1.close()
                print "El tiempo total en captura de datos es: ", self.M4, " Segundos"
                print "el total de datos capturados fue: ", self.N4
                print "El ruido promedio en el diodo lateral es de: ", self.Dat4, " Voltios "

       

#===================================================================== Validando 1 ===================================================================

        def Valido1():
            lblRapidez = Label(bicho, text="PRUEBA DE INTENSIDAD,  RAPIDEZ CON PAUSA", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=30, y=300)
            btnVelo1= Button(bicho, text= "Rapidez 1", width=5, height=1, command= Velo_1).place(x=20, y=350)
            btnVelo2= Button(bicho, text= "Rapidez 2", width=5, height=1, command= Velo_2).place(x=90, y=350)
            btnVelo3= Button(bicho, text= "Rapidez 3", width=5, height=1, command= Velo_3).place(x=160, y=350)
            btnVelo4= Button(bicho, text= "Rapidez 4", width=5, height=1, command= Velo_4).place(x=230, y=350)
            btnVelo5= Button(bicho, text= "Rapidez 5", width=5, height=1, command= Velo_5).place(x=300, y=350)

             
#=========================================================Prueba sensor lateral con pausa ==============================================================
               
        
        def Velo_1():
            arduino= serial.Serial(puerto.get(), 9600)
            for n in range (0, 20):
                os.system('rm Datos_C/dat1/datos_1.dat')
                print("aca va la pausa")
                #arduino.write("bbbbb")
                #time.sleep(0.5)
                arduino.write("1")
                time.sleep(1)
                arduino=serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('hh')
                for i in range(0, 100):
                    arduino=serial.Serial(puerto.get(), 9600)
                    archi = open('Datos_C/dat1/datos_1.dat', 'a+')
                #   time.sleep(0.00005)
                    x = arduino.readline()
                    z = self.R5*n
                    xo = str(z)
                    yo = str(x)
                    print('{0} {1}').format(xo, yo)
                    archi.write (xo)
                    archi.write (" ")
                    archi.write (yo)
                    archi.close()
                    
             
                    
                else:
                    os.system("octave Datos_C/prom1.m")
                    arduino.write('hh')
                    # Res1_1(self)
                    arduino.write('aa')
                    print "El ciclo termino"
                    os.system('sync')
                archi = open('Datos_C/dat1/prom.dat', 'a+')
                print "aca va la lectura"
                Lectura = archi.read()
                archi.close() 
                archi1 = open('Datos_C/dat1/datos1_.dat', 'a+')
                archi1.write(Lectura)
                archi1.close()
                # os.system("gnuplot  Datos_C/dat1/graf.gnp &")
                os.system('rm Datos_C/dat1/datos_1.dat')    
                    
            else:
                os.system('sync')
                arduino.close()
                arduino.close()
                LoL()           
     
        def LoL():
            bicho1 = Toplevel(bicho)
            bicho1.title("Codigo Python")
            bicho1.geometry("400x228+850+0")
            bicho1.config(bg="white")
            bicho1.title("Distancia vs Voltaje promedio")
            bicho1.resizable(width=0, height=0)
            lblPuerto = Label(bicho1, text="Distancia | Voltaje ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=25, y=10)
            scrollbar = Scrollbar(bicho1)
            scrollbar.pack( side = RIGHT, fill=Y )
            archi1 = open('Datos_C/dat1/datos1_.dat', 'a+')
            lstLecturas = Listbox(bicho1, yscrollcommand = scrollbar.set, width=40)
            for linea in archi1.readlines():
                lstLecturas.insert(END, linea)
            archi1.close()
            lstLecturas.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = lstLecturas.yview )
            lstLecturas.place(x=10, y=50) 
            btnGraf= Button(bicho1, text= "Grafica", width=5, height=1, command= LoL1).place(x=180, y=15)            
            btnInfo= Button(bicho1, text= "Información", width=8, height=1, command= Msg1).place(x=250, y=15)            

        def Msg1():
            tkMessageBox.showinfo("Información ", message= "Los datos se encuentran en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Datos_C/dat1/datos1_.dat' y la grafica se encuentra en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Image/graf1.gif'")
            
        def LoL1():
            gp = Gnuplot.Gnuplot()
            gp("set title 'ESPACIO VS VOLTAJE'")
            gp("set xlabel 'Espacio en cm'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set grid")
            gp("plot 'Datos_C/dat1/datos1_.dat' title ' ' ")
            gp("pause mouse")
            gp("set term png")
            gp("set output '../../Image/graf1.png'")
            gp("replot")
            gp("pause mouse")
            os.system("rm '../../Image/graf1.gif' ")
            os.system("convert  '../../Image/graf1.png' '../../Image/graf1.gif'  &")
            # time.sleep(2)
           # os.system("eog '../../Image/2graf1.gif' &")
            print "funciono"




        def Velo_2():
            arduino= serial.Serial(puerto.get(), 9600)
            for n in range (0, 20):
                os.system('rm Datos_C/dat2/datos_2.dat')
                print("aca va la pausa")
                arduino.write("1")
                time.sleep(1)
                arduino=serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('hh')
                for i in range(0, 100):
                    arduino=serial.Serial(puerto.get(), 9600)
                    archi = open('Datos_C/dat2/datos_2.dat', 'a+')
                #   time.sleep(0.00005)
                    x = arduino.readline()
                    z = self.R6*n
                    xo = str(z)
                    yo = str(x)
                    print('{0} {1}').format(xo, yo)
                    archi.write (xo)
                    archi.write (" ")
                    archi.write (yo)
                    archi.close()
                    
             
                    
                else:
                    os.system("octave Datos_C/prom2.m")
                    arduino.write('hh')
                    # Res1_1(self)
                    arduino.write('aa')
                    print "El ciclo termino"
                    os.system('sync')
                archi = open('Datos_C/dat2/prom.dat', 'a+')
                print "aca va la lectura"
                Lectura = archi.read()
                archi.close() 
                archi1 = open('Datos_C/dat2/datos2_.dat', 'a+')
                archi1.write(Lectura)
                archi1.close()
                # os.system("gnuplot  Datos_C/dat2/graf2.gnp &")
                os.system('rm Datos_C/dat2/datos_2.dat')    
                    
            else:
                os.system('sync')
                arduino.close()
                arduino.close()
                LoL2()           
     
        def LoL2():
            bicho1 = Toplevel(bicho)
            bicho1.title("Codigo Python")
            bicho1.geometry("400x228+850+0")
            bicho1.config(bg="white")
            bicho1.title("Distancia vs Voltaje promedio")
            bicho1.resizable(width=0, height=0)
            lblPuerto = Label(bicho1, text="Distancia | Voltaje ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=25, y=10)
            scrollbar = Scrollbar(bicho1)
            scrollbar.pack( side = RIGHT, fill=Y )
            archi1 = open('Datos_C/dat2/datos2_.dat', 'a+')
            lstLecturas = Listbox(bicho1, yscrollcommand = scrollbar.set, width=40)
            for linea in archi1.readlines():
                lstLecturas.insert(END, linea)
            archi1.close()
            lstLecturas.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = lstLecturas.yview )
            lstLecturas.place(x=10, y=50) 
            btnGraf= Button(bicho1, text= "Grafica", width=5, height=1, command= LoL3).place(x=180, y=15)            
            btnInfo= Button(bicho1, text= "Información", width=8, height=1, command= Msg2).place(x=250, y=15)            

        def Msg2():
            tkMessageBox.showinfo("Información ", message= "Los datos se encuentran en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Datos_C/dat2/datos2_.dat' y la grafica se encuentra en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Image/graf2.gif'")
            
        def LoL3():
            gp = Gnuplot.Gnuplot()
            gp("set title 'ESPACIO VS VOLTAJE'")
            gp("set xlabel 'Espacio en cm'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set grid")
            gp("plot 'Datos_C/dat2/datos2_.dat' title ' ' ")
            gp("pause mouse")
            gp("set term png")
            gp("set output '../../Image/graf2.png'")
            gp("replot")
            gp("pause mouse")
            os.system("rm '../../Image/graf2.gif' ")
            os.system("convert  '../../Image/graf2.png' '../../Image/graf2.gif'  &")
            # time.sleep(2)
           # os.system("eog '../../Image/2graf2.gif' &")
            print "funciono"



        def Velo_3():
            arduino= serial.Serial(puerto.get(), 9600)
            for n in range (0, 20):
                os.system('rm Datos_C/dat3/datos_3.dat')
                print("aca va la pausa")
                #arduino.write("ee")
                #time.sleep(0.4)
                arduino.write("1")
                time.sleep(1)
                arduino=serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('hh')
                for i in range(0, 100):
                    arduino=serial.Serial(puerto.get(), 9600)
                    archi = open('Datos_C/dat3/datos_3.dat', 'a+')
                #   time.sleep(0.00005)
                    x = arduino.readline()
                    z = self.R7*n
                    xo = str(z)
                    yo = str(x)
                    print('{0} {1}').format(xo, yo)
                    archi.write (xo)
                    archi.write (" ")
                    archi.write (yo)
                    archi.close()
                    
             
                    
                else:
                    os.system("octave Datos_C/prom3.m")
                    arduino.write('hh')
                    # Res1_1(self)
                    arduino.write('aa')
                    print "El ciclo termino"
                    os.system('sync')
                archi = open('Datos_C/dat3/prom.dat', 'a+')
                print "aca va la lectura"
                Lectura = archi.read()
                archi.close() 
                archi1 = open('Datos_C/dat3/datos3_.dat', 'a+')
                archi1.write(Lectura)
                archi1.close()
                # os.system("gnuplot  Datos_C/dat3/graf3.gnp &")
                os.system('rm Datos_C/dat3/datos_3.dat')    
                    
            else:
                os.system('sync')
                arduino.close()
                arduino.close()
                LoL4()           
     
        def LoL4():
            bicho1 = Toplevel(bicho)
            bicho1.title("Codigo Python")
            bicho1.geometry("400x228+850+0")
            bicho1.config(bg="white")
            bicho1.title("Distancia vs Voltaje promedio")
            bicho1.resizable(width=0, height=0)
            lblPuerto = Label(bicho1, text="Distancia | Voltaje ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=25, y=10)
            scrollbar = Scrollbar(bicho1)
            scrollbar.pack( side = RIGHT, fill=Y )
            archi1 = open('Datos_C/dat3/datos3_.dat', 'a+')
            lstLecturas = Listbox(bicho1, yscrollcommand = scrollbar.set, width=40)
            for linea in archi1.readlines():
                lstLecturas.insert(END, linea)
            archi1.close()
            lstLecturas.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = lstLecturas.yview )
            lstLecturas.place(x=10, y=50) 
            btnGraf= Button(bicho1, text= "Grafica", width=5, height=1, command= LoL5).place(x=180, y=15)            
            btnInfo= Button(bicho1, text= "Información", width=8, height=1, command= Msg3).place(x=250, y=15)            

        def Msg3():
            tkMessageBox.showinfo("Información ", message= "Los datos se encuentran en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Datos_C/dat3/datos3_.dat' y la grafica se encuentra en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Image/graf3.gif'")
            
        def LoL5():
            gp = Gnuplot.Gnuplot()
            gp("set title 'ESPACIO VS VOLTAJE'")
            gp("set xlabel 'Espacio en cm'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set grid")
            gp("plot 'Datos_C/dat3/datos3_.dat' title ' '")
            gp("pause mouse")
            gp("set term png")
            gp("set output '../../Image/graf3.png'")
            gp("replot")
            gp("pause mouse")
            os.system("rm '../../Image/graf3.gif' ")
            os.system("convert  '../../Image/graf3.png' '../../Image/graf3.gif'  &")
            # time.sleep(2)
           # os.system("eog '../../Image/2graf3.gif' &")
            print "funciono" 
    
        def Velo_4():
            arduino= serial.Serial(puerto.get(), 9600)
            for n in range (0, 20):
                os.system('rm Datos_C/dat4/datos_4.dat')
                print("aca va la pausa")
                #arduino.write("ff")
                #time.sleep(0.4)
                arduino.write("1")
                time.sleep(1)
                arduino=serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('hh')
                for i in range(0, 50):
                    arduino=serial.Serial(puerto.get(), 9600)
                    archi = open('Datos_C/dat4/datos_4.dat', 'a+')
                #   time.sleep(0.00005)
                    x = arduino.readline()
                    z = self.R8*n
                    xo = str(z)
                    yo = str(x)
                    print('{0} {1}').format(xo, yo)
                    archi.write (xo)
                    archi.write (" ")
                    archi.write (yo)
                    archi.close()
                    
             
                    
                else:
                    os.system("octave Datos_C/prom4.m")
                    arduino.write('hh')
                    # Res1_1(self)
                    arduino.write('aa')
                    print "El ciclo termino"
                    os.system('sync')
                archi = open('Datos_C/dat4/prom.dat', 'a+')
                print "aca va la lectura"
                Lectura = archi.read()
                archi.close() 
                archi1 = open('Datos_C/dat4/datos4_.dat', 'a+')
                archi1.write(Lectura)
                archi1.close()
                # os.system("gnuplot  Datos_C/dat4/graf4.gnp &")
                os.system('rm Datos_C/dat4/datos_4.dat')    
                    
            else:
                os.system('sync')
                arduino.close()
                arduino.close()
                LoL6()           
     
        def LoL6():
            bicho1 = Toplevel(bicho)
            bicho1.title("Codigo Python")
            bicho1.geometry("400x228+850+0")
            bicho1.config(bg="white")
            bicho1.title("Distancia vs Voltaje promedio")
            bicho1.resizable(width=0, height=0)
            lblPuerto = Label(bicho1, text="Distancia | Voltaje ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=25, y=10)
            scrollbar = Scrollbar(bicho1)
            scrollbar.pack( side = RIGHT, fill=Y )
            archi1 = open('Datos_C/dat4/datos4_.dat', 'a+')
            lstLecturas = Listbox(bicho1, yscrollcommand = scrollbar.set, width=40)
            for linea in archi1.readlines():
                lstLecturas.insert(END, linea)
            archi1.close()
            lstLecturas.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = lstLecturas.yview )
            lstLecturas.place(x=10, y=50) 
            btnGraf= Button(bicho1, text= "Grafica", width=5, height=1, command= LoL7).place(x=180, y=15)            
            btnInfo= Button(bicho1, text= "Información", width=8, height=1, command= Msg4).place(x=250, y=15)            

        def Msg4():
            tkMessageBox.showinfo("Información ", message= "Los datos se encuentran en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Datos_C/dat4/datos4_.dat' y la grafica se encuentra en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Image/graf4.gif'")
            
        def LoL7():
            gp = Gnuplot.Gnuplot()
            gp("set title 'ESPACIO VS VOLTAJE'")
            gp("set xlabel 'Espacio en cm'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set grid")
            gp("plot 'Datos_C/dat4/datos4_.dat' title ' ' ")
            gp("pause mouse")
            gp("set term png")
            gp("set output '../../Image/graf4.png'")
            gp("replot")
            gp("pause mouse")
            os.system("rm '../../Image/graf4.gif' ")
            os.system("convert  '../../Image/graf4.png' '../../Image/graf4.gif'  &")
            # time.sleep(2)
           # os.system("eog '../../Image/graf4.gif' &")
            print "funciono"




        def Velo_5():
            arduino= serial.Serial(puerto.get(), 9600)
            for n in range (0, 20):
                os.system('rm Datos_C/dat5/datos_5.dat')
                print("aca va la pausa")
                #arduino.write("gg")
                time.sleep(1)
                arduino.write("1")
                time.sleep(1)
                arduino=serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('hh')
                for i in range(0, 100):
                    arduino=serial.Serial(puerto.get(), 9600)
                    archi = open('Datos_C/dat5/datos_5.dat', 'a+')
                #   time.sleep(0.00005)
                    x = arduino.readline()
                    z = self.R9*n
                    xo = str(z)
                    yo = str(x)
                    print('{0} {1}').format(xo, yo)
                    archi.write (xo)
                    archi.write (" ")
                    archi.write (yo)
                    archi.close()
                    
             
                    
                else:
                    os.system("octave Datos_C/prom5.m")
                    arduino.write('hh')
                    # Res1_1(self)
                    arduino.write('aa')
                    print "El ciclo termino"
                    os.system('sync')
                archi = open('Datos_C/dat5/prom.dat', 'a+')
                print "aca va la lectura"
                Lectura = archi.read()
                archi.close() 
                archi1 = open('Datos_C/dat5/datos5_.dat', 'a+')
                archi1.write(Lectura)
                archi1.close()
                # os.system("gnuplot  Datos_C/dat5/graf5.gnp &")
                os.system('rm Datos_C/dat5/datos_5.dat')    
                    
            else:
                os.system('sync')
                arduino.close()
                arduino.close()
                LoL8()           
     
        def LoL8():
            bicho1 = Toplevel(bicho)
            bicho1.title("Codigo Python")
            bicho1.geometry("400x228+850+0")
            bicho1.config(bg="white")
            bicho1.title("Distancia vs Voltaje promedio")
            bicho1.resizable(width=0, height=0)
            lblPuerto = Label(bicho1, text="Distancia | Voltaje ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=25, y=10)
            scrollbar = Scrollbar(bicho1)
            scrollbar.pack( side = RIGHT, fill=Y )
            archi1 = open('Datos_C/dat5/datos5_.dat', 'a+')
            lstLecturas = Listbox(bicho1, yscrollcommand = scrollbar.set, width=40)
            for linea in archi1.readlines():
                lstLecturas.insert(END, linea)
            archi1.close()
            lstLecturas.pack( side = LEFT, fill = BOTH )
            scrollbar.config( command = lstLecturas.yview )
            lstLecturas.place(x=10, y=50) 
            btnGraf= Button(bicho1, text= "Grafica", width=5, height=1, command= LoL9).place(x=180, y=15)            
            btnInfo= Button(bicho1, text= "Información", width=8, height=1, command= Msg5).place(x=250, y=15)            

        def Msg5():
            tkMessageBox.showinfo("Información ", message= "Los datos se encuentran en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Datos_C/dat5/datos5_.dat' y la grafica se encuentra en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Image/graf5.gif'")
            
        def LoL9():
            gp = Gnuplot.Gnuplot()
            gp("set title 'ESPACIO VS VOLTAJE'")
            gp("set xlabel 'Espacio en cm'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set grid")
            gp("plot 'Datos_C/dat5/datos5_.dat' title ' ' ")
            gp("pause mouse")
            gp("set term png")
            gp("set output '../../Image/graf5.png'")
            gp("replot")
            gp("pause mouse")
            os.system("rm '../../Image/graf5.gif' ")
            os.system("convert  '../../Image/graf5.png' '../../Image/graf5.gif'  &")
            # time.sleep(2)
           # os.system("eog '../../Image/2graf5.gif' &")
            print "funciono"


#====================================================MENU==============================================================


#Volver al menu
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
