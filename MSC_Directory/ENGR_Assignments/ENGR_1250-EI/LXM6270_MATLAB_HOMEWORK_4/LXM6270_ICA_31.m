%{
Landon Moon ENGR 1250-008 4/20/2021

Problem Statement: plot resistnace against tempature for certain materials

variables:
T-Temperature [c]
CF-Carbon Film
DS-Doped Silicon

x-theoretical x locations
**c-polyfit information
**y-theoretical y locations
%}
clear
clc
close all

%input data
T=[15 20 25];
CF=[10.050 10.048 10.045];
DS=[10.15 9.85 9.48];

%generating trendlines
x=[15:.1:25];
CFc=polyfit(T,CF,1);
CFy=CFc(1)*x+CFc(2);
DSc=polyfit(T,DS,1);
DSy=DSc(1)*x+DSc(2);

%plotting
hold on
grid on
plot(T,CF,'bo','MarkerFaceColor','b')
plot(T,DS,'ko','MarkerFaceColor','k')
plot(x,CFy,'b-')
plot(x,DSy,'k-')

%axis'
axis([15 25 9 10.5])
set(gca,'Xtick',15:1:25,'Ytick',9:.1:10.5)

%labels
title('Material Resistance due to Temperature')
ylabel('Resistance (R) [Ω]')
xlabel('Temperature (T) [°C]')

%legend
legend('Carbon Film Resistance (R) [Ω]','Doped Silicon Resistance (R) [Ω]','location','best')