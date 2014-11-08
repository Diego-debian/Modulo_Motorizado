#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import os
import subprocess
import math
import time
 
class Modulo:
    def Logo(self):
        os.system ("clear")
        print " =========================================================================="
        print " =========================================================================="
        print "\n \t    Modulo motorizado  para ilustrar la difracción, atenuación \n \t y absorción de ondas electromagnéticas en el espectro infrarrojo;\n \t      utilizando tecnologías libres y de bajo costo."
        print "\n \t \t  \t DIEGO ALBERTO PARRA GARZON "
        print "\t \t \t     COLOMBIA, BOGOTA D.C"
        print "\n =========================================================================="
        print " =========================================================================="

    def Bienvenida(self):
        self.Logo()
        print "\n \n Espere unos segundos mientras el programa carga"
        time.sleep(5)
        self.puerto = raw_input('\n INGRESE LA UBICACION DONDE SE ENCUENTRA EL DISPOSITIVO:   ')
        time.sleep(2)
    
    def Test(self):
        try:
            arduino = serial.Serial(self.puerto, 9600)
            time.sleep(3)
            arduino.write('@')
            print "el dispositivo esta listo."
            time.sleep(1)
        except:
            arduino = serial.Serial()
            arduino.close()
            print('Por favor verifique la ruta del dispositivo, porque no se encontro')
            time.sleep(3)
            self.Logo()
            self.puerto = raw_input('\n INGRESE LA UBICACION DONDE SE ENCUENTRA EL DISPOSITIVO:   ')
            self.Test()
            
            
    def Vel_0(self):
         arduino = serial.Serial(self.puerto, 9600)
         time.sleep(2)
         arduino.write('aa')
         print "\n El motor se encuentra detenido"
         arduino.close()
         time.sleep(2)
         self.Vel_Motor()

    def Vel_1(self):
        arduino = serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('bb')
        print "\n El motor se encuentra en la velocidad 1"
        arduino.close()
        time.sleep(2)
        self.Vel_Motor()

    def Vel_2(self):
        arduino = serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('cc')
        print "\n El motor se encuentra en la velocidad 2"
        arduino.close()
        time.sleep(2)
        self.Vel_Motor()
        
    def Vel_3(self):
        arduino = serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('dd')
        print "\n El motor se encuentra en la velocidad 3"
        arduino.close()
        time.sleep(2)
        self.Vel_Motor()

    def Vel_4(self):
        arduino = serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('ee')
        print "\n El motor se encuentra en la velocidad 4"
        arduino.close()
        time.sleep(2)
        self.Vel_Motor()

    def Vel_5(self):
        arduino = serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('ff')
        print "\n El motor se encuentra en la velocidad 5"
        arduino.close()
        time.sleep(2)
        self.Vel_Motor()


    def Vel_Motor(self):
        self.Logo()
        print "\n  ###################### MENU CONTROL VELOCIDAD MOTOR ##################### "
        print "\n  Detener motor                    ------>          0"
        print "  Primera velocidad                ------>          1"
        print "  Segunda velocidad                ------>          2"
        print "  Tercera velocidad                ------>          3"
        print "  Cuarta Velocidad                 ------>          4"
        print "  Quinta velocidad                 ------>          5"
        print "  VOLVER MENU PRINCIPAL            ------>          6"
        print "  SALIR DEL PROGRAMA               ------>          7"
        vel = input('\n DIGITA TU OPCION Y PULSA ENTER:    ')
        if vel == 0 :
            self.Vel_0()

        elif vel == 1 :
            self.Vel_1()      

        elif vel == 2 :
            self.Vel_2()

        elif vel == 3 :
            self.Vel_3()

        elif vel == 4 :
            self.Vel_4()

        elif vel == 5 :
            self.Vel_5()
        
        elif vel == 6:
            self.Menu_Principal()

        elif vel == 7:
            self.Salir()
        else :
            self.Vel_Motor()
    def Salir(self):
        exit()

    def Menu_Principal(self):
        self.Logo()
        print "\n \n ############################# MENU PRINCIPAL ############################"
        print "\n\n  Prueba velocidad motor            ------>           0"
        print "  Prueba sensor lateral             ------>           1"
        print "  Prueba sensor frontal             ------>           2"
        print "  Salir del Programa                ------>           3"
        opcion = input ("\n DIGITA TU OPCION Y PULSA ENTER:   ")
        if opcion == 0:
            self.Vel_Motor()

    def __init__(self):
        self.Bienvenida()
        self.Test()
        self.Menu_Principal()
        
    def __del__(self):
        print "el programa finalizo"
modulo = Modulo() 
