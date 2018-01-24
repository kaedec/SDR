%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 3

clear
clc

format compact

%Generate t values
t = linspace(-2*pi,2*pi,100);

%Generate the formula
sint = (exp(j*t)-exp(-j*t))/(2*j);

%Plots the formula and sin(t) function on top of each other
%The formula is shown in red; the function in blue
subplot(2,1,1);
plot(t, sint, 'r', t, sin(t), 'b')
title('sin(t) Formula Compared to Function')
xlabel('t')
ylabel('sint and sin(t)')
axis([-2*pi 2*pi -1 1])
xticks([-2*pi -pi 0 pi 2*pi])
xticklabels({'-2\pi', '-\pi', '0', '\pi', '2\pi'})
legend('Formula','Function')

%Plots the difference between the two (expected to be constant 0)
subplot(2,1,2);
plot(t, sint-sin(t))
title('Difference Between Formula and Function')
xlabel('t')
ylabel('sint-sin(t)')
axis([-2*pi 2*pi -1 1])
xticks([-2*pi -pi 0 pi 2*pi])
xticklabels({'-2\pi', '-\pi', '0', '\pi', '2\pi'})