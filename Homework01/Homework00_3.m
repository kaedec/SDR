%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 2

clear all
clc

format short
format compact

x = -10:0.1:10;
y = -10:0.1:10;

[X, Y] = meshgrid(x,y);

f = sinc(X.^2+Y.^2);

figure(1)
mesh(X,Y,f)
%colormap('bone')

figure(2)
surf(X,Y,f)