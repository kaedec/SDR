%Katelyn Charbonneau
%CPE490 Software Defined Radio Jan22Classwork

clear
clc

format short
format compact

Fs = 5000;
Ts = 1/Fs;
fm = 5;
fc = 40;
Ac = 1;
Am = 1;
mu = 0.5;
t = [0:Ts:2-Ts];

DSB_Amp_Mod(Fs, fm, fc, Am, Ac, mu, t);

%ct = Ac*cos(2*pi*fc*t);
%mt = Am*cos(2*pi*fm*t);

%AM
%st = Ac.*(1+mu.*cos(2*pi*fm.*t)).*cos(2*pi*fc.*t);

%DSB
%st2 = mt.*ct;

%L = length(st);
%f = Fs*((-L/2):(L/2-1))/L;

%figure(1)
%plot(st)

%ft = fft(st);

%figure(2)
%subplot(3,1,1), plot(f, abs(fftshift(fft(mt, L)))/(L));
%subplot(3,1,2), plot(f, abs(fftshift(fft(ct, L)))/(L));
%subplot(3,1,3), plot(f, abs(fftshift(fft(st, L)))/(L));

%replace mt with ct for carrier signal
%mt is message signal
%replace with st for s signal, also normalize signal (divide by number of
%points we take)

%figure(3)
%subplot(3,1,1), plot(f, abs(fftshift(fft(mt, L)))/(L));
%subplot(3,1,2), plot(f, abs(fftshift(fft(ct, L)))/(L));
%subplot(3,1,3), plot(f, abs(fftshift(fft(st2, L)))/(L));