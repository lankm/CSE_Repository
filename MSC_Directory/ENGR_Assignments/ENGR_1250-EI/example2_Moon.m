clear
clc
close all

B_0=10;
k1=0.2;
k2=0.3;

t=[0:0.1:5];
B1=B_0*exp(k1*t);
B2=B_0*exp(k2*t);

figure('Color','w')
plot(t,B1,'--r',t,B2,':g','LineWidth',3)
grid on

xlabel('Time (t) [hr]')
ylabel('Concentration (B) [#]')

axis([0 5 0 50])
set(gca,'Xtick',0:1:5,'Ytick',0:10:50)

LT={'0.2/hr' '0.3/hr'};
legend(LT,'Location','Best')

