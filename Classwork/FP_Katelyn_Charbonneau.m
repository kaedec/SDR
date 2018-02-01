%Katelyn Charbonneau
%CPE490 Software Defined Radio Jan24Classwork

clear
clc

format short
format compact


Fs = 5000;
Ts = 1/Fs;
fm = 5;
fc = 40;
Am = 1;
Ac = 1;
mu = 0.5;
t = [0:Ts:2-Ts];

[ct_am, mt_am, st_am, sf_am] = AM_Amp_Mod(Fs, fm, fc, Am, Ac, mu, t);
L_am = length(st_am);
f_am = Fs*((-L_am/2):(L_am/2-1))/L_am;

%% Plotting for AM
figure(1)
subplot(3,1,1), plot(f_am, abs(fftshift(fft(mt_am, L_am)))/(L_am))
title('mt')
xlabel('Freq(Hz)')
ylabel('m(f)')

subplot(3,1,2), plot(f_am, abs(fftshift(fft(ct_am, L_am)))/(L_am))
title('ct')
xlabel('Freq(Hz)')
ylabel('c(f)')

subplot(3,1,3), plot(f_am, abs(fftshift(fft(st_am, L_am)))/(L_am))
title('st')
xlabel('Freq(Hz)')
ylabel('s(f)')

[ct_dsb, mt_dsb, st_dsb, sf_dsb] = DSB_Amp_Mod(Fs, fm, fc, Am, Ac, mu, t);
L_dsb = length(st_dsb);
f_dsb = Fs*((-L_dsb/2):(L_dsb/2-1))/L_dsb;

%% Plotting for DSB
figure(2)
subplot(3,1,1), plot(f_dsb, abs(fftshift(fft(mt_dsb, L_dsb)))/(L_dsb))
title('st')
xlabel('Freq(Hz)')
ylabel('s(f)')

subplot(3,1,2), plot(f_dsb, abs(fftshift(fft(ct_dsb, L_dsb)))/(L_dsb))
title('st')
xlabel('Freq(Hz)')
ylabel('s(f)')

subplot(3,1,3), plot(f_dsb, abs(fftshift(fft(st_dsb, L_dsb)))/(L_dsb))
title('st')
xlabel('Freq(Hz)')
ylabel('s(f)')
