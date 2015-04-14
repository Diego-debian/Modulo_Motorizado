f = load ('Datos/dat1/datos_1.dat');
Y = f(:,2)/1000; 
Yp = sum(Y) /52; 
save -ascii 'Datos/dat1/promRad.dat' Yp