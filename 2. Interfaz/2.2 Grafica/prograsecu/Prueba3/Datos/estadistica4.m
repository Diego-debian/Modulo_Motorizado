f = load ('Datos/dat4/datos_4.dat');
Y = f(:,2)/1000; 
Yp = sum(Y) /27; 
save -ascii 'Datos/dat4/promRad.dat' Yp