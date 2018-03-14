#!/usr/bin/env python
# Started 3/5/2018
# First transmit python script

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from optparse import OptionParser
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
import time

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
		
		# .wav file to transmit
		self.wav_source_0 = blocks.wavfile_source(
			"/home/sdr/Downloads/0477.wav", True)

		# wfm block
		self.wfm_tx_0 = analog.wfm_tx(
			audio_rate=int(samp_rate/audio_decim),
			quad_rate=int(samp_rate),
			tau=75e-6,
			max_dev=75e3)
		
		## Connections
		self.connect(self.wav_source_0, self.wfm_tx_0)
		self.connect(self.wfm_tx_0, self.usrp_sink_0)





if __name__ == '__main__':
    tb = usrp_wfm_tx_1()
    try:
        tb.run()
    except KeyboardInterrupt:
        pass
