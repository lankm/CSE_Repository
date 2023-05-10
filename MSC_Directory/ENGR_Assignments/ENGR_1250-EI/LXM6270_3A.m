%{
Landon Moon ENGR 1250-008 4/13/21
Problem statement: follow instructions
housekeeping
%}

clear
clc


beam={'Steel' 5 11.8;'Titanium' 7 13.1;'Copper' 9 12.5};
ops=beam(:,1);

choice=menu('Beam Material',ops);

actual=input('Emter a deflection of no more than 4 inches (in inches): ');
actual=actual*2.54;
ref=beam{choice,3};

diff=abs(actual-ref)/ref;

fprintf('The %s beam has an actual deflection of %.1f cm\n\n',beam{choice,1},ref);
fprintf('Your entry is %.0f%% less delection than the reference beam.\n',diff*100)