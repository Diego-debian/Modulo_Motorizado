#!/usr/bin/python
# -*- coding:utf-8 -*-


import os 
import subprocess
import math 

class Atenuacion():
    def Articulo(self):
        archi = open('articulo/arti.tex', 'a+')
        archi.write("%\\documentclass[12pt, twocolumn{article}] \\")
        archi.write("\\documentclass[12]{article}")
        archi.write("\\usepackage[spanish,english]{babel}")
        archi.write("%\\usepackage[spanish]{babel}")
        archi.write("\\usepackage[latin1]{inputenc}")
        archi.write("\\usepackage{graphicx}")
        archi.write("\\usepackage{epsfig}")
        archi.write("\\usepackage{multicol,caption}")
        archi.write("\\usepackage{amsthm} % Theorem Formatting")
        archi.write("\\usepackage{amssymb}    % Math symbols such as \mathbb")
        archi.write("\\usepackage{color}")
        archi.write("\\usepackage{hyperref}")
        archi.write("\\usepackage[none]{hyphenat}")
        archi.write("%\\renewcommand{\\tablename}{Tabla}")
        archi.write("%\\def\tablename{Cuadro}% por \\def\\tablename{Tabla}% ")
        archi.write("\\newenvironment{Figure}")
        archi.write("{\\par\\medskip\\noindent\\minipage{\\linewidth}}")
        archi.write("{\endminipage\par\medskip}")
        archi.write("\addto\captionsspanish{%")
        archi.write(" \def\\tablename{Tabla}%")
        archi.write("}")
        archi.write("\topmargin  = 10pt")
        archi.write("\oddsidemargin  = -0.5in")
        archi.write("%\headheight = 12pt")
        archi.write("%\headsep    = 15pt")
        archi.write("%\footskip   = 15pt")
        archi.write("\textheight = 21.5 cm")
        archi.write("\textwidth  = 18.5cm")
        archi.write("\tolerance=10000")
        archi.write("\title{\bf{Ilustración de la propiedad de atenuación en ondas electromagnéticas en el espectro infrarrojo, utilizando tecnologías libres y de bajo costo}}")
        archi.write("\author{Diego Alberto Parra Garzón \footnote{diegoestudianteud1@gmail.com}} \\")
        archi.write("Universidad Distrital, Calle 3 No 26A-40 Bogotá-Colombia\\")
        archi.write("   Proyecto curricular de licenciatura en física ")
        archi.write("}")
        archi.write("\date{\today}")
        archi.write("\begin{document}")
        archi.write("%\def\tablename{Cuadro}% por \def\tablename{Tabla}% ")
        archi.write("\renewcommand{\tablename}{Tabla}")
        archi.write("\maketitle")
        archi.write("\vspace{-0.8cm}")
        archi.write("\begin{abstract}")
        archi.write("This article provides an educational tool for visualization of the Maxwell-Boltzmann molecular-velocity-distribution law, into an ideal gas. It illustrates an experimental setup of a system of gas (air) molecules within a control volume, simulated by polystyrene pellets into a plastic bottle, where the pressure inside the bottle is maintained by an air pump. From drawing semicircle, polystyrene balls velocity measurement is made where an interesting distribution of velocities is obtained and fit to a Maxwell-Boltzmann-like distribution.\\")

        archi.write("{\bf{Keywords:}} Maxwell-Boltzmann Distribution, Ideal gas kinetic theory, physics education.")
        archi.write("\indent{\bf {PACS:}} 01.50.My, 01.40.Ha, 01.40.Fk.")
        archi.write("\end{abstract}")
        archi.write("\selectlanguage{spanish}")
        archi.write("\begin{abstract}")

        archi.write("El presente artículo aporta una herramienta didáctica para la visualización del la ley de distribución de velocidades de moléculas de Maxwell-Boltzmann, de un gas ideal. Se ilustra una disposición experimental de un sistema de moléculas de un gas al interior de un volumen de control, simulado por pequeñas esferas de poliestireno al interior de una botella de plástico, donde la presión dentro de la botella es mantenida por una bomba de aire. A partir de una disposición de semicírculos se realiza la medición de velocidades de las pequeñas esferas de poliestireno donde se obtiene una distribución interesante de velocidades que es ajustada a una curva que guarda la forma de la distribución de Maxwell-Boltzmann.\\")

        archi.write("{\bf{Descriptores:}} Distribución de Maxwell-Boltzmann, teoría cinética de gases, enseñanza de la física.")
        archi.write("\end{abstract}")


        archi.write("\end{document}")
        archi.close()

    def cArti(self):
        os.system("pdflatex 'articulo/arti.tex'") 
        os.system("evince ' articulo/arti.tex'")

    def __init__(self):
        self.Articulo()
        self.cArti()

    def __del__(self):
        print ("PROGRAMA FINALIZADO")

articulo = Atenuacion()
