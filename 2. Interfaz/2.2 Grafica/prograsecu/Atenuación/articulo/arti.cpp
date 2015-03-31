#include <iostream>
#include <fstream>
#include <iostream>
#include <stdlib.h>
using namespace std;
main()
{
  ofstream out;
  
  // ++++++++++++++++++++++ SALIDA A LATEX +++++++++++++++++++++++++++++++
  out.open("arti.tex");
  {
    out<<"\\documentclass[12]{article}"<<endl;
    out<<"\\usepackage[spanish,english]{babel}"<<endl;
    out<<"%\\usepackage[spanish]{babel}"<<endl;
    out<<"\\usepackage[utf8]{inputenc}"<<endl;
    out<<"\\usepackage{graphicx}"<<endl;
    out<<"\\usepackage{epsfig}"<<endl;
    out<<"\\usepackage{multicol,caption}"<<endl;
    out<<"\\usepackage{amsthm} % Theorem Formatting"<<endl;
    out<<"\\usepackage{amssymb}    % Math symbols such as \\mathbb"<<endl;
    out<<"\\usepackage{color}"<<endl;
    out<<"\\usepackage{hyperref}"<<endl;
    out<<"\\usepackage[none]{hyphenat}"<<endl;
    out<<"%\\renewcommand{\\tablename}{Tabla}"<<endl;
    out<<"%\\def\\tablename{Cuadro}% por \\def\\tablename{Tabla}% "<<endl;
    out<<"\\newenvironment{Figure}"<<endl;
    out<<"{\\par\\medskip\\noindent\\minipage{\\linewidth}}"<<endl;
    out<<"{\\endminipage\\par\\medskip}"<<endl;
    out<<"\\addto\\captionsspanish{%"<<endl;
    out<<"\\def\\tablename{Tabla}%"<<endl;
    out<<"}"<<endl;
    out<<"\\topmargin  = 10pt"<<endl;
    out<<"\\oddsidemargin  = -0.5in"<<endl;
    out<<"%\\headheight = 12pt"<<endl;
    out<<"%\\headsep    = 15pt"<<endl;
    out<<"%\\footskip   = 15pt"<<endl;
    out<<"\\textheight = 21.5 cm"<<endl;
    out<<"\\textwidth  = 18.5cm"<<endl;
    out<<"\\tolerance=10000"<<endl;
    out<<"\\title{\\bf{Ilustración de la propiedad de atenuación en ondas electromagnéticas en el espectro infrarrojo, utilizando tecnologías libres y de bajo costo}}"<<endl;
    out<<"\\author{Diego Alberto Parra Garzón \\footnote{diegoestudianteud1@gmail.com} \\\\ Universidad Distrital, Calle 3 No 26A-40 Bogotá-Colombia \\\\    Proyecto Curricular de Licenciatura en Física }"<<endl;
    out<<"\\date{\\today}"<<endl;
    out<<"\\begin{document}"<<endl;
    out<<"%\\def\\tablename{Cuadro}% por \\def \\tablename{Tabla}% "<<endl;
    out<<"\\renewcommand{\\tablename}{Tabla}"<<endl;
    out<<"\\maketitle"<<endl;
    out<<"\\vspace{-0.8cm}"<<endl;
    out<<"\\begin{abstract}"<<endl;
    out<<"This article presents a new way of illustrating the attenuation property with electromagnetic waves; as the wavelengths in the infrared are also part of the electromagnetic spectrum and everyday use we give to this radiation is very wide, so it is essential to place this resource for both students and professionals, for the experimental part is combined with the theoretical giving a feedback issue. Data were obtained from a motor module equipped with an infrared sensor receiver and an infrared LED emitter, which are controlled by a atmega microcontroller 328-Pu and this is linked via Bluetooth to a computer, this process is done by the computer with the help of free software like python, gnuplot, octave among other languages, it is worth noting that everything is done in a free operating system like linux mint or debian. Data analysis laboratory, which will have to shed the value of attenuation of electromagnetic waves and has to match what is in the scientific literature will.\\\\ \\\\"<<endl;
    out<<"{\\bf{Keywords:}} Maxwell's laws, electromagnetic attenuation data nonlinear regression."<<endl;
    out<<"\\end{abstract}"<<endl;
    out<<"\\selectlanguage{spanish}"<<endl;
    out<<"\\begin{abstract}"<<endl;
    out<<"El presente articulo presenta una nueva forma de ilustrar la propiedad de atenuación que tienen las ondas electromagnéticas; como las longitudes de onda en el  infrarrojo también hacen parte del espectro electromagnético y el uso diario que le damos a esta radiación es muy amplio, por ello es indispensable colocar este recurso tanto para estudiantes como profesionales, pues se combina la parte experimental con lo teórico dando una retroalimentación del tema en cuestión. Se obtendrán los datos a partir de un modulo motorizado equipado con un sensor infrarrojo receptor y un led infrarrojo emisor, los cuales son controlados por un microcontrolador atmega 328-Pu y este va enlazado vía bluetooth a un ordenador, todo este proceso lo realiza el ordenador con la ayuda de software libre como python, gnuplot, octave entre otros lenguajes, cabe resaltar que todo se realiza en un sistema operativo libre como lo es linux mint o debian. Se hará el análisis de datos del laboratorio, el cual tendrá que arrojar el valor de atenuación de las ondas electromagnéticas y tiene que coincidir con el que se encuentra en la literatura científica.\\\\ \\\\"<<endl;
    out<<"{\\bf{Descriptores:}} Leyes de Maxwell, atenuación electromagnética, regresión no lineal de datos."<<endl;
    out<<"\\end{abstract}"<<endl;
    out<<"\\begin{multicols}{2}"<<endl;
    out<<"\\section{Introducción}"<<endl;
    out<<"El arreglo experimental esta esquematizado en la Fig. 1 y constaba de un horno con un pequeño orificio de salida para calentar el gas, luego de la salida un colimador y un selector de velocidades, y finalmente, un detector de partículas."<<endl;
    out<<"\\end{multicols}"<<endl;
    out<<"\\end{document}"<<endl;
    out.close();
  }    
  system("pdflatex arti.tex");
  system("evince arti.pdf");
  return 0;
}
