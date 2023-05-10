%{
Landon Moon ENGR 1250-008 5/1/2021

Problem Statement:  Ask for a grade and return a letter grade

Variables:
G - grade [%]
LG - letter grade char [char]
%}
clear
clc

%getting user input
G=input('Enter your grade as a value between 0-100: ');

%converting to letter grade
if G>=90
    LG='A';
elseif G>=80
    LG='B';
elseif G>=70
    LG='C';
elseif G>=60
    LG='D';
else 
    LG='F';
end

%outputing
fprintf('Your letter grade is: %s', LG)