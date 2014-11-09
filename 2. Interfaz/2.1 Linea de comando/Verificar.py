#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import os
import subprocess
import math
import time
import  Gnuplot

class Modulo:
    def Logo(self):
        os.system("mkdir datos_sensor_lateral")
        os.system("mkdir datos_sensor_frontal")
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
    
    def Sen_Lat0(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('gg')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_lateral/datos_0.dat', 'a+')
         #   time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_lateral/datos_0.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Lat1(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('hh')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_lateral/datos_1.dat', 'a+')
       #     time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_lateral/datos_1.dat' with lines ")
        else:
            gp("exit")
            #time.sleep(1)
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Lat2(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('ii')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_lateral/datos_2.dat', 'a+')
    #        time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_lateral/datos_2.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Lat3(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('jj')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_lateral/datos_3.dat', 'a+')
            time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_lateral/datos_3.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Lat4(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('kk')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_lateral/datos_4.dat', 'a+')
            time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_lateral/datos_4.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Lat5(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('ll')
        for i in range(0, 1000):
            self.archi = open('datos_sensor_lateral/datos_5.dat', 'a+')
            time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_lateral/datos_5.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Fron0(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('mm')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_frontal/datos_0.dat', 'a+')
            #   time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_frontal/datos_0.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Fron1(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('nn')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_frontal/datos_1.dat', 'a+')
            #     time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_frontal/datos_1.dat' with lines ")
        else:
            gp("exit")
            #time.sleep(1)
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Fron2(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('oo')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_frontal/datos_2.dat', 'a+')
            #        time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_frontal/datos_2.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Fron3(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('pp')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_frontal/datos_3.dat', 'a+')
            time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_frontal/datos_3.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Fron4(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('qq')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_frontal/datos_4.dat', 'a+')
            time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_frontal/datos_4.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

    def Sen_Fron5(self):
        gp = Gnuplot.Gnuplot()
        gp("set title 'TIEMPO VS VOLTAJE EN EL DIODO LATERAL'")
        gp("set xlabel 'Tiempo en milesimas de segundos'") 
        gp("set ylabel 'Voltaje en milivoltios'")
        gp("set xrange [-10: 80000] ")
        gp("set yrange [-10: 4000] ")
        arduino=serial.Serial(self.puerto, 9600)
        time.sleep(2)
        arduino.write('rr')
        time.sleep(2)
        for i in range(0, 1000):
            self.archi = open('datos_sensor_frontal/datos_5.dat', 'a+')
            time.sleep(0.00005)
            x = arduino.readline()
            z = int(i*60)
            self.xo = str(z)
            self.yo = str(x)
            print('{0} {1}').format(self.xo, self.yo)
            self.archi.write ("\t")
            self.archi.write (self.xo)
            self.archi.write ("\t")
            self.archi.write (self.yo)
            self.archi.close()
            gp("plot 'datos_sensor_frontal/datos_5.dat' with lines")
        else:
            gp("exit")
            arduino.write('aa')
            print "El ciclo termino"
            os.system('sync')
            arduino.close()
        arduino.close()
        self.Sen_Lateral()

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

    def Sen_Lateral(self):
        self.Logo()
        print "\n  ########## MENU SENSOR LATERAL CON CONTROL VELOCIDAD MOTOR ###############"
        print "\n  Sensor lateral con vehiculo detenido      ------>          0"
        print "  Sensor lateral con primera velocidad      ------>          1"
        print "  Sensor lateral con segunda velocidad      ------>          2"
        print "  Sensor lateral con tercera velocidad      ------>          3"
        print "  Sensor lateral con cuarta Velocidad       ------>          4"
        print "  Sensor lateral con quinta velocidad       ------>          5"
        print "  VOLVER MENU PRINCIPAL                     ------>          6"
        print "  SALIR DEL PROGRAMA                        ------>          7"
        Sen_lat = input('\n DIGITA TU OPCION Y PULSA ENTER:    ')
        if Sen_lat == 0 :
            print "se procede a tomar datos del sensor lateral con velocidad 0"
            time.sleep(2)
            self.Sen_Lat0()

        elif Sen_lat == 1 :
            print "se procede a tomar datos del sensor lateral con velocidad 1"
            time.sleep(2)
            self.Sen_Lat1()

        elif Sen_lat == 2 :
            print "se procede a tomar datos del sensor lateral con velocidad 2"
            time.sleep(2)
            self.Sen_Lat2()

        elif Sen_lat == 3 :
            print "se procede a tomar datos del sensor lateral con velocidad 3"
            time.sleep(2)
            self.Sen_Lat3()

        elif Sen_lat == 4 :
            print "se procede a tomar datos del sensor lateral con velocidad 4"
            time.sleep(2)
            self.Sen_Lat4()

        elif Sen_lat == 5 :
            print "se procede a tomar datos del sensor lateral con velocidad 5"
            time.sleep(2)
            self.Sen_Lat5()        

        elif Sen_lat == 6:
            self.Menu_Principal()

        elif Sen_lat == 7:
            self.Salir()

        else :
            self.Sen_Lateral()

    def Salir(self):
        exit()

    def Sen_Frontal(self):
        self.Logo()
        print "\n  ########## MENU SENSOR FRONTAL CON CONTROL VELOCIDAD MOTOR ###############"
        print "\n  Sensor frontal con vehiculo detenido      ------>          0"
        print "  Sensor frontal con primera velocidad      ------>          1"
        print "  Sensor frontal con segunda velocidad      ------>          2"
        print "  Sensor frontal con tercera velocidad      ------>          3"
        print "  Sensor frontal con cuarta Velocidad       ------>          4"
        print "  Sensor frontal con quinta velocidad       ------>          5"
        print "  VOLVER MENU PRINCIPAL                     ------>          6"
        print "  SALIR DEL PROGRAMA                        ------>          7"
        Sen_fron = input('\n DIGITA TU OPCION Y PULSA ENTER:    ')
        if Sen_fron == 0 :
            print "se procede a tomar datos del sensor lateral con velocidad 0"
            time.sleep(2)
            self.Sen_Fron0()

        elif Sen_fron == 1 :
            print "se procede a tomar datos del sensor lateral con velocidad 1"
            time.sleep(2)
            self.Sen_Fron1()

        elif Sen_fron == 2 :
            print "se procede a tomar datos del sensor lateral con velocidad 2"
            time.sleep(2)
            self.Sen_Fron2()

        elif Sen_fron == 3 :
            print "se procede a tomar datos del sensor lateral con velocidad 3"
            time.sleep(2)
            self.Sen_Fron3()

        elif Sen_fron == 4 :
            print "se procede a tomar datos del sensor lateral con velocidad 4"
            time.sleep(2)
            self.Sen_Fron4()

        elif Sen_fron == 5 :
            print "se procede a tomar datos del sensor lateral con velocidad 5"
            time.sleep(2)
            self.Sen_Fron5()        

        elif Sen_fron == 6:
            self.Menu_Principal()

        elif Sen_fron == 7:
            self.Salir()

        else :
            self.Sen_Frontal()

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
        elif opcion == 1:
            self.Sen_Lateral()
        elif opcion == 2:
            self.Sen_Frontal()
        else:
            self.Menu_Principal()

    def __init__(self):
        self.Bienvenida()
        self.Test()
        self.Menu_Principal()
        
    def __del__(self):
        print "el programa finalizo"
modulo = Modulo() 
