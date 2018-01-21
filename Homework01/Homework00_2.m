%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 2

clear all
clc

format short
format compact

t = [-2*pi:0.1:2*pi];

sint = (exp(j*t)-exp(-j*t))/(2*j);

subplot(2,1,1), plot(t, sint, 'r;Formula;', t, sin(t), 'b;Function;')
title('sin(t) Formula Compared to Function')
xlabel('t')
ylabel('sint and sin(t)')
axis([-2*pi 2*pi -1 1])
%xticks([-2*pi -pi 0 pi 2*pi])
%xticklabels({'-2\pi', '-\pi', '0', '\pi', '2\pi'})


subplot(2,1,2), plot(t, sint-sin(t))
title('Difference Between Formula and Function')
xlabel('t')
ylabel('sint-sin(t)')
axis([-2*pi 2*pi -1 1])