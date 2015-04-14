f = load ('Datos/dat3/datos_3.dat');
Y = f(:,2)/1000; 
Yp = sum(Y) /32; 
save -ascii 'Datos/dat3/promRad.dat' Yp