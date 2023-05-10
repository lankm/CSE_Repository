%{
Landon Moon ENGR 1250-008 4/1/2021

Problem Statement:  Determines the efficiency of a stovetop given inputs

Variables:
Tini - the initial tempature of the water [deg f]
Time - the time to boil [min]
Name - name and model of the stove
Power - the power of the stove-top [W]
SHwat - specific heat of water [J/(g*K)] 
Vol - volume of water being heated [gal]

Jreq - energy required [J]
Wpow - power used by burner [W]
Efic - effeciency of the burner [%]

mass - mass of the water [g]
dT - change in temperture [K]
Timesec - time in seconds [s]
%}

clear
clc

%set input values and formatting
fprintf('Household Appliance Efficiency Calculator: Stove\n\n');
Tini=input('Type the initial room temperature of the water [deg F]: ');
Time=input('Type the time it takes the water to boil [min]: ');
Name=input('Type the brand name and model of your stove: ','s');
Power=input('Type the power of the stove-top burner [W]: ');
SHwat=4.1841;
Vol=1;

%convert and calculate required variables for thermal energy equation
mass=Vol/.264*1000;
dT=(212-Tini)/1.8;
Timesec=Time*60;

%calculate output variables
Jreq=mass*SHwat*dT;
Wpow=Jreq/Timesec;
Efic=Wpow/Power*100;

%output data
fprintf('\nEnergy required\t\t    %.0f J',Jreq);
fprintf('\nPower used by burner    %.0f W',Wpow);
fprintf('\n\nBurner efficiency for a %s stove: %0.1f%%\n',Name,Efic);