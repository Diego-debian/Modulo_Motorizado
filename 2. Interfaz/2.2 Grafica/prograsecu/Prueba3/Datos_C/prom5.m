f= load('Datos_C/dat5/datos_5.dat');
  f1=sum(f())
  f2=f1/50
save -ascii 'Datos_C/dat5/prom.dat' f2
