% precalculated values
N = 3;
Oc = .2555;

% calculating poles
poles = zeros(1,N);
for k = 0:N-1
    poles(k+1) = Oc*exp(1i*(pi+2*k*pi)/(2*N))*exp(1i*(pi/2));
end

% frequency response
B = Oc^3;
A = poly(poles);
[H,W] = freqs(B,A,100);
figure(1),plot(W, abs(H))

% converting continuous tf to digital
Hc = tf(B,A);
Hd = c2d(Hc,1); % gave a slightly different answer compared to notes.

% cleaning up A and B
A = real(Hd.Denominator{1})
B = real(Hd.Numerator{1})

% frequency response around a circle
z = exp(1i*2*pi*(1:101)/101);
Hz = freqresp(Hd,z);
figure(2),plot(2*pi*(1:101)/101,abs(squeeze(Hz)))

