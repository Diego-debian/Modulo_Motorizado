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
    def Prueba1(self):
        bicho = Tk()
        bicho.geometry("810x500+0+0")
        bicho.config(bg="white")
        bicho.title("Interfaz Proyecto Propiedades, Prueba Motor y Rapidez")
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
            lblRapidez = Label(bicho, text="PRUEBA RAPIDEZ SIN PAUSA", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=30, y=180)
            btnVelo0= Button(bicho, text= "Detener", width=5, height=1, command= Vel_0).place(x=20, y=230)         
            btnVelo1= Button(bicho, text= "Rapidez 1", width=5, height=1, command= Vel_1).place(x=90, y=230)
            btnVelo2= Button(bicho, text= "Rapidez 2", width=5, height=1, command= Vel_2).place(x=160, y=230)
            btnVelo3= Button(bicho, text= "Rapidez 3", width=5, height=1, command= Vel_3).place(x=230, y=230)
            btnVelo4= Button(bicho, text= "Rapidez 4", width=5, height=1, command= Vel_4).place(x=300, y=230)
            btnVelo5= Button(bicho, text= "Rapidez 5", width=5, height=1, command= Vel_5).place(x=370, y=230)
   

        def Vel_0():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write('aa')
            print "\n El motor se encuentra detenido"            
            arduino.close()
            
            

        def Vel_1():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write('bb')
            print "\n El motor se encuentra en la velocidad 1"
            time.sleep(5)
            arduino.write('aa')
            print "\n El motor se encuentra detenido"            
            arduino.close()
            
            
            
        def Vel_2():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write('dd')
            print "EL motor esta a la velocidad 2"
            time.sleep(5)
            print "\n El motor se encuentra detenido"            
            arduino.write('aa') 
            arduino.close()
            
            
            
        def Vel_3():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write('ee')
            print "\n El motor se encuentra en la velocidad 3"
            time.sleep(5)
            arduino.write('aa')
            print "\n El motor se encuentra detenido"            
            arduino.close()
                      
            
        def Vel_4():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write('ff')
            print "\n El motor se encuentra en la velocidad 4"
            time.sleep(5)
            arduino.write('aa')
            arduino.close()

        def Vel_5():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write("gg")
            print "\n El motor se encuentra en la velocidad 5"
            time.sleep(5)
            arduino.write('aa')
            print "\n El motor se encuentra detenido"            
            arduino.close()
                   
      

        def Valido1():
            lblRapidez = Label(bicho, text="PRUEBA RAPIDEZ CON PAUSA", fg = ("red"), font = ("Century Schoolbook L",10)).place(x=30, y=300)
            btnVelo0= Button(bicho, text= "Detener", width=5, height=1, command= Velo_0).place(x=20, y=350)         
            btnVelo1= Button(bicho, text= "Rapidez 1", width=5, height=1, command= Velo_1).place(x=90, y=350)
            btnVelo2= Button(bicho, text= "Rapidez 2", width=5, height=1, command= Velo_2).place(x=160, y=350)
            btnVelo3= Button(bicho, text= "Rapidez 3", width=5, height=1, command= Velo_3).place(x=230, y=350)
            btnVelo4= Button(bicho, text= "Rapidez 4", width=5, height=1, command= Velo_4).place(x=300, y=350)
            btnVelo5= Button(bicho, text= "Rapidez 5", width=5, height=1, command= Velo_5).place(x=370, y=350)

        def Velo_0():
            arduino = serial.Serial(puerto.get(), 9600)
            arduino.write('aa')
            print "\n El motor se encuentra detenido"            
            arduino.close()
            
            

        def Velo_1():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                for i in range (0, 20):
                    arduino = serial.Serial(puerto.get(), 9600)
                    arduino.write('1')
                    time.sleep(0.0001)
                    arduino.close()
                    print "El motor avanzo ", i
                else:
                    arduino.close()

            except:
                print ("EL programa fallo")
                arduino.write('aa')
                arduino.close()
                Salir()
                
            
            
            
        def Velo_2():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                for i in range (0, 20):
                    arduino = serial.Serial(puerto.get(), 9600)
                    arduino.write('2')
                    time.sleep(0.0001)
                    arduino.close()
                    print "El motor avanzo ", i
                else:
                    arduino.close()

            except:
                print ("EL programa fallo")
                arduino.write('aa')
                arduino.close()
                Salir()
            
            
            
        def Velo_3():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                for i in range (0, 20):
                    arduino = serial.Serial(puerto.get(), 9600)
                    arduino.write('3')
                    time.sleep(0.0001)
                    arduino.close()
                    print "El motor avanzo ", i
                else:
                    arduino.close()

            except:
                print ("EL programa fallo")
                arduino.write('aa')
                arduino.close()
                Salir()

           
        def Velo_4():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                for i in range (0, 20):
                    arduino = serial.Serial(puerto.get(), 9600)
                    arduino.write('4')
                    time.sleep(0.0001)
                    arduino.close()
                    print "El motor avanzo ", i
                else:
                    arduino.close()

            except:
                print ("EL programa fallo")
                arduino.write('aa')
                arduino.close()
                Salir()   


        def Velo_5():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                for i in range (0, 20):
                    arduino = serial.Serial(puerto.get(), 9600)
                    arduino.write('5')
                    time.sleep(0.0001)
                    arduino.close()
                    print "El motor avanzo ", i
                else:
                    arduino.close()

            except:
                print ("EL programa fallo")
                arduino.write('aa')
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
        self.Prueba1()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")
        
        
        
modulo  = Gramo()
