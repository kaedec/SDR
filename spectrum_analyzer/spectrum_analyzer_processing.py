#!/usr/bin/env python
##################################################
# Python Data Processing
# Title: spectrum_analyzer_processing.py
# Author: Katelyn Charbonneau
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
# 4/25/18 - Updated with pseudo-cognitive radio capabilities
##################################################

import scipy						# Contains file reading function
import numpy						# Contains math functions
import matplotlib.pyplot as plt		# Plotting the data

center_freq = 2.483e9 	# Receiver center frequency
samp_rate = 1e6 		# Receiver sample rate
fft_points = 1024		# Number of points in the FFT
num_averages = 15.0		# Number of averages to take

pavg_data = []			# Pre-averaged snapshots
avg_data = []			# Averaged snapshots
freq_axis = []			# x-axis for plotting
open_band_start = []	# Start values for open bands
open_band_end = []		# End values for open bands

##################################################
# Data Reading, Snapshotting, and Averaging
##################################################

# Read the selected data file (gnuradio-companion writes a float data type)
# YOU WILL HAVE TO CHANGE THIS NAME TO SELECT THE DESIRED FILE
# For simplicity's sake, put the data file in the same directory as this script
DATA_FILE = "file4out.bin"

f = scipy.fromfile(open(DATA_FILE), dtype=scipy.float32)

# Variables to allow for easier troubleshooting and testing
window_size = 1
halfway_point = len(f)/2
window_start = 1/2*halfway_point+(fft_points*0) # Start at x% of the data
window_end = window_start+(fft_points*window_size*num_averages) # Take [num_averages] snapshots

# Fill pavg_data with 5 sets of fft_points number of FFT data points
for i in range(int (window_start), int (window_end)):
	pavg_data.append(f[i])

# set_floor defines whether to plot all data for testing or development
#  or to set values below the noise floor to 0
# Values:
#	0 : Plot All Data
#	1 : Set values below noise floor to 0
#	X : Where X is any value other than 0 or 1, Plot All Data

set_floor = 1

# Average each set into one set of fft_points number of points

for i in range(0, int (fft_points*window_size)):
	# Calculate the average value for each data point
	sum = 0.0
	for j in range(0, int (num_averages)):
		sum = sum + pavg_data[i+fft_points*j]
	avg_val = sum/num_averages

	if set_floor == 1: # Floor is set
		if avg_val > 15: # Noise Floor value
			avg_data.append(avg_val)
		else:
			avg_data.append(0)

	else: # Floor is not set
		avg_data.append(avg_val)


##################################################
# Plotting in Frequency Domain
##################################################

# Generate the x-axis
N = fft_points*2*window_size # number of points
T = 1.0/(fft_points*2)
xf = numpy.linspace(0.0, 1.0/(2.0*T), N//2)

# Convert x-axis from FFT points to frequency

freq_resolution = samp_rate/fft_points # Distance between 2 FFT points
min_freq = center_freq - (samp_rate/2) # Frequency Range
max_freq = center_freq + (samp_rate/2) # Frequency range

# Might not be perfect, but it's easy
for i in range(0, fft_points):
	freq_axis.append((min_freq + freq_resolution*i))

# Plot the data - graph will display later
fig = plt.figure("Spectrum Analysis")
plt.plot(freq_axis, avg_data)

plt.xlim([min_freq, max_freq])
plt.xlabel('Frequency (Hz)')
plt.title('Spectrum analysis of data obtained from GNURadio')

##################################################
# Scan Data and Determine Open Bands
##################################################

# Find values for the start and end of open bands (where there is no transmission)

for i in range(0, fft_points-1):

	# Set first start value to 0 (this may fail if there is a transmission at point at point 0)
	if i == 0:
		open_band_start.append(i)
	# Open band starts if signal goes from non-zero value to zero value
	if avg_data[i-1] != 0 and avg_data[i] == 0:
		open_band_start.append(i)

	# Open band ends if signal goes from zero value to non-zero value
	if avg_data[i+1] != 0 and avg_data[i] == 0:
		open_band_end.append(i)
	# Set last end value to the end of the FFT (this may fail is there is a transmission at that point)
	if i == fft_points-2:
		open_band_end.append(i+1)

# Calculate the sizes of the open bands

open_band_length_calc = []

for i in range(0, len(open_band_start)):
	open_band_length_calc.append(open_band_end[i] - open_band_start[i])

# Find the largest open band

max_open_band_index = open_band_length_calc.index(max(open_band_length_calc))

# Transmit at the midpoint of the largest open band and convert it to frequency

tx_point = int((open_band_end[max_open_band_index] - open_band_start[max_open_band_index])/2 + open_band_start[max_open_band_index])

tx_freq = int(min_freq + tx_point * freq_resolution)
tx_freq_print = tx_freq / 1e9

print "Selected transmit frequency: %fGHz" % tx_freq_print

# Display the plot
plt.show()
