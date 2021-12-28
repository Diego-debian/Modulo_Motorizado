Modulo Motorizado
=================

Bienvenido a este proyecto, el cual tiene como finalidad desarrollar un vehículo motorizado para poder ilustrar ciertas propiedades de las ondas electromagnéticas como los son: difracción, absorbción y atenuación; en este repositorio encontrara:
 1. Instalación de los paquetes de software necesarios.
 2. Los planos eléctricos del hardware.
 3. Programación del microcontrolador atmega 328
 4. Programa para la obtención de datos y graficador en tiempo real de dichos datos.
 5. Guías de elaboración de los laboratorios propuestos para ilustrar las propiedades de la radiación electromagnética. 
 6. Análisis de datos.
 7. Licencia de software.

Para comenzar la descarga del repositorio así como su instalación haga clic en la carpeta [0. Inicio] (/0. Instalación/)


<p align="center"><img src="https://github.com/Diego-debian/Modulo_Motorizado/blob/master/2.%20Interfaz/2.2%20Grafica/Image/cap6.png" /></p>

Objetivos
=========

# Generales 

 * Utilizar tecnologías libres para la realización de este proyecto.
 * Crear un modulo motorizado controlado vía bluetooth para ilustrar propiedades de la radiación infrarroja como lo son la difracción, la absorción y la atenuación. 

## Específicos 

 * Utilizar un Sistema operativo GNU-Linux como plataforma para el desarrollo del software que va a controlar el hardware del dispositivo.
 * Con el microcontrolador atmega328P-PU  realizar la parte de control del hardware.
 * Utilizar diodos led infrarrojos, tanto receptores como emisores, para la   construcción del sensor que llevara integrado nuestro proyecto.
 * Utilizar un motor a 9 voltios DC e integrarlo al vehículo, junto con un transistor TIP 122   para el control de la velocidad del motor.
 * Utilizar un modulo Bluetooth HC-06 para arduino, el cual permita la comunicación a distancia con el dispositivo, sin necesidad de un sistema físico cableado.
 * Utilizar un transistor LM-7805CV para construir un transformador de voltaje de 9 voltios a 5 voltios para poder alimentar el microcontrolador atmega328P-PU, y los demás dispositivos del proyecto.
 * Encontrar el patrón de difracción de los diodos emisores en infrarrojo para determinar la longitud de onda de los diodos.
 * Encontrar una constante en el patrón de absorción de diferentes materiales que nos permita clasificarlos por su capacidad de absorber radiación infrarroja.
 * Encontrar una constante en el patrón de atenuación la cual nos tiene que llevar a la conclusión de como se atenúa este tipo de radiación a través del espacio.

Metodología 
===========

 * Diseñar  una placa micro controladora que sea muy parecida a la placa arduino uno, con diodos emisores y receptores infrarrojos, resistencias, condensadores para la creación de los instrumentos de medición.
 * Construir un modulo motorizado “Vehículo motorizado”, con instrumentos para el análisis de radiación infrarroja, en donde reposara nuestra placa micro controladora y sus respectivos instrumentos de medición.
 * Utilizar un sistema operativo de software libre como lo es debian 7 Jessie o Linux mint 17, y con programas como  arduino, python, c++, octave, gnuplot, libreoffice, kile, fritzing y emacs para la creación del software.
 * Crear el software, adaptarlo y configurar bien al hardware para que no surjan errores significativos con las mediciones. 
 * Crear unas guías de laboratorio la cual sea de fácil comprensión tanto a estudiantes como profesionales que estén relacionados con estos temas.

Referencia Bibliográfica 
========================

 * Notas del curso, python para el computo científico, curso de actualización académica de la DGAPA-UNAM, Facultad de ciencias, Dr. David P. Sanders, 5 de agosto de 2013. 
 * Manual básico de uso de minicom http://www.slideshare.net/Metaconta/manual-bsico- minicom-presentation .
 * Para la placa arduino, se toma de referencia http://www.proyectosarduino.com/ 
 * Para la programación en la tarjeta micro controladora arduino se utilizara la siguiente referencia http://www.arduino.cc/es/ 
 * Para la programación en c++ y gcc, GNU/Linux, Programación de sistemas, Pablo Garaizar Sagarminaga, Facultad de Ingeniería -ESIDE, Universidad de Deusto, Bilbao. 
 * Fundamentos de circuitos eléctricos, tercera edición, editorial Mc Graw Hill, Charles K. Alexander and Matthew N. O. Sadiku. 
Manual del proyecto octave http://www.gnu.org/software/octave/doc/interpreter/ 
 * Pagina oficial del proyecto gnuplot http://www.gnuplot.info/ 
 * Pagina oficial del proyecto Libreoffice http://www.libreoffice.org/ 
 * Edición de textos científicos Latex, Walter Mora, Alexander Borbon
 * Escuela de matemática,Instituto Tecnológico de Costa Rica; Revista digital matemática, educación e Internet www.tec-digital.itcr.ac.cr/revistamatematica/ 
 * Manual del usuario emacs http://www.nongnu.org/emacs-man-es/ 
 * Pagina oficial del Sistema Operativo debian https://www.debian.org/index.es.html 
 * Pagina oficial del proyecto fritzing http://fritzing.org/home/ 
 * Física Macarenha Herrera Aguayo, Edición especial para el ministerio de educación Chileno, editorial Santillana. 
 * Berkeley Physics Course Vol 3 Ondas (Crawford), editorial Reverte 
 * Para el integrado microcontrolador atmega328 se utilizara esta pagina  http://www.futurlec.com/Atmel/ATMEGA328P-PU.shtml
 * Para el uso del TIP 122 se toma de referencia esta pagina http://pdf.datasheetcatalog.com/datasheet/fairchild/TIP122.pdf
 * Para el modulo Bluetooth HC-06 arduino se toma esta referencia http://42bots.com/tutorials/hc-06-bluetooth-module-datasheet-and-configuration-with-arduino/
 * Con el transistor LM7805CV se toma de referencia http://www.fairchildsemi.com/ds/LM/LM7805.pdf
 * Pagina oficial de Scilab http://www.scilab.org/
 * Pagina oficial de los productos  Phywe http://www.phywe.com/448/Product-Catalogue.htm
 



Mesa de Miembros del Proyecto
=============================

 1. Diego Alberto Parra Garzón <diegoestudianteud1@gmail.com> Desarrollador de Contenidos


