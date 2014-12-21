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
        
 
        def Saluda():
            tkMessageBox.showinfo("Saludo", message="<Interfaz gráfica del modulo motorizado para ilustrar propiedades de las ondas electromagnéticas.> \n Copyright (C) 2014  <Diego Alberto Parra Garzón> \n Este programa es software libre. Puede redistribuirlo y/o modificarlo bajo los términos de la Licencia Pública General de GNU según es publicada por la Free Software Foundation, Este programa se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA, incluso sin la garantía MERCANTIL implícita o sin garantizar la CONVENIENCIA PARA UN PROPÓSITO PARTICULAR. Véase la Licencia Pública General de GNU para más detalles.\n Debería haber recibido una copia de la Licencia Pública General junto con este programa. Si no ha sido así, escriba a la Free Software Foundation, Inc., en 675 Mass Ave, Cambridge, MA 02139, EEUU.\n Diegoestudianteud1@gmail.com")
            os.system("emacs ../../LICENSE")
        
        def Salir():
            exit()

        def Iniciar():
            print "hola"

# Botones con imagenes 
        imgBoton=PhotoImage(file="Image/cap5.gif")
        btnSaludar=Button(bicho, image=imgBoton, command=Saluda, height=150, width =300).place(x=480, y=10)
        imgBoton1=PhotoImage(file="Image/cap7.gif")
        btnSalir=Button(bicho, image=imgBoton1, command=Salir, height=100, width =240).place(x=20, y=380)
        imgBoton2=PhotoImage(file="Image/cap6.gif")
        btnIniciar=Button(bicho, image=imgBoton2, command = Iniciar, height=300, width =440).place(x=10,y=10)

# Escritos en el texto
        w = Label(bicho, text="| GNU public license ... |", fg = ("blue"), font=("Century Schoolbook L", 9)).place(x=480, y=165)
        w1 = Label (bicho, text="Modulo motorizado para ilustrar la difracción,\n atenuación   y absorción de ondas\n electromagnéticas en el espectro infrarrojo;\n  utilizando tecnologías libres y de bajo costo.", font = ("Century Schoolbook L", 11)).place(x=470, y= 300)
        w2 = Label (bicho, text ="Diego Alberto Parra Garzón", font = ("Century Schoolbook L", 11)).place(x=540, y= 400)
        w3 = Label (bicho, text = "UNIVERSIDAD DISTRITAL FRANCISCO JOSE DE CALDAS", font = ("Century Schoolbook L", 9)).place(x=440, y=430)
        w4 =Label (bicho, text = "COLOMBIA, BOGOTA D.C.", font = ("Century Schoolbook L",8)).place(x=570,y=460)
        w5 =Label (bicho, text = "| Iniciar ... |", fg = ("blue"), font = ("Century Schoolbook L",10)).place(x=10,y=315)
        bicho.mainloop()  
    
    
    

    def __init__(self):
        self.Grafica()
modulo  = Gramo()


