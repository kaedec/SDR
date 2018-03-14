#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: transmit1
# Author: KC&JO
# Description: first transmit grc->python
# Generated: Mon Mar  5 15:21:45 2018
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time

class fm_tx_nogui(gr.top_block):

    def __init__(self, freq=2.483e9, samp_rate=441e3):
        gr.top_block.__init__(self, "transmit1")

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.audio_decim = audio_decim = 10

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq, 0)
        self.uhd_usrp_sink_0.set_gain(3, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/sdr/Downloads/0477.wav", True)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=int(samp_rate/audio_decim),
        	quad_rate=int(samp_rate),
        	tau=75e-6,
        	max_dev=75e3,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_tx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.analog_wfm_tx_0, 0))



    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_sink_0.set_center_freq(self.freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_audio_decim(self):
        return self.audio_decim

    def set_audio_decim(self, audio_decim):
        self.audio_decim = audio_decim

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(2.483e9),
        help="Set Default Frequency [default=%default]")
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(441e3),
        help="Set Sample Rate [default=%default]")
    (options, args) = parser.parse_args()
    tb = fm_tx_nogui(freq=options.freq, samp_rate=options.samp_rate)
    tb.start()
    raw_input('Press Enter to quit: ')
    tb.stop()
    tb.wait()
