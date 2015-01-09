f= load('Datos_C/dat4/datos_4.dat');
  f1=sum(f())
  f2=f1/50
save -ascii 'Datos_C/dat4/prom.dat' f2
