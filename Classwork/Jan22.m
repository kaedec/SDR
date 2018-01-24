%Katelyn Charbonneau
%CPE490 Software Defined Radio Jan22Classwork

clear
clc

format short
format compact

fs = 5000;
t = [0:1/fs:2-1/fs]; %the subtracted 1/fs is very important - b/c otherwise is 10001 not 10000

st = sin(5*2*pi*t);

%figure(1)
%plot(x,st)

sf = fft(st);

L = length(st);

f = (0:L-1)*(fs/L);

figure(2)
plot(f, sf)