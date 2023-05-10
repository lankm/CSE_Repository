%{
Landon Moon 1250-008 4/16/2021
problem statemnt: develope a software ordering system for FunCereals Inc.

I put comments noting which steps go with what blocks of code. I saw in the
instructions saying that constants should be stored in varibles. I didn't
see any cases that needed it becuase its just conversion but I put comments
explaining why and some commented code for if I used solved the problem
using a constant.
%}
clear
clc
close all

%1
Specs={'Crazy Marshmallows' 0.100 20 5 22 3.00;'Cinnamonairs' 0.168 20 4.5 24.5 1.75;'Loopy Loops' 0.103 20 5.5 30.5 1.50;'Crunch Bunch' 0.118 20 7 32 2.50};

%2
S=size(Specs); %size of Specs
Choice=menu('What cereal would you like to order?',Specs(1:S(1),1));

%3
Box=input('Enter the number of boxes you would like: ');

%4
UserName=input('Enter your name: ','s');

%5
%SG is in g/cm^3 by default. I saw this problem as just a conversion
%problem so I didn't state the density of water because its just 1g/cm^3.
%Here's the code for if you want me to multiply by a the constant instead.
%SGw=1000;
%Dense=Specs{Choice,2}*SGw;
Dense=Specs{Choice,2}*1000; %converting given SG into kg/m^3

%6
V=Specs{Choice,3}*Specs{Choice,4}*Specs{Choice,5}; %volume in cm^3
V=V/1000000; %converting from cm^3 to m^3. dividing by 100 three times is the same as dividing by 1000000

%7
Mass=Dense*V; %mass of the box in kg
Mass=Mass*2.205; %converting kg to lbm. Constant of gravity is not needed to convert to lbm since its not a force
Cost=Mass*Specs{Choice,6}; %mass times cost per mass.

%8
CName=Specs{Choice,1};

%9
fprintf('%s ordered %.0f boxes of %s cereal. The total cost of the order is $%.2f.',UserName,Box,CName,Cost*Box)

%10
CData=[5 10 15 20 25 30;7 15 22 29 36 44];
L=length(CData);
x=CData(1,1:L);
y=CData(2,1:L);
%plotting
plot(x,y,'dk','MarkerSize',15,'MarkerFaceColor','k')
grid on
%labels
xlabel('Number of Boxes (N) [#]','FontSize',18,'FontWeight','bold')
ylabel('Total Cost (C) [$]','FontSize',18,'FontWeight','bold')
%axis
axis([0 35 0 50])