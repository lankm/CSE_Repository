%{
Landon Moon ENGR 1250-008 4/8/2021

Problem Statement:  plot data and make it look linear by changing the rate
of the axis'
Instructions: "plot only". I'm still displaying the line of best fit but not
printing it to the screen

Variables:
dia - diameter [ft]
pow - power [hp]

p - exponential to fit the data
m - power of the exponential
b - coeficient of the eponential
x - the x coordinates for the graph
y - the coresponding y coordinates
%}

clear
clc
close all

%setting input data
dia=[.5 .75 1 1.5 2 2.25 2.5 2.75];
pow=[.004 .04 .13 .65 3 8 18 22];

%setting up line of best fit
p=polyfit(log10(dia),log10(pow),1);
m=p(1);
b=10^p(2);

x=[0:.01:3];
y=b*x.^m;

%plotting data
figure('Color','w')
loglog(dia,pow,'or','MarkerFaceColor','r')
hold on
loglog(x,y,'k')
grid on

%labels
xlabel('Diameter (D) [ft]')
ylabel('Power (P) [hp]')
title('Turbine Power')

%axis'
axis([.5 3 .004 25])
set(gca,'Xtick',0:.5:3,'Ytick',0:2.5:25)

%legend
LT={'Data Points' 'Line of best fit'};
legend(LT,'Location','best')
