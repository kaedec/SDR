%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 1

clear all
clc

format short
format compact

x = -10:0.0001:10;
y = (x.^3)./(x.^2-2*abs(x-2));
plot(x,y)

[max, max_index] = max(y)
[min, min_index] = min(y)