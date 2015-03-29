f = load ('datos1_.dat');
X = f(:,1);
Y = f(:,2);
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
promX = sumX/104;
promY = sumY/104;
promU = sumU/104;
promV = sumV/104;
promU2 = sumU2/104;
promUV = sumUV/104;
Suv = promUV - promU*promV;
Su2 = promU2 - promU*promU;
b = Suv / Su2
A = promV - b*promU
a = exp(A)


