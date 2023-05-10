%{
Landon Moon ENGR 1250-008 4/20/2021

Problem Statement: plot the resistance of photoresistors against the
distance from a light source

variables:
L-Distance from light [m]
A-set A
B-set B
C-set C

x-theoretical x locations
*c-polyfit information
*y-theoretical y locations
%}
clear
clc
close all

%input data
L=[1 3 6 10];
A=[79 400 1100 2500];
B=[150 840 2500 4900];
C=[460 2500 6900 15000];

%generating trendlines
x=[0:.1:10];
Ac=polyfit(log10(L),log10(A),1);
Bc=polyfit(log10(L),log10(B),1);
Cc=polyfit(log10(L),log10(C),1);
Ay=10^Ac(2)*x.^Ac(1);
By=10^Bc(2)*x.^Bc(1);
Cy=10^Cc(2)*x.^Cc(1);


%plotting
hold on
grid on
plot(L,A,'ko','MarkerFaceColor','k')
plot(L,B,'bo','MarkerFaceColor','b')
plot(L,C,'mo','MarkerFaceColor','m')
plot(x,Ay,'k-')
plot(x,By,'b-')
plot(x,Cy,'m-')

%axis'
axis([0 10 0 15000])
set(gca,'Xtick',0:1:10,'Ytick',0:1000:15000)

%labels
title('CdS photoresistor resistance')
ylabel('Resistance (R) [Ω]')
xlabel('Distance from Light (d) [m]')

%legend
legend('CdS photoresistor A Resistance (R) [Ω]','CdS photoresistor B Resistance (R) [Ω]','CdS photoresistor C Resistance (R) [Ω]','location','best')