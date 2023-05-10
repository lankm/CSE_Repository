%{
Landon Moon ENGR 1250-008 3/22/2021

Problem Statement:  Determines the side of a cube of gold

Variables:
m - mass of the cube [kg]
SG - specific gravity of gold [g/cm^3]

mG - mass of the cube in grams [g]
V - volume of the cube [cm^3]
Lcm - side length of cube [cm]
L - final side length of cube [in]
%}

clear
clc

%Set input variables listed above
m=.4;
SG=19.3;

%Calculate the mass in grams, volume, and side length
mG=m*1000;
V=mG/SG;
Lcm=nthroot(V,3);

%convert Lcm [cm] to L [in]
L=Lcm/2.54
