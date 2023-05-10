%{
Landon Moon ENGR 1250-008 5/1/2021

Problem Statement:  

Variables:
H - altitude[meters]
L - location(tromosphere, lower/upper stratosphere)
p - pressure[kPa]
T - temperature[C]
%}
clear
clc

%input
H=input('What altitude in meters in the atmosphere do you want information about: ');

%input verification
if H<0||H>50000
    error('You entered a number that is outside the atmosphere.')
end

%determining the presure and tempature along with which layer.
if H<11000
    L='troposphere';
    T=15.04-(.00649*H);
    P=101.29*((T+273.1)/288.08)^5.256;
elseif H<25000
    L='lower stratosphere';
    T=-56.46;
    P=22.65*exp(1.73-.000157*H);
else
    L='upper stratosphere';
    T=-131+0.00299*H;
    P=2.488*((T+273.1)/216)^-11.388;
end

%output
fprintf('An altitude of %.0f is in the %s with a temperature of %.0f degrees C and pressure of %.0f kPa.', H, L, T, P)
