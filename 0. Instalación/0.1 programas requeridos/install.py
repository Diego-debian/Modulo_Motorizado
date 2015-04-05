#! /usr/bin/python
#-*- coding:utf-8 -*-
from os import *
import os 
import subprocess
import time

class Instalacion:
    def Presentacion(self):
        os.system("clear")
        print '\n \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t --                                                      --'
        print '   \t --          Diego Alberto Parra Garzón                  --'
        print '   \t --            Colombia, Bogotá D.C.                    --'
        print '   \t --                                                      --'
        print '   \t --                INSTALACION                           --'
        print '   \t --                                                      --'
        print '   \t --    SE PROCEDE A INSTALAR LOS SIGUIENTES PAQUETES     --'
        print '   \t --     *gcc        *g++        *python tools            --'
        print '   \t --     *gnuplot    *emacs      *arduino                 --'
        print '   \t --     *fritzing   *octave     *latex                   --'
        print '   \t --     *evince     *dispositivos bluetooh               --'
        print '   \t --                                                      --'
        time.sleep(2)
        print '\n \t -- Por favor espere mientras carga el instalador  '
        for i in range (1 , 5):
            print '   \t -- Van ........' , i, "segundos" 
            time.sleep(1)
    
    def Debian(self):
        print ('Se procede a instalar')
        os.system("apt-get install  bluez* gcc g++ emacs gnuplot gnuplot-qt evince octave")
        os.system("apt-get install python-matplotlib python-numpy python-tk python-gnuplot python-serial python-visual* libgtkglextmm*  ")
        
        os.system("apt-get install kile texlive-latex-recommended texlive-latex-extra")      
        os.system("apt-get install arduino fritzing eog")
        os.system("arduino")

    def ubuntu(self):
        os.system("sudo apt-get install bluez* gcc g++ emacs gnuplot gnuplot-qt evince octave")
            
        os.system("sudo apt-get install python-matplotlib python-numpy python-tk python-gnuplot python-serial python-visual* libgtkglextmm*  ")
        
        os.system("sudo apt-get install kile texlive-latex-recommended texlive-latex-extra")
        os.system("sudo apt-get install arduino fritzing eog ")
        os.system("arduino")


    
    def Fedora(self):
         os.system("yum -y install bluez* gcc g++ emacs eog gnuplot gnuplot-qt evince octave")
         time.sleep(1)
         os.system("yum -y install python-matplotlib python-numpy python-tk python-gnuplot python-serial python-visual* libgtkglextmm*  ")
         time.sleep(1)
         os.system("yum -y install kile texlive-latex-recommended texlive-latex-extra")
         os.system("yum -y install arduino fritzing ")
         os.system("arduino")

    def menu_Secundario(self):
        os.system("clear")
        self.preguntar = raw_input("\n LA INSTALCION FINALIZO \n ¿DESEA REINICIAR EL EQUIPO s/n: ")
        if self.preguntar == 's':
            print 'El sistema se esta preparando para reiniciarse'
            time.sleep(5)
            os.system("reboot")

        elif self.preguntar == 'n':
            for i in range (0, 5):
                os.system("clear")
                print 'El programa se cerrara en: ' 
                print '\n cerrando en:  ',  5 - i , "segundos "
                time.sleep(1)
        else:
            print "usted escogio una opcion no valida"
            time.sleep(4)
            self.menu_Secundario()
    def Menu_Principal(self):
        os.system("clear") 
        print '\n \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t --                                                      --'
        print '   \t --          Diego Alberto Parra Garzón                  --'
        print '   \t --            Colombia, Bogotá D.C.                     --'
        print '   \t --                                                      --'
        print '   \t --                  OPCIONES                            --'
        print '   \t --                                                      --'
        print '   \t --  Elija una opción y oprima enter:                    --'
        print '   \t --    La instalación sera en :                          --'
        print '   \t --   * Debian y basadas en debian ----------------->  1 --'
        print '   \t --   * Basadas en ubuntu          ----------------->  2 --'
        print '   \t --   * Fedora  y derivados        .................>  3 --'
        print '   \t --   * No instalar y Salir        .................>  4 --'
        print '\n \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'
        print '   \t ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'

        time.sleep(2)
        self.pregunta = raw_input("escoja una opción:  ")
        
        if self.pregunta == '1':
            self.Debian()
            self.menu_Secundario()
        
        elif self.pregunta == '2':
            self.ubuntu() 
            self.menu_Secundario()

        elif self.pregunta == '3':
            self.Fedora()     
            self.menu_Secundario()
                       
        elif self.pregunta == '4':
            exit()
        
        else:
            os.system("clear")
            for i in range (10):
                print ("\n warning } \t opción no valida:")
                print ("\n el programa saldra en ---------"), 14 - i
                time.sleep(1)
                os.system("clear")
            exit()
    
    def __init__(self):
        self.Presentacion()
        self.Menu_Principal()
        self.__del__()
    def __del__(self):
        print "El programa termino" 

install = Instalacion()
