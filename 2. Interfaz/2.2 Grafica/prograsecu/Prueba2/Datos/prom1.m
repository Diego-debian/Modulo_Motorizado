f= load('dat0/datos_0.dat')
f1=sum(f())
f2=f1/1000
save -ascii "prom.dat" f2
