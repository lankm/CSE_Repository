%{
Landon Moon ENGR 1250-008 4/8/2021

Problem Statement:  Display a set of data

I would personally display the total instead of the individual data points
but the question doesn't ask for the total distance before you stop

Variables:
vs - speed of a vehicle [mph]
rea - distance it takes for the driver to react [m]
bra - distance it takes after the driver starts braking [m]
%}

clear
clc
close all

%setting input data
vs=[20 30 40 50 60 70];
rea=[6 9 12 15 18 21];
bra=[6 14 24 38 55 75];


%plotting the data
figure('color','w')
plot(vs,rea,'or','MarkerFaceColor','r')
hold on
plot(vs,bra,'sk','MarkerFaceColor','k')
grid on

%labels
xlabel('Vehicle Speed (v) [mph]')
ylabel('Distance (d) [m]')

%axis'
axis([0 80 0 80])
set(gca,'Xtick',0:10:80,'Ytick',0:10:80)

%legend
LG={'Reaction [m]' 'Braking [m]'};
legend(LG,'Location','Best')