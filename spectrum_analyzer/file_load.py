#!/usr/bin/env python
import scipy
import numpy
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.signal import blackman

f = scipy.fromfile(open("spectrum_data_50dB_1000voice.bin"), dtype=scipy.float32)
#conv = open("spectrum_data_1.txt")
#print conv
#conv.read()

#f = [ord(c) for c in conv]


#f2 = open("spectrum_data_2.dat", "w")
#f2.write(f)
#f2.close

temp = []
temp2 = []

#print len(f)
#m = max(f)
#print f

window_size = 1
halfway_point = len(f)/2
window_start = 3/2*halfway_point+(1024*0)
window_end = window_start+(1024*window_size*5)

for i in range(int (window_start), int (window_end)):
	#if f[i] > 25:
	temp.append(f[i])
		#print temp
		#print f[i]
	#else:
		#temp.append(0)

for i in range(0, int (1024*window_size)):
	avg_val = numpy.mean([temp[i], temp[i+1024], temp[i+2*1024], temp[i+3*1024], temp[i+4*1024]])
	#if avg_val > 20:
	temp2.append(avg_val)
	#else:
		#temp2.append(0)

print len(temp2)


## FFT Conversion

N = 2048*window_size # number of points
T = 1.0/2048.0
w = blackman(N/2)

#yf = fft(temp)
xf = numpy.linspace(0.0, 1.0/(2.0*T), N//2)

print len(temp)
print len(xf)

#plt.semilogy(xf[1:N//2], 2.0/N * numpy.abs(yf[1:N//2]), '-b')
plt.plot(xf, temp2)
plt.show()

#somedata = [100, 110, 120]
#dataB = struct.pack("3B", *somedata)
#print repr(dataB)
#conv = [ord(c) for c in dataB]
#print conv
