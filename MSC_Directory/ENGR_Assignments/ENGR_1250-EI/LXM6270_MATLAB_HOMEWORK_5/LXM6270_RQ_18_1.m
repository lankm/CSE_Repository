%{
Landon Moon ENGR 1250-008 5/1/2021

Problem Statement:  determing the status of an Apple TV based on its
wattage.
assumptions: power ranges are inclusive on the lower bounds of each.

Variables:
W - watts of the Apple TV [watts]
State - the current state of the Apple TV [string]
%}
clear
clc

%getting current wattage
W=input('What is the current wattage for the Apple TV: ');

%determining the current state
if W<0||W>2
    error('The state of the device is unknown. the given wattage is outside the normal range.');
elseif W<.5
    State='Off/Standby';
elseif W<1.5
    State='Idle';
elseif W<1.6
    State='Streaming via Ethernet';
else
    State='Streaming via Wifi';
end

%outputting data
fprintf('The current state of your Apple TV is: %s', State)
