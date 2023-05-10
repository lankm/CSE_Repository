%{
header

Landon Moon ENGR1250-008 4/8/21
graphing example: data points

housekeeping
%}

clear
clc
close all

h1=[10 30 50 70 100]; %x axis
P1=[0.12 0.30 0.55 0.75 1.10]; %y axis

h2=[10 15 25 35 60];
P2=[0.26 0.35 0.65 0.90 1.50]; %y axis


figure('Color','w')
plot(h1,P1,'sr','MarkerFaceColor','r','MarkerSize',10)
hold on
plot(h2,P2,'db','MarkerFaceColor','b','MarkerSize',10)
grid on
grid minor

xlabel('Height (H) [m]')
ylabel('Power (P) [hp]')

axis([0 120 0 1.75])
set(gca,'Xtick',0:20:120,'Ytick',0:0.25:1.75)
ytickformat('%.2f')

legend('Mass 250kg','Mass 100kg','location','best')
