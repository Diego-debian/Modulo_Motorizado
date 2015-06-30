f = load ('Datos_C/dat1/datos1_.dat');
X = f(:,1)/100;
Y = f(:,2)/1000;
ff = [X, Y];
U = log(X);
V = log(Y);
U2 = U .* U;
UV = U .* V; 
sumX = sum(X);
sumY = sum(Y);
sumU = sum(U);
sumV = sum(V);
sumU2 = sum(U2);
sumUV = sum(UV);
promX = sumX/111;
promY = sumY/111;   			
promU = sumU/111;
promV = sumV/111;
promU2 = sumU2/111;
promUV = sumUV/111;
Suv = promUV - promU*promV;
Su2 = promU2 - promU*promU;
b = Suv / Su2
A = promV - b*promU
a = exp(A)
save -ascii 'Datos_C/dat1/xy.dat' ff;
save -ascii 'Datos_C/dat1/a.dat' a;
save -ascii 'Datos_C/dat1/A.dat' A;

