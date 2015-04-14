f = load ('Datos/dat2/datos_2.dat');
Y = f(:,2)/1000; 
Yp = sum(Y) /44; 
save -ascii 'Datos/dat2/promRad.dat' Yp