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
import Tkinter

class Gramo():
    def Atenua(self):
        bicho = Tk()
        bicho.geometry("810x500+0+0")
        bicho.config(bg="white")
        bicho.title("Interfaz Proyecto Propiedades, Atenuación")
        bicho.resizable(width=0, height=0)
      
        
        def Salir():
            exit()

        def Verifica():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                tkMessageBox.showinfo("Verificando", message= "Dispositivo Listo")
                arduino.write("@@")
                Valido()
                #time.sleep(1)
                
            except:
                tkMessageBox.showinfo("Verificando", message= "Dispositivo no encontrado")
                arduino = serial.Serial(puerto.get(), 9600)
                arduino.close()  
        
        def Valido():
            lblRapidez = Label(bicho, text="DIFRACCION", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=30, y=180)
            btnVelo0 = Button(bicho, text= "Velo_1", width=5, height=1, command= Velo_1).place(x=20, y=230)         

        def Velo_0():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write("aa")
            arduino.close()
         
        def Conteo1():
            arduino= serial.Serial(puerto.get(), 9600)
            for n in range (0, 93):
                time.sleep(2)
                arduino= serial.Serial(puerto.get(), 9600)
                os.system('rm Datos_C/dat1/datos_1.dat')
                print("aca va la pausa")
                arduino.write("aa")
                time.sleep(1)
                arduino.write('3')
                time.sleep(1.3)
                arduino.close()
                arduino=serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('zz')
                for i in range(0, 70):
                    arduino=serial.Serial(puerto.get(), 9600)
                    archi = open('Datos_C/dat1/datos_1.dat', 'a+')
                    time.sleep(0.000005)
                    x = arduino.readline()
                    z = 0.27*2*(185-n)
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
                # os.system("gnuplot  Datos_C/dat1/agraf.gnp &")
                os.system('rm Datos_C/dat1/datos_1.dat')  
                    
            else:
                os.system('sync')
                arduino.close()
                arduino.close()
               
        
        def Conteo2():
            arduino= serial.Serial(puerto.get(), 9600)
            for n in range (0, 82):
                time.sleep(2)
                arduino= serial.Serial(puerto.get(), 9600)
                os.system('rm Datos_C/dat1/datos_2.dat')
                print("aca va la pausa")
                arduino.write("aa")
                time.sleep(1)
                arduino.write('3')
                time.sleep(1.3)
                arduino.close()
                arduino=serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('zz')
                for i in range(0, 70):
                    arduino=serial.Serial(puerto.get(), 9600)
                    archi = open('Datos_C/dat1/datos_2.dat', 'a+')
                    time.sleep(0.000005)
                    x = arduino.readline()
                    z = 0.27*2*(92-n)
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
                archi = open('Datos_C/dat1/prom2.dat', 'a+')
                print "aca va la lectura"
                Lectura1 = archi.read()
                archi.close() 
                archi1 = open('Datos_C/dat1/datos1_.dat', 'a+')
                archi1.write(Lectura1)
                archi1.close()
                # os.system("gnuplot  Datos_C/dat1/agraf.gnp &")
                os.system('rm Datos_C/dat1/datos_2.dat')  
                    
            else:
                os.system('sync')
                arduino.close()
                arduino.close()

        def Velo_1():
            Conteo1()
            print "Esperando 1 minuto antes de continuar, disculpe las molestias"
            time.sleep(60)
            Conteo2()
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
            tkMessageBox.showinfo("Información ", message= "Los datos se encuentran en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Datos_C/dat1/datos1_.dat' y la grafica se encuentra en 'Modulo_Motorizado/2. Interfaz/2.2 Grafica/prograsecu/Prueba2/Image/agraf1.gif'")
            
        def LoL1():
            gp = Gnuplot.Gnuplot()
            gp("set title 'ESPACIO VS VOLTAJE'")
            gp("set xlabel 'Espacio en cm'") 
            gp("set ylabel 'Voltaje en milivoltios'")
            gp("set grid")
            gp("plot 'Datos_C/dat1/datos1_.dat' title ' ' ")
            gp("pause mouse")
            gp("set term png")
            gp("set output '../../Image/agraf1.png'")
            gp("replot")
            gp("pause mouse")
            os.system("rm '../../Image/agraf1.gif' ")
            os.system("convert  '../../Image/agraf1.png' '../../Image/agraf1.gif'  &")
            # time.sleep(2)
           # os.system("eog '../../Image/2agraf1.gif' &")
            print "funciono"


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
        self.Atenua()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")
        
        
        
modulo  = Gramo()
