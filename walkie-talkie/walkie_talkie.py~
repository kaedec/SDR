#!/usr/bin/env python
##################################################
# Python Flow Graph
# Title: walkie_talkie
# Author: Katelyn Charbonneau & John Oleksak
# Description: Implements a "walkie-talkie" system that allows the user to switch
#  between transmit and receive modes upon button press
##################################################
# Update History
#
# 3/12/18 - Project created
# 3/14/18 - Documentation
##################################################

from gnuradio import analog			# wfm_tx and wfm_rcv
from gnuradio import audio			# microphone source/speakers sink
from gnuradio import blocks			# was used for wavfile source
from gnuradio import eng_notation
from gnuradio import filter			# used for the filter in receive mode
from gnuradio import gr
from gnuradio import uhd			# USRP sink/source
from optparse import OptionParser	# for user commands
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes	# used for the filter in receive mode
import time

##################################################
# Receive Flow Graph
##################################################

class usrp_wfm_rx_1(gr.top_block):

	def __init__(self, freq=2.483e9, samp_rate=441e3):
		gr.top_block.__init__(self)

		## Parameters
		self.freq = freq
		self.samp_rate = samp_rate

		## Variables
		self.audio_decim = audio_decim = 10

		## Blocks
		# USRP Source
		self.usrp_source_0 = uhd.usrp_source(
			",".join(("", "")),
			uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),)
		self.usrp_source_0.set_samp_rate(samp_rate)
		self.usrp_source_0.set_center_freq(freq, 0)
		self.usrp_source_0.set_gain(3, 0)
		self.usrp_source_0.set_antenna("TX/RX", 0)
		
        # Low Pass Filter
		self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
			1, samp_rate, 115e3, 30e3, firdes.WIN_HANN, 6.76))

		# Audio Sink - outputs to speakers
		self.audio_sink_0 = audio.sink(int(samp_rate/audio_decim))

		# WFM Block
		self.wfm_rcv_0 = analog.wfm_rcv(
			quad_rate=samp_rate,
            audio_decimation=audio_decim)
		
		## Connections
		self.connect(self.usrp_source_0, self.low_pass_filter_0)
		self.connect(self.low_pass_filter_0, self.wfm_rcv_0)
		self.connect(self.wfm_rcv_0, self.audio_sink_0)

##################################################
# Transmit Flow Graph
##################################################

class usrp_wfm_tx_1(gr.top_block):

	def __init__(self, freq=2.483e9, samp_rate=441e3):
		gr.top_block.__init__(self)

		## Parameters
		self.freq = freq
		self.samp_rate = samp_rate

		## Variables
		self.audio_decim = audio_decim = 10

		## Blocks
		# USRP Sink
		self.usrp_sink_0 = uhd.usrp_sink(
			",".join(("", "")),
			uhd.stream_args(
				cpu_format="fc32",
				channels=range(1),
			),)
		self.usrp_sink_0.set_samp_rate(samp_rate)
		self.usrp_sink_0.set_center_freq(freq, 0)
		self.usrp_sink_0.set_gain(3, 0)
		self.usrp_sink_0.set_antenna("TX/RX", 0)
		
		# Audio Source - input from microphone
		self.audio_source_0 = audio.source(44100, "", True)

		# WFM Block
		self.wfm_tx_0 = analog.wfm_tx(
			audio_rate=int(samp_rate/audio_decim),
			quad_rate=int(samp_rate),
			tau=75e-6,
			max_dev=75e3)
		
		## Connections
		self.connect(self.audio_source_0, self.wfm_tx_0)
		self.connect(self.wfm_tx_0, self.usrp_sink_0)

##################################################
# Main
##################################################

if __name__ == '__main__':
	rx = usrp_wfm_rx_1() # receive variable
	tx = usrp_wfm_tx_1() # transmit variable
	try:
		while True: # infinite loop - run program until user presses KeyboardInterrupt (CTRL+C)
			rx.start() # begin receiving
			raw_input('Current Mode: Receive (RX). Press Enter to change mode to Transmit (TX).')
			print("Changing mode to Transmit (TX)...\n")
			rx.stop()
			rx.wait() # stop receiving
			tx.start() # begin transmitting
			raw_input('Current Mode: Transmit (TX). Press Enter to change mode to Receive (RX).')
			print("Changing mode to Receive (RX)...\n")
			tx.stop()
			tx.wait() # stop transmitting
	except KeyboardInterrupt:
		pass
