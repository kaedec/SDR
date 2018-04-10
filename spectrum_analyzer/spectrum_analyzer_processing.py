#!/usr/bin/env python
##################################################
# Python Data Processing
# Title: spectrum_analyzer_processing.py
# Author: Katelyn Charbonneau & John Oleksak
# Description: Processes data from a gnuradio-companion receive flow graph
#  in order to determine which frequencies are currently in use
#  and which frequencies are free to use
##################################################
# Update History
#
# 4/02/18 - Spectrum analysis project begun
# 4/04/18 - Python script begun; not functional
# 4/09/18 - Script debugged; properly plots FFT points
# 4/10/18 - Code organization and documentation; plots frequency instead of points
##################################################

import scipy						# Contains file reading function
import numpy						# Contains math functions
import matplotlib.pyplot as plt		# Plotting the data

pavg_data = []	# Pre-averaged snapshots
avg_data = []	# Averaged snapshots
freq_axis = []	# x-axis for plotting

##################################################
# Data Reading, Snapshotting, and Averaging
##################################################

# Read the selected data file (gnuradio-companion writes a float data type)
# YOU WILL HAVE TO CHANGE THIS NAME TO SELECT THE DESIRED FILE
# For simplicity's sake, put the data file in the same directory as this script
DATA_FILE = "spectrum_data_50dB_1000voice.bin"

f = scipy.fromfile(open(DATA_FILE), dtype=scipy.float32)

# Variables to allow for easier troubleshooting and testing
window_size = 1
halfway_point = len(f)/2
window_start = 3/2*halfway_point+(1024*0) # Start at 75% of the data
window_end = window_start+(1024*window_size*5) # Take 5 snapshots

# Fill pavg_data with 5 sets of 1024 FFT data points
for i in range(int (window_start), int (window_end)):
	pavg_data.append(f[i])

# set_floor defines whether to plot all data for testing or development
#  or to set values below the noise floor to 0
# Values:
#	0 : Plot All Data
#	1 : Set values below noise floor to 0
#	X : Where X is any value other than 0 or 1, Plot All Data

set_floor = 1

# Average each set into one set of 1024 points

for i in range(0, int (1024*window_size)):
	# Calculate the average value for each data point
	avg_val = numpy.mean([pavg_data[i], pavg_data[i+1024], pavg_data[i+2*1024], pavg_data[i+3*1024], pavg_data[i+4*1024]])

	if set_floor == 1: # Floor is set
		if avg_val > 20: # Noise Floor value
			avg_data.append(avg_val)
		else:
			avg_data.append(0)

	else: # Floor is not set
		avg_data.append(avg_val)


##################################################
# Plotting in Frequency Domain
##################################################

# Generate the x-axis
N = 2048*window_size # number of points
T = 1.0/2048.0
xf = numpy.linspace(0.0, 1.0/(2.0*T), N//2)

# Convert to frequency instead of FFT points
center_freq = 2.483e9 # Receiver center frequency
fft_points = 1024 # Number of points in the FFT
samp_rate = 1e6 # Receiver sample rate

freq_resolution = samp_rate/fft_points # Distance between 2 FFT points
min_freq = center_freq - (samp_rate/2) # Frequency Range
max_freq = center_freq + (samp_rate/2) # Frequency range

# Might not be perfect, but it's easy
for i in range(0,1024):
	freq_axis.append((min_freq + freq_resolution*i))

# Plot the data and display it
fig = plt.figure("Spectrum Analysis")
plt.plot(freq_axis, avg_data)

plt.xlim([min_freq, max_freq])
plt.xlabel('Frequency (Hz)')
plt.title('Spectrum analysis of data obtained from GNURadio')

plt.show()