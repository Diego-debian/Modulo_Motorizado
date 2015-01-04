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
    def Grafica(self):
        bicho = Tk()
        bicho.geometry("810x500+0+0")
        bicho.config(bg="white")
        bicho.title("Interfaz Proyecto Propiedades")
        bicho.resizable(width=0, height=0)


        def Salir():
            exit()

        def Inicio():
            os.system("cd ../ && python Gverificar.py &")
            exit()

        def Iniciar():
            print "hola"

        def Prueba1():
            os.system("cd Prueba1 && python Prueba1.py &")
            exit()

        def Prueba2():
            print "SALIO BIEN"

        def Prueba3():
            print "SALIO BIEN"
        def Difraccion():
            print "TODO SALIO BIEN"
        def Absorcion():
            print "TODO SALIO BIEN"
        def Atenuacion():
            print "TODO SALIO BIEN"


# Botones con imagenes
        imgBoton1=PhotoImage(file="../Image/cap7.gif")
        btnSalir=Button(bicho, image=imgBoton1, command=Salir, height=50, width =130).place(x=5, y=435)
        imgBoton2=PhotoImage(file="../Image/cap6.gif")
        btnIniciar=Button(bicho, image=imgBoton2, command = Iniciar, height=300, width =440).place(x=10,y=10)


#botones normales
        btnInicio=Button(bicho, text="Inicio", command=Inicio, height=1, width=5).place(x=700, y=70)
        btnPrueba1=Button(bicho, text="Prueba 1", command=Prueba1, height=1, width=5).place(x=700, y=120)
        btnPrueba2=Button(bicho, text="Prueba 2", command=Prueba2, height=1, width=5).place(x=700, y=150)
        btnPrueba3=Button(bicho, text="Prueba 3", command=Prueba3, height=1, width=5).place(x=700, y=180)
        btnDifraccion=Button(bicho, text="Difracción", command=Difraccion, height=1, width=5).place(x=700, y=240)
        btnAbsorcion=Button(bicho, text="Absorción", command=Absorcion, height=1, width=5).place(x=700, y=290)
        btnAtenuacion=Button(bicho, text="Atenuación", command=Atenuacion, height=1, width=6).place(x=700, y=340)
# Escritos en el texto
        w = Label(bicho, text="| Bienvenidos ... |", fg = ("blue"), font=("Century Schoolbook L", 18)).place(x=480, y=15)
        w1 = Label(bicho, text = "INICIO |------------------>", fg="red", font=("Century Schoolbook L", 12)).place(x=480, y=70)
        w2 = Label(bicho, text = "PRUEBAS |---------------->", fg="red", font=("Century Schoolbook L", 12)).place(x=480, y=150)
        w3 = Label(bicho, text = "DIFRACCION |----------->", fg="red", font=("Century Schoolbook L", 12)).place(x=480, y=240)
        w4 = Label(bicho, text = "ABSORCION |----------->", fg="red", font=("Century Schoolbook L", 12)).place(x=480, y=290)
        w5 = Label(bicho, text = "ATENUACION |----------->", fg="red", font=("Century Schoolbook L", 12)).place(x=480, y=340)
        bicho.mainloop()

    def __init__(self):
        self.Grafica()
    def __del__(self):
        print ("fin")

modulo = Gramo()
