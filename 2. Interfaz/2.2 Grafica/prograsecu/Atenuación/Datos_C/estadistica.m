f = load ('dat1/datos1_.dat');
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
promX = sumX/112;
promY = sumY/112;
promU = sumU/112;
promV = sumV/112;
promU2 = sumU2/112;
promUV = sumUV/112;
Suv = promUV - promU*promV;
Su2 = promU2 - promU*promU;
b = Suv / Su2
A = promV - b*promU
a = exp(A)
save -ascii 'dat1/xy.dat' ff;

