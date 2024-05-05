clear all;
%%Variables (Edit yourself)

 fs = 625;
TimeInterval = 1/fs;
N = 256;
fscale = linspace(-fs/2,fs/2,N);
[B,A]=butter(3,0.2555);
[H,W]=freqz(B,A,N/2);
H2 = [fliplr(H.') H.'];
W = [-fliplr(W.') W.'];
W = (W*fs/2)./pi;

while(1)
    s = serialport('COM4', 115200);

    for i = 1:N+1

        %str = fscanf(s);
        x(i)=str2double(readline(s));
        pause(TimeInterval);
    end

    x = x(2:end);

    X = fft(x);
    X = X./max(abs(X));
    Xs = fftshift(abs(X));
    figure(1),plot(fscale(129:256),Xs(129:256)),axis([0,fs/2,0,1]),xlabel('Hz'),title('Normalized DFT of Samples'),ylabel('Magnitude');
    figure(2),plot(x),axis([0,N,-1.5,1.5]),title('Time-Domain Plot of Samples');
    clear x;
    
    clear s;
end

