f= load('Datos_C/dat1/datos_1.dat');
  f1=sum(f())
  f2=f1/200
save -ascii 'Datos_C/dat1/prom.dat' f2
