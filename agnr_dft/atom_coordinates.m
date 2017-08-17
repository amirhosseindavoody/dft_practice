clear; clc;

a_cc = 1.42;		%Angstrom

N = 14;


x0 = 1.5;
y0 = sqrt(3)/2;
x (1:2:N) = 0;
x (2:2:N) = x0;
x (N+1:2:2*N) = 1;
x (N+2:2:2*N) = 1-x0;

y (1:N) = ((1:N)-1)*y0;
y (N+1:2*N) = ((1:N)-1)*y0;
x = x*1.42;
y = y*1.42;
z = zeros(size(x));

out = [x', y',z'];