%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 4

clear
clc

format compact

%Generate x and y axes
x = linspace(-10,10,100);
y = linspace(-10,10,100);
[X, Y] = meshgrid(x,y);

f = sinc(X.^2+Y.^2);

%Mesh plot
figure(1)
mesh(X,Y,f)

%Surface plot
figure(2)
surf(X,Y,f)

%The Mesh command plots a "mesh grid" where Surf plots a surface grid
%The colors can be changed by using the colorgrid command