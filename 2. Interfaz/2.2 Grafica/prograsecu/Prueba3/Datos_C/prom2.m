f= load('Datos_C/dat2/datos_2.dat');
  f1=sum(f())
  f2=f1/50
save -ascii 'Datos_C/dat2/prom.dat' f2
