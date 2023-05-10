%{
Landon Moon ENGR 1250-008 3/22/2021

Problem Statement: calculate the mass of oxygen in a contatiner

Variables:
Vgal - volume of the container [gal]
Tcel - Temperture of the oxygen [C]
P - presure of the oxygen [atm]
R - gas constant [atm*L/mol*K]
MW - molecular weight of o2 [g/mol]

T - Temperture of the oxygen [K]
V - Volume of the container [L]
mols - amount of o2 atoms [mol]

m - mass of oxygen [g]
%}

clear
clc

%Set input variables listed above
Vgal=1.25;
Tcel=125;
P=2.5;
R=.08206;
MW=32;

%Converting to si units
T=Tcel+273;
V=Vgal/.264;

%calculating the amount of mols
mols=P*V/T/R;

%calculating the mass from the amount of mols
m=mols*MW