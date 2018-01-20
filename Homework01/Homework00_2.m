%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 2

clear all
clc

format short
format compact

t = [-10:0.001:10];

sint = (exp(j*t)-exp(-j*t))/(2*j);

subplot(3,1,1), plot(t, sint)
subplot(3,1,2), plot(t, sin(t))
subplot(3,1,3), plot(t,sint-sin(t))