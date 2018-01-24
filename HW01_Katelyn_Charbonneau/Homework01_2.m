%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 2

clear
clc

format compact

%Specify pretty fine step size
x = -10:0.00001:10-0.01;
y = (x.^3)./(x.^2-2*abs(x-2));

plot(x,y)
xlabel('x')
ylabel('y')

%The maximum value (as well as the index it appears in the array)
[Maximum_Value, Maximum_Index] = max(y)
[Minimum_Value, Minimum_Index] = min(y)