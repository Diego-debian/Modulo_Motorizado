f = load ('Datos/dat0/datos_0.dat');
Y = f(:,2)/1000; 
Yp = sum(Y) /200; 
save -ascii 'Datos/dat0/promRad.dat' Yp