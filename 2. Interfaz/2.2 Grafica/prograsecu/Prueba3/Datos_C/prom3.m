f= load('Datos_C/dat3/datos_3.dat');
  f1=sum(f())
  f2=f1/50
save -ascii 'Datos_C/dat3/prom.dat' f2
