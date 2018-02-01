function [ ct, mt, st, sf ] = DSB_Amp_Mod( Fs, fm, fc, Am, Ac, mu, t )
%DSB_Amp_Mod DSB Function

Ts = 1/Fs;

ct = Ac*cos(2*pi*fc*t);
mt = Am*cos(2*pi*fm*t);

st = ct.*mt;
sf = fft(st);
end