%{
Landon Moon ENGR 1250-008 4/20/2021

Problem Statement: plot power needed for diameters of impellers

variables:
D-diameter of the impeller [ft]
P-power required [hp]

x-theoretical x locations
*c-polyfit data
*y-theoretical y locations
%}
clear
clc
close all

%input data
D=[0.5 0.75 1 1.5 2 2.25 2.5 2.75];
P=[0.004 .04 .13 .65 3 8 18 22];

%generating trendlines
x=[0:.1:3];
Pc=polyfit(log10(D),log10(P),1);
Py=10^Pc(2)*x.^Pc(1);

%generating equation
TE=sprintf('P=%.3f*x^{%.3f}',Pc(2),Pc(1));
text(1,5,TE,'BackgroundColor','w','EdgeColor','k','Color','k')

%plotting
hold on
grid on
plot(D,P,'ko','MarkerFaceColor','k')
plot(x,Py,'k-')

%axis'
axis([0 3 0 30])
set(gca,'Xtick',0:1:3,'Ytick',0:5:30)

%labels
title('Mixer Impeller Power Requirements')
ylabel('Power (P) [hp]')
xlabel('Diameter (D) [ft]')