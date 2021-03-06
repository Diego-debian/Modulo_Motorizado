#!/usr/bin/python
# -*- coding:utf-8 -*-
#ESTE PROGRAMA FUE REALIZADO POR DIEGO ALBERTO PARRA GARZON 
#EN LA CIUDAD DE BOGOTA
#UNIVERSIDAD DISTRITAL FRANCISCO JOSE DE CALDAS 

from visual import *
x= -8
frente1 = box(size = (1, 5, 0.6), pos = (0+x, 0, 0), color = color.red)
frente2 = box(size = (3, 3, 0.6), pos =(2+x, 0 ,0), color = color.red)
frente3 = box(size = (7.5, 5, 0.6), pos =(7+x, 0 , 0), color = color.red)
frente4 = box(size = (1.5, 3, 0.6), pos =(8+x, 4 , 0), color = color.red)
frente5 = box(size = (1.5, 3, 0.6), pos =(8+x, -4 , 0), color = color.red) 
frente6 = box(size = (5, 11, 0.6), pos =(13.1+x, 0 , 0), color = color.red)
frente7 = box(size = (1, 3.5, 0.6), pos =(16+x, 3.8 , 0), color = color.red)
frente8 = box(size = (1, 2.5, 0.6), pos =(16+x, -4.3 , 0), color = color.red)  
frente9 = box(size = (2, 2, 0.6), pos =(9.6+x, 3.3 , 0), color = color.red)  
frente10 = box(size = (2, 2, 0.6), pos =(9.6+x, -3.3 , 0), color = color.red)  

caja1 = box(size = (0.2, 30, 0.6), pos =(-15, 0 ,0), color = color.white)
caja2 = box(size = (0.2, 30, 0.6), pos =(15, 0 ,0), color = color.white)
caja3 = box(size = (30, 0.2, 0.6), pos =(0, 15 ,0), color = color.white)
caja4 = box(size = (30, 0.2, 0.6), pos =(0, -15 ,0), color = color.white)

cilindro1 = cylinder(pos=(-6,0,0), axis=(0,0,1), radius=(0.7), color = color.black)
cilindro2 = cylinder(pos=(-1.6,0,-0.6), axis=(0,0,1), radius=(0.3), color = color.black)

label0a = label(pos = (-7, -7 ,0 ), text= 'DIEGO ALBERTO PARRA GARZON',  font='sans', box = True, height = 12)
label0 = label(pos = (-7, 7 ,0 ), text= 'ESQUEMA CHASIS',  font='sans', box = True, height = 12)
label1 = label(pos = (-9, 0 ,0 ), text= '5 cm',  font='sans', box = True, height = 10)
label2 = label(pos = (-8.2, 2.9 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label3 = label(pos = (-7.1, 2 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label4 = label(pos = (-5.4, 2 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label5 = label(pos = (-3, 3 ,0 ), text= '4 cm',  font='sans', box = True, height = 10)
label6 = label(pos = (-1.4, 4 ,0 ), text= '3 cm',  font='sans', box = True, height = 10)
label7 = label(pos = (0, 6 ,0 ), text= '1.5 cm',  font='sans', box = True, height = 10)
label8 = label(pos = (1.3, 5 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label9 = label(pos = (-6.2, 1 ,0 ), text= '3 cm',  font='sans', box = True, height = 10)
label10 = label(pos = (3, 5 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label11 = label(pos = (1.5, 4 ,0 ), text= '2 cm',  font='sans', box = True, height = 10)
label12 = label(pos = (6, 6 ,0 ), text= '6 cm',  font='sans', box = True, height = 10)
label12 = label(pos = (9.4, 4 ,0 ), text= '2.5 cm',  font='sans', box = True, height = 10)
label13 = label(pos = (8.4, -0.5 ,0 ), text= '6 cm',  font='sans', box = True, height = 10)
label14 = label(pos = (-8.2, -2.9 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label15= label(pos = (-7.1, -2 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label16= label(pos = (-5.4, -2 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label17= label(pos = (-3, -3 ,0 ), text= '4 cm',  font='sans', box = True, height = 10)
label18= label(pos = (-1.4, -4 ,0 ), text= '3 cm',  font='sans', box = True, height = 10)
label19= label(pos = (0, -6 ,0 ), text= '1.5 cm',  font='sans', box = True, height = 10)
label20 = label(pos = (1.3, -5 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label21 = label(pos = (-6.2, -1 ,0 ), text= '3 cm',  font='sans', box = True, height = 10)
label22 = label(pos = (3, -5 ,0 ), text= '1 cm',  font='sans', box = True, height = 10)
label23 = label(pos = (1.5, -4 ,0 ), text= '2 cm',  font='sans', box = True, height = 10)
label24 = label(pos = (6, -6 ,0 ), text= '6 cm',  font='sans', box = True, height = 10)
label25 = label(pos = (9.4, -4 ,0 ), text= '2.5 cm',  font='sans', box = True, height = 10)
label26 = label(pos = (-4.4, 0 ,0 ), text= 'r = 0.7 cm',  font='sans', box = True, height = 10)
label27 = label(pos = (0, 0 ,0 ), text= 'r = 0.2 cm',  font='sans', box = True, height = 10)
