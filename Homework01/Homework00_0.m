%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 0

clear all
clc

format short
format compact

x = [1 2 3; 4 5 6; 7 8 9];
y = [1 2 3; 4 5 6; 7 8 9];

for i = 1:3
    for j = 1:3
        z(i,j) = sum(x(i,:).*y(:,j)');
    end
end

z