Modulo Motorizado
==============

Bienvenido a este proyecto, el cual tiene como finalidad desarrollar un vehículo motorizado para poder ilustrar ciertas propiedades de las ondas electromagnéticas como los son: difracción, absorbción y atenuación; en este repositorio encontrara:
 1. Instalación de los paquetes de software necesarios.
 2. Los planos eléctricos del hardware.
 3. Programación del microcontrolador atmega 328
 4. Programa para la obtención de datos y gratificador en tiempo real de dichos datos.
 5. Guías de elaboración de los laboratorios propuestos para ilustrar las propiedades de la radiación electromagnética. 
 6. Análisis de datos.
 7. Licencia de software.

Objetivos
=========

# Generales 

 * Utilizar tecnologías libres para la realización de este proyecto.
 * Crear un modulo motorizado controlado vía bluetooth para ilustrar propiedades de la radiación infrarroja como lo son la difracción, la absorción y la atenuación. 

##Específicos 

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

 
Para comenzar la descarga del repositorio así como su instalación haga clic en la carpeta [0. Inicio] (/0. Instalación/)


Mesa de Miembros del Proyecto
=============================

 1. Diego Alberto Parra Garzón <diegoestudianteud1@gmail.com> Desarrollador de Contenidos


