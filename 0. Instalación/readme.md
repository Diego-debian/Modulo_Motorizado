Instalación 
===========

Para el correcto funcionamiento del programa es necesario instalar los siguientes programas:
 0. git 
 1. bluez* 
 2. gcc
 3. g++
 4. emacs
 5. gnuplot gnuplot-qt
 6. evince 
 7. octave
 8. python-matplotlib 
 9. python-numpy
 10. python-tk 
 11. python-gnuplot
 12. python-serial
 13. python-visual*
 14. libgtkglextmm*
 15. kile
 16. arduino 
 17. fritzing 
 18. eog
 19. arduino

lo primero sera instalar git en su S.O. dependiendo su S.O. el comando puede variar en mi caso uso debian y por lo general se instala de la siguiente manera.
    
Ingresar como usuario root

    $ su  

Introducir el Password, atención por que cuando escribimos el pass no se escribe en la terinal y esto es debido a razones de seguridad, pero claro que si se esta escribiendo. Luego de logeados escribimos:

    $ apt-get install git 

Luego de instalado debera escribir en una terminal el siguiente comando, esta vez no como superusuario sino como usuario normal para esto escribimos exit, luego oprimimos enter y luego escribimos lo siguiente.

    $ git clone https://github.com/Diego-debian/Modulo_Motorizado.git