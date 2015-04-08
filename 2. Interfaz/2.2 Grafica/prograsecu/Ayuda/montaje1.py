#!/usr/bin/python
# -*- coding:utf-8 -*-
#ESTE PROGRAMA FUE REALIZADO POR DIEGO ALBERTO PARRA GARZON 
#EN LA CIUDAD DE BOGOTA
#UNIVERSIDAD DISTRITAL FRANCISCO JOSE DE CALDAS
 
from visual import *
x= -8
#++++++++++++++++++++++++CHASIS++++++++++++++++++++++++++++++++++++++++++++++++ 
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
cilindro2 = cylinder(pos=(-1.6,0,-0.6), axis=(0,0,1), radius=(0.3), color = color.black)
# +++++++++++++++++RODAMIENTO DELANTERO ++++++++++++++++++++++++++++++++++++++++
cilindro1 = cylinder(pos=(-6,0,-2), axis=(0,0,3), radius=(0.7), color = color.white)
cilindro2 = cylinder(pos=(-5.92, -3.6, -1.5), axis=(0,7,0), radius=(0.2), color = color.white)
cilindro3 = cylinder(pos=(-5.92, -5, -1.5), axis=(0,1.4,0), radius=(1.4), color = color.white)
cilindro4 = cylinder(pos=(-5.92, 3.5, -1.5), axis=(0,1.4,0), radius=(1.4), color = color.white)

#+++++++++++++++++++++++++++++RODAMIENTO TRASERO++++++++++++++++++++++++++++
cilindro5 = cylinder(pos=(5.92, -7, -1.5), axis=(0,14,0), radius=(0.2), color = color.white)
cilindro6 = cylinder(pos=(5.92, -8, -1.5), axis=(0,1.4,0), radius=(1.7), color = color.white)
cilindro7 = cylinder(pos=(5.92, 6.5, -1.5), axis=(0,1.4,0), radius=(1.7), color = color.white)

lamina1 = box(size = (8, 0.2, 2), pos =(3, 2, -1), color = color.white)
lamina2 = box(size = (8, 0.2, 2), pos =(3, -2, -1), color = color.white)
lamina3 = box(size = (0.2, 4, 2), pos =(7, 0, -1), color = color.white)
lamina4 = box(size = (0.2, 4, 2), pos =(-1, 0, -1), color = color.white)


#+++++++++++++++++++++++SISTEMA DE TRANSMISION ++++++++++++++++++++++++++++++
xo = 0.4
cilindro8 = cylinder(pos=(4.52, -2.5, -1.5), axis=(0,5,0), radius=(0.07), color = color.white)
cilindro9 = cylinder(pos=(3.52, -2.5, -1.5), axis=(0,5,0), radius=(0.07), color = color.white)
cilindro10 = cylinder(pos=(3.52, -0.7, -1.5), axis=(0,0.2,0), radius=(0.8), color = color.white)
cilindro11 = cylinder(pos=(4.52, -0.8, -1.5), axis=(0,0.4,0), radius=(0.2), color = color.blue)
cilindro12 = cylinder(pos=(5.92, 1, -1.5), axis=(0,0.2,0), radius=(0.9), color = color.white)
cilindro13 = cylinder(pos=(4.52, -0.5, -1.5), axis=(0,0.2,0), radius=(0.8), color = color.white)
cilindro14 = cylinder(pos=(1+xo, 0, -1), axis=(1.5,0,0), radius=(0.1), color = color.white)
cilindro15 = cylinder(pos=(2+xo, 0, -1), axis=(0.5,0,0), radius=(0.5), color = color.blue)
cilindro16 = cylinder(pos=(3.52, -0.5, -1.5), axis=(0,0.4,0), radius=(0.2), color = color.blue)
cilindro17 = cylinder(pos=(4.52, 0.8, -1.5), axis=(0,0.5,0), radius=(0.6), color = color.blue)


motor = box(size = (2.6, 2, 1.8), pos= (0.3,0,-1), color = color.yellow) 

#label0a = label(pos = (-7, -7 ,0 ), text= 'DIEGO ALBERTO PARRA GARZON',  font='sans', box = True, height = 12)
