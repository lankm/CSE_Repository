clear
clc
close all

Voltage=[18 30 40 45];
RectA=[5 18 24 30];
RectB=[15 26 34 50];

figure('Color','w')
plot(Voltage,RectA,'sk','MarkerSize',16,'MarkerFaceColor','k')
hold on
plot(Voltage,RectB,'or','MarkerSize',24,'MarkerFaceColor','r')
grid on

xlabel('Voltage (V) [V]','Color','r','EdgeColor','r')
ylabel('Current (I) [mA]')
title('Tracking current over rectifiers')

axis([0 50 0 60])
set(gca,'XTick',0:10:50,'YTick',0:20:60)

LT={'Rectifier A' 'Rectifer B'};
L=legend(LT,'Location','Best');
set(L,'TextColor','b','FontSize',16)
