%{
Landon Moon ENGR 1250-008 3/22/2021

Problem Statement:  Determines the distance the Microjoule will travel
given an amount of fuel

Variables:
F - amount of fuel [g]
SG - specific gravity of ethanol [g/cm^3]
P - performace of the MicroJoule [mi/gal]

Vcm - volume of fuel [cm^3]
Vgal - volume of fuel [gal]
Dmi - distance traveled [mi]
Dkm - distance traveled [km]
%}

clear
clc

%Set input variables listed above
F=100;
SG=.789;
P=10705;

%Calculate volume in cm^3 and gal
Vcm=F/SG;
Vgal=Vcm/1000*.264;

%calculates the distance traveled in miles and km
Dmi=P*Vgal;
Dkm=Dmi/.621
