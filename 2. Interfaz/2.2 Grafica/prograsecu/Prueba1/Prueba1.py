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
        bicho.title("Interfaz Proyecto Propiedades")
  
        
        def Salir():
            exit()

        def Verifica():
            try:
                arduino = serial.Serial(puerto.get(), 9600)
                tkMessageBox.showinfo("Verificando", message= "Dispositivo Listo")
                arduino.write('@')
            
            except:
                tkMessageBox.showinfo("Verificando", message= "Dispositivo no encontrado")
                arduino = serial.Serial(puerto.get(), 9600)
                arduino.close()  
           

            def Vel_0():
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('aa')
                print "\n El motor se encuentra detenido"
                arduino.close()
                time.sleep(2)
                

            def Vel_1():
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('bb')
                print "\n El motor se encuentra en la velocidad 1"
                arduino.close()
                time.sleep(2)
                

            def Vel_2():
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('cc')
                print "\n El motor se encuentra en la velocidad 2"
                arduino.close()
                time.sleep(2)
                
        
            def Vel_3():
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('dd')
                print "\n El motor se encuentra en la velocidad 3"
                arduino.close()
                time.sleep(2)
                

            def Vel_4():
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('ee')
                print "\n El motor se encuentra en la velocidad 4"
                arduino.close()
                time.sleep(2)
                

            def Vel_5():
                arduino = serial.Serial(puerto.get(), 9600)
                time.sleep(2)
                arduino.write('ff')
                print "\n El motor se encuentra en la velocidad 5"
                arduino.close()
                time.sleep(2)
        
      
  
# botones con imagenes

        
        imgBoton1=PhotoImage(file="../../Image/cap7.gif")
        btnSalir=Button(bicho, image=imgBoton1, command=Salir, height=50, width =130).place(x=5, y=435)


#Escribir label
        puerto = StringVar()
        lblPuerto = Label(bicho, text="Ruta al dispositivo: ", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=30, y=100)
        txtPuerto = Entry(bicho, textvariable = puerto, width=40).place(x=180, y= 100)

#Botones normales
        btnProbar= Button(bicho, text= "Verificar", width=5, height=1, command= Verifica).place(x=520, y=100)         
        
        bicho.mainloop()  




    
    def __init__(self):
        self.Prueba1()
        self.__del__()

    def __del__(self):
        print ("PROGRAMA TERMINADO")
        
        
        
modulo  = Gramo()
