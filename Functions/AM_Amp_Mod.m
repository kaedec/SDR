function [ ct, mt, st, sf ] = AM_Amp_Mod( Fs, fm, fc, Am, Ac, mu, t )
%AM_Amp_Mod AM Function

Ts = 1/Fs;

ct = Ac*cos(2*pi*fc*t);
mt = Am*cos(2*pi*fm*t);

st = Ac.*(1+mu.*cos(2*pi*fm.*t)).*cos(2*pi*fc.*t);
sf = fft(st);
end