%Katelyn Charbonneau
%CPE490 Software Defined Radio Homework 01 Problem 1

clear
clc

format compact

%Inputs
%The problem only specifically requires 3x3 matrix multiplication
%As such, these need to be 3x3
x = [1 2 3; 4 5 6; 7 8 9];
y = [1 2 3; 4 5 6; 7 8 9];

%Nested for loop
%Does array multiplication of row.*colum for index (i,j) then sums values
for i = 1:3
    for j = 1:3
        z(i,j) = sum(x(i,:).*y(:,j)');
    end
end

disp('Result:')
disp(z)