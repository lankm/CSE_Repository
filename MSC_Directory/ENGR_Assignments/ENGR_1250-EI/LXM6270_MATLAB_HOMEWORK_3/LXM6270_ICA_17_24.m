%{
Landon Moon ENGR 1250-008 4/8/2021

Problem Statement:  plot the decay rate of an isotope

Variables:
C0 - initial amount of the element at time zero [g]
k - the decay rate of the isotope [hr]

t - time since beginning [hr]
C - values of the the element after  givent time [g]
%}

clear
clc
close all

%set input variables
C0=10;
k=1.48;

%get x and y coordinates
t=[0:.1:5];
C=C0*exp(-t*k);


%plotting the data
figure('Color','w')
plot(t,C,'or','MarkerFaceColor','r','MarkerSize',4)
grid on

%labels
xlabel('time (t) [hr]')
ylabel('amount of substance (m) [g]')

%axis'
axis([0 5 0 10])
set(gca,'Xtick',0:1:5,'Ytick',0:2.5:10)

%no legend is needed


