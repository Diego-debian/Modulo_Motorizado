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
        bicho.geometry("800x500+0+0")
        bicho.config(bg="white")
        bicho.title("Interfaz Proyecto Propiedades")
        imagen1=PhotoImage(file="Image/cap6.gif")
        lblImagen1=Label(bicho, image=imagen1).place(x=10,y=10)
        def Saluda():
            tkMessageBox.showinfo("Saludo", message="Hi")


        imgBoton=PhotoImage(file="Image/cap5.gif")
        btnSaludar=Button(bicho, image=imgBoton, command=Saluda, height=150, width =300).place(x=480, y=10)
        bicho.mainloop()  
    
    
    def __init__(self):
        self.Grafica()
modulo  = Gramo()


