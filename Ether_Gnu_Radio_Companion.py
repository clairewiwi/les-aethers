#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ether
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt,QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
import ConfigParser
import epy_block_0_0
import epy_block_0_1_0
import osmosdr
import time

from gnuradio import qtgui

class Ether_Gnu_Radio_Companion(gr.top_block, Qt.QWidget):
	
    def eventFilter(self, obj, event):
        if event.type() ==  Qt.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Escape: #and self.isFullScreen():
            #self.setFullScreen(False) n'a pas cette methode
            event.accept()
            self.stop()
            self.wait()
            QtCore.QCoreApplication.quit()
            return True
        return super(Ether_Gnu_Radio_Companion, self).eventFilter(obj, event)
            
    def __init__(self):
        gr.top_block.__init__(self, "ether")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ether")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Ether_Gnu_Radio_Companion")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self._volume_cordes_saved_config = ConfigParser.ConfigParser()
        self._volume_cordes_saved_config.read('Harmonic_frequencies')
        try: volume_cordes_saved = self._volume_cordes_saved_config.getfloat('main', 'volume_cordes_slider')
        except: volume_cordes_saved = 1.
        self.volume_cordes_saved = volume_cordes_saved
        self.radio_frequency_center_menu = radio_frequency_center_menu = 0
        self.radio_frequency__delta_MHz = radio_frequency__delta_MHz = 0
        self.volume_headphone_slider = volume_headphone_slider = 0.5
        self.volume_headphone_max = volume_headphone_max = 0.5
        self.volume_cordes_slider = volume_cordes_slider = volume_cordes_saved
        self.volume_cordes_max = volume_cordes_max = 0.12
        self._time_stop_on_frequency_saved_config = ConfigParser.ConfigParser()
        self._time_stop_on_frequency_saved_config.read('Harmonic_frequencies')
        try: time_stop_on_frequency_saved = self._time_stop_on_frequency_saved_config.getfloat('main', 'time_stop_on_frequency')
        except: time_stop_on_frequency_saved = 30
        self.time_stop_on_frequency_saved = time_stop_on_frequency_saved
        self._time_between_frequencies_saved_config = ConfigParser.ConfigParser()
        self._time_between_frequencies_saved_config.read('Harmonic_frequencies')
        try: time_between_frequencies_saved = self._time_between_frequencies_saved_config.getint('main', 'time_between_frequencies')
        except: time_between_frequencies_saved = 30
        self.time_between_frequencies_saved = time_between_frequencies_saved
        self.radio_frequency_delta = radio_frequency_delta = radio_frequency__delta_MHz * 1e6
        self.radio_frequency_center = radio_frequency_center = radio_frequency_center_menu
        self._corde8_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde8_frequence5_saved = self._corde8_frequence5_saved_config.getfloat('main', 'corde8_frequence5')
        except: corde8_frequence5_saved = 50
        self.corde8_frequence5_saved = corde8_frequence5_saved
        self._corde8_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde8_frequence4_saved = self._corde8_frequence4_saved_config.getfloat('main', 'corde8_frequence4')
        except: corde8_frequence4_saved = 40
        self.corde8_frequence4_saved = corde8_frequence4_saved
        self._corde8_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde8_frequence3_saved = self._corde8_frequence3_saved_config.getfloat('main', 'corde8_frequence3')
        except: corde8_frequence3_saved = 30
        self.corde8_frequence3_saved = corde8_frequence3_saved
        self._corde8_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde8_frequence2_saved = self._corde8_frequence2_saved_config.getfloat('main', 'corde8_frequence2')
        except: corde8_frequence2_saved = 20
        self.corde8_frequence2_saved = corde8_frequence2_saved
        self._corde8_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde8_frequence1_saved = self._corde8_frequence1_saved_config.getfloat('main', 'corde8_frequence1')
        except: corde8_frequence1_saved = 10
        self.corde8_frequence1_saved = corde8_frequence1_saved
        self._corde7_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde7_frequence5_saved = self._corde7_frequence5_saved_config.getfloat('main', 'corde7_frequence5')
        except: corde7_frequence5_saved = 50
        self.corde7_frequence5_saved = corde7_frequence5_saved
        self._corde7_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde7_frequence4_saved = self._corde7_frequence4_saved_config.getfloat('main', 'corde7_frequence4')
        except: corde7_frequence4_saved = 40
        self.corde7_frequence4_saved = corde7_frequence4_saved
        self._corde7_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde7_frequence3_saved = self._corde7_frequence3_saved_config.getfloat('main', 'corde7_frequence3')
        except: corde7_frequence3_saved = 30
        self.corde7_frequence3_saved = corde7_frequence3_saved
        self._corde7_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde7_frequence2_saved = self._corde7_frequence2_saved_config.getfloat('main', 'corde7_frequence2')
        except: corde7_frequence2_saved = 20
        self.corde7_frequence2_saved = corde7_frequence2_saved
        self._corde7_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde7_frequence1_saved = self._corde7_frequence1_saved_config.getfloat('main', 'corde7_frequence1')
        except: corde7_frequence1_saved = 10
        self.corde7_frequence1_saved = corde7_frequence1_saved
        self._corde6_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde6_frequence5_saved = self._corde6_frequence5_saved_config.getfloat('main', 'corde6_frequence5')
        except: corde6_frequence5_saved = 50
        self.corde6_frequence5_saved = corde6_frequence5_saved
        self._corde6_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde6_frequence4_saved = self._corde6_frequence4_saved_config.getfloat('main', 'corde6_frequence4')
        except: corde6_frequence4_saved = 40
        self.corde6_frequence4_saved = corde6_frequence4_saved
        self._corde6_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde6_frequence3_saved = self._corde6_frequence3_saved_config.getfloat('main', 'corde6_frequence3')
        except: corde6_frequence3_saved = 30
        self.corde6_frequence3_saved = corde6_frequence3_saved
        self._corde6_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde6_frequence2_saved = self._corde6_frequence2_saved_config.getfloat('main', 'corde6_frequence2')
        except: corde6_frequence2_saved = 20
        self.corde6_frequence2_saved = corde6_frequence2_saved
        self._corde6_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde6_frequence1_saved = self._corde6_frequence1_saved_config.getfloat('main', 'corde6_frequence1')
        except: corde6_frequence1_saved = 10
        self.corde6_frequence1_saved = corde6_frequence1_saved
        self._corde5_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde5_frequence5_saved = self._corde5_frequence5_saved_config.getfloat('main', 'corde5_frequence5')
        except: corde5_frequence5_saved = 50
        self.corde5_frequence5_saved = corde5_frequence5_saved
        self._corde5_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde5_frequence4_saved = self._corde5_frequence4_saved_config.getfloat('main', 'corde5_frequence4')
        except: corde5_frequence4_saved = 40
        self.corde5_frequence4_saved = corde5_frequence4_saved
        self._corde5_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde5_frequence3_saved = self._corde5_frequence3_saved_config.getfloat('main', 'corde5_frequence3')
        except: corde5_frequence3_saved = 30
        self.corde5_frequence3_saved = corde5_frequence3_saved
        self._corde5_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde5_frequence2_saved = self._corde5_frequence2_saved_config.getfloat('main', 'corde5_frequence2')
        except: corde5_frequence2_saved = 20
        self.corde5_frequence2_saved = corde5_frequence2_saved
        self._corde5_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde5_frequence1_saved = self._corde5_frequence1_saved_config.getfloat('main', 'corde5_frequence1')
        except: corde5_frequence1_saved = 10
        self.corde5_frequence1_saved = corde5_frequence1_saved
        self._corde4_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde4_frequence5_saved = self._corde4_frequence5_saved_config.getfloat('main', 'corde4_frequence5')
        except: corde4_frequence5_saved = 50
        self.corde4_frequence5_saved = corde4_frequence5_saved
        self._corde4_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde4_frequence4_saved = self._corde4_frequence4_saved_config.getfloat('main', 'corde4_frequence4')
        except: corde4_frequence4_saved = 40
        self.corde4_frequence4_saved = corde4_frequence4_saved
        self._corde4_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde4_frequence3_saved = self._corde4_frequence3_saved_config.getfloat('main', 'corde4_frequence3')
        except: corde4_frequence3_saved = 30
        self.corde4_frequence3_saved = corde4_frequence3_saved
        self._corde4_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde4_frequence2_saved = self._corde4_frequence2_saved_config.getfloat('main', 'corde4_frequence2')
        except: corde4_frequence2_saved = 20
        self.corde4_frequence2_saved = corde4_frequence2_saved
        self._corde3_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde3_frequence5_saved = self._corde3_frequence5_saved_config.getfloat('main', 'corde3_frequence5')
        except: corde3_frequence5_saved = 50
        self.corde3_frequence5_saved = corde3_frequence5_saved
        self._corde3_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde3_frequence4_saved = self._corde3_frequence4_saved_config.getfloat('main', 'corde3_frequence4')
        except: corde3_frequence4_saved = 40
        self.corde3_frequence4_saved = corde3_frequence4_saved
        self._corde3_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde3_frequence3_saved = self._corde3_frequence3_saved_config.getfloat('main', 'corde3_frequence3')
        except: corde3_frequence3_saved = 30
        self.corde3_frequence3_saved = corde3_frequence3_saved
        self._corde3_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde3_frequence2_saved = self._corde3_frequence2_saved_config.getfloat('main', 'corde3_frequence2')
        except: corde3_frequence2_saved = 20
        self.corde3_frequence2_saved = corde3_frequence2_saved
        self._corde3_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde3_frequence1_saved = self._corde3_frequence1_saved_config.getfloat('main', 'corde3_frequence1')
        except: corde3_frequence1_saved = 10
        self.corde3_frequence1_saved = corde3_frequence1_saved
        self._corde2_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde2_frequence5_saved = self._corde2_frequence5_saved_config.getfloat('main', 'corde2_frequence5')
        except: corde2_frequence5_saved = 50
        self.corde2_frequence5_saved = corde2_frequence5_saved
        self._corde2_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde2_frequence4_saved = self._corde2_frequence4_saved_config.getfloat('main', 'corde2_frequence4')
        except: corde2_frequence4_saved = 40
        self.corde2_frequence4_saved = corde2_frequence4_saved
        self._corde2_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde2_frequence3_saved = self._corde2_frequence3_saved_config.getfloat('main', 'corde2_frequence3')
        except: corde2_frequence3_saved = 30
        self.corde2_frequence3_saved = corde2_frequence3_saved
        self._corde2_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde2_frequence2_saved = self._corde2_frequence2_saved_config.getfloat('main', 'corde2_frequence2')
        except: corde2_frequence2_saved = 20
        self.corde2_frequence2_saved = corde2_frequence2_saved
        self._corde2_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde2_frequence1_saved = self._corde2_frequence1_saved_config.getfloat('main', 'corde2_frequence1')
        except: corde2_frequence1_saved = 10
        self.corde2_frequence1_saved = corde2_frequence1_saved
        self._corde1_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence5_saved_config.read('Harmonic_frequencies')
        try: corde1_frequence5_saved = self._corde1_frequence5_saved_config.getfloat('main', 'corde1_frequence5')
        except: corde1_frequence5_saved = 50
        self.corde1_frequence5_saved = corde1_frequence5_saved
        self._corde1_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence4_saved_config.read('Harmonic_frequencies')
        try: corde1_frequence4_saved = self._corde1_frequence4_saved_config.getfloat('main', 'corde1_frequence4')
        except: corde1_frequence4_saved = 40
        self.corde1_frequence4_saved = corde1_frequence4_saved
        self._corde1_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence3_saved_config.read('Harmonic_frequencies')
        try: corde1_frequence3_saved = self._corde1_frequence3_saved_config.getfloat('main', 'corde1_frequence3')
        except: corde1_frequence3_saved = 30
        self.corde1_frequence3_saved = corde1_frequence3_saved
        self._corde1_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence2_saved_config.read('Harmonic_frequencies')
        try: corde1_frequence2_saved = self._corde1_frequence2_saved_config.getfloat('main', 'corde1_frequence2')
        except: corde1_frequence2_saved = 20
        self.corde1_frequence2_saved = corde1_frequence2_saved
        self._corde1_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde1_frequence1_saved = self._corde1_frequence1_saved_config.getfloat('main', 'corde1_frequence1')
        except: corde1_frequence1_saved = 10
        self.corde1_frequence1_saved = corde1_frequence1_saved
        self.audio_sample_rate = audio_sample_rate = 24000
        self.WBFM_Receive_PLL_Audio_Decimation = WBFM_Receive_PLL_Audio_Decimation = 16
        self.Low_Pass_Filter_Decimation = Low_Pass_Filter_Decimation = 2
        self.volume_headphone = volume_headphone = volume_headphone_slider * volume_headphone_max
        self.volume_cordes = volume_cordes = volume_cordes_slider * volume_cordes_max
        self.time_stop_on_frequency = time_stop_on_frequency = time_stop_on_frequency_saved
        self.time_between_frequencies = time_between_frequencies = time_between_frequencies_saved
        self.radio_scann = radio_scann = True
        self.radio_sample_rate = radio_sample_rate = audio_sample_rate*WBFM_Receive_PLL_Audio_Decimation*Low_Pass_Filter_Decimation
        self.radio_on_cordes = radio_on_cordes = True
        self.corde8_frequence5 = corde8_frequence5 = corde8_frequence5_saved
        self.corde8_frequence4 = corde8_frequence4 = corde8_frequence4_saved
        self.corde8_frequence3 = corde8_frequence3 = corde8_frequence3_saved
        self.corde8_frequence2 = corde8_frequence2 = corde8_frequence2_saved
        self.corde8_frequence1 = corde8_frequence1 = corde8_frequence1_saved
        self.corde8_amplitude5 = corde8_amplitude5 = False
        self.corde8_amplitude4 = corde8_amplitude4 = False
        self.corde8_amplitude3 = corde8_amplitude3 = False
        self.corde8_amplitude2 = corde8_amplitude2 = False
        self.corde8_amplitude1 = corde8_amplitude1 = False
        self.corde7_frequence5 = corde7_frequence5 = corde7_frequence5_saved
        self.corde7_frequence4 = corde7_frequence4 = corde7_frequence4_saved
        self.corde7_frequence3 = corde7_frequence3 = corde7_frequence3_saved
        self.corde7_frequence2 = corde7_frequence2 = corde7_frequence2_saved
        self.corde7_frequence1 = corde7_frequence1 = corde7_frequence1_saved
        self.corde7_amplitude5 = corde7_amplitude5 = False
        self.corde7_amplitude4 = corde7_amplitude4 = False
        self.corde7_amplitude3 = corde7_amplitude3 = False
        self.corde7_amplitude2 = corde7_amplitude2 = False
        self.corde7_amplitude1 = corde7_amplitude1 = False
        self.corde6_frequence5 = corde6_frequence5 = corde6_frequence5_saved
        self.corde6_frequence4 = corde6_frequence4 = corde6_frequence4_saved
        self.corde6_frequence3 = corde6_frequence3 = corde6_frequence3_saved
        self.corde6_frequence2 = corde6_frequence2 = corde6_frequence2_saved
        self.corde6_frequence1 = corde6_frequence1 = corde6_frequence1_saved
        self.corde6_amplitude5 = corde6_amplitude5 = False
        self.corde6_amplitude4 = corde6_amplitude4 = False
        self.corde6_amplitude3 = corde6_amplitude3 = False
        self.corde6_amplitude2 = corde6_amplitude2 = False
        self.corde6_amplitude1 = corde6_amplitude1 = False
        self.corde5_frequence5 = corde5_frequence5 = corde5_frequence5_saved
        self.corde5_frequence4 = corde5_frequence4 = corde5_frequence4_saved
        self.corde5_frequence3 = corde5_frequence3 = corde5_frequence3_saved
        self.corde5_frequence2 = corde5_frequence2 = corde5_frequence2_saved
        self.corde5_frequence1 = corde5_frequence1 = corde5_frequence1_saved
        self.corde5_amplitude5 = corde5_amplitude5 = False
        self.corde5_amplitude4 = corde5_amplitude4 = False
        self.corde5_amplitude3 = corde5_amplitude3 = False
        self.corde5_amplitude2 = corde5_amplitude2 = False
        self.corde5_amplitude1 = corde5_amplitude1 = False
        self.corde4_frequence5 = corde4_frequence5 = corde4_frequence5_saved
        self.corde4_frequence4 = corde4_frequence4 = corde4_frequence4_saved
        self.corde4_frequence3 = corde4_frequence3 = corde4_frequence3_saved
        self.corde4_frequence2 = corde4_frequence2 = corde4_frequence2_saved
        self._corde4_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence1_saved_config.read('Harmonic_frequencies')
        try: corde4_frequence1_saved = self._corde4_frequence1_saved_config.getfloat('main', 'corde4_frequence1')
        except: corde4_frequence1_saved = 10
        self.corde4_frequence1_saved = corde4_frequence1_saved
        self.corde4_frequence1 = corde4_frequence1 = corde1_frequence1_saved
        self.corde4_amplitude5 = corde4_amplitude5 = False
        self.corde4_amplitude4 = corde4_amplitude4 = False
        self.corde4_amplitude3 = corde4_amplitude3 = False
        self.corde4_amplitude2 = corde4_amplitude2 = False
        self.corde4_amplitude1 = corde4_amplitude1 = False
        self.corde3_frequence5 = corde3_frequence5 = corde3_frequence5_saved
        self.corde3_frequence4 = corde3_frequence4 = corde3_frequence4_saved
        self.corde3_frequence3 = corde3_frequence3 = corde3_frequence3_saved
        self.corde3_frequence2 = corde3_frequence2 = corde3_frequence2_saved
        self.corde3_frequence1 = corde3_frequence1 = corde3_frequence1_saved
        self.corde3_amplitude5 = corde3_amplitude5 = False
        self.corde3_amplitude4 = corde3_amplitude4 = False
        self.corde3_amplitude3 = corde3_amplitude3 = False
        self.corde3_amplitude2 = corde3_amplitude2 = False
        self.corde3_amplitude1 = corde3_amplitude1 = False
        self.corde2_frequence5 = corde2_frequence5 = corde2_frequence5_saved
        self.corde2_frequence4 = corde2_frequence4 = corde2_frequence4_saved
        self.corde2_frequence3 = corde2_frequence3 = corde2_frequence3_saved
        self.corde2_frequence2 = corde2_frequence2 = corde2_frequence2_saved
        self.corde2_frequence1 = corde2_frequence1 = corde2_frequence1_saved
        self.corde2_amplitude5 = corde2_amplitude5 = False
        self.corde2_amplitude4 = corde2_amplitude4 = False
        self.corde2_amplitude3 = corde2_amplitude3 = False
        self.corde2_amplitude2 = corde2_amplitude2 = False
        self.corde2_amplitude1 = corde2_amplitude1 = False
        self.corde1_frequence5 = corde1_frequence5 = corde1_frequence5_saved
        self.corde1_frequence4 = corde1_frequence4 = corde1_frequence4_saved
        self.corde1_frequence3 = corde1_frequence3 = corde1_frequence3_saved
        self.corde1_frequence2 = corde1_frequence2 = corde1_frequence2_saved
        self.corde1_frequence1 = corde1_frequence1 = corde1_frequence1_saved
        self.corde1_amplitude5 = corde1_amplitude5 = False
        self.corde1_amplitude4 = corde1_amplitude4 = False
        self.corde1_amplitude3 = corde1_amplitude3 = False
        self.corde1_amplitude2 = corde1_amplitude2 = False
        self.corde1_amplitude1 = corde1_amplitude1 = False
        self.WBFM_Receive_PLL_Audio_Decimation_0 = WBFM_Receive_PLL_Audio_Decimation_0 = radio_frequency__delta_MHz * 1e6
        self.Low_Pass_Filter_cut_of_frequency = Low_Pass_Filter_cut_of_frequency = 9e4
        self.Low_Pass_Filter_Transition_Width = Low_Pass_Filter_Transition_Width = 1e4
        self.Frequency = Frequency = str(round((radio_frequency_center+radio_frequency_delta)*1e-6,3))+ " Mhz"
        self.FFT_size = FFT_size = 1024

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_tab_widget = Qt.QTabWidget()
        self.qtgui_tab_widget_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_0)
        self.qtgui_tab_widget_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_0.addLayout(self.qtgui_tab_widget_grid_layout_0)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_0, 'Screen')
        self.qtgui_tab_widget_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_1)
        self.qtgui_tab_widget_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_1.addLayout(self.qtgui_tab_widget_grid_layout_1)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_1, 'Radio')
        self.qtgui_tab_widget_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_2)
        self.qtgui_tab_widget_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_2.addLayout(self.qtgui_tab_widget_grid_layout_2)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_2, 'Cordes')
        self.qtgui_tab_widget_widget_3 = Qt.QWidget()
        self.qtgui_tab_widget_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_widget_3)
        self.qtgui_tab_widget_grid_layout_3 = Qt.QGridLayout()
        self.qtgui_tab_widget_layout_3.addLayout(self.qtgui_tab_widget_grid_layout_3)
        self.qtgui_tab_widget.addTab(self.qtgui_tab_widget_widget_3, 'Curves')
        self.top_grid_layout.addWidget(self.qtgui_tab_widget)
        _radio_on_cordes_check_box = Qt.QCheckBox('Radio on Cordes')
        self._radio_on_cordes_choices = {True: True, False: False}
        self._radio_on_cordes_choices_inv = dict((v,k) for k,v in self._radio_on_cordes_choices.items())
        self._radio_on_cordes_callback = lambda i: Qt.QMetaObject.invokeMethod(_radio_on_cordes_check_box, "setChecked", Qt.Q_ARG("bool", self._radio_on_cordes_choices_inv[i]))
        self._radio_on_cordes_callback(self.radio_on_cordes)
        _radio_on_cordes_check_box.stateChanged.connect(lambda i: self.set_radio_on_cordes(self._radio_on_cordes_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_radio_on_cordes_check_box, 0, 0, 1, 1)
        for r in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._radio_frequency__delta_MHz_range = Range(-1, 1, 0.001, 0, 200)
        self._radio_frequency__delta_MHz_win = RangeWidget(self._radio_frequency__delta_MHz_range, self.set_radio_frequency__delta_MHz, 'Delta', "slider", float)
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._radio_frequency__delta_MHz_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self._corde8_frequence5_range = Range(1, 200, 0.01, corde8_frequence5_saved, 200)
        self._corde8_frequence5_win = RangeWidget(self._corde8_frequence5_range, self.set_corde8_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde8_frequence5_win, 16, 4, 1, 1)
        for r in range(16, 17):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde8_frequence4_range = Range(1, 200, 0.01, corde8_frequence4_saved, 200)
        self._corde8_frequence4_win = RangeWidget(self._corde8_frequence4_range, self.set_corde8_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde8_frequence4_win, 16, 3, 1, 1)
        for r in range(16, 17):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde8_frequence3_range = Range(1, 200, 0.01, corde8_frequence3_saved, 200)
        self._corde8_frequence3_win = RangeWidget(self._corde8_frequence3_range, self.set_corde8_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde8_frequence3_win, 16, 2, 1, 1)
        for r in range(16, 17):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde8_frequence2_range = Range(1, 200, 0.01, corde8_frequence2_saved, 200)
        self._corde8_frequence2_win = RangeWidget(self._corde8_frequence2_range, self.set_corde8_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde8_frequence2_win, 16, 1, 1, 1)
        for r in range(16, 17):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde8_frequence1_range = Range(1, 200, 0.01, corde8_frequence1_saved, 200)
        self._corde8_frequence1_win = RangeWidget(self._corde8_frequence1_range, self.set_corde8_frequence1, 'Corde 8 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde8_frequence1_win, 16, 0, 1, 1)
        for r in range(16, 17):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde8_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde8_amplitude5_choices = {True: True, False: False}
        self._corde8_amplitude5_choices_inv = dict((v,k) for k,v in self._corde8_amplitude5_choices.items())
        self._corde8_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde8_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde8_amplitude5_choices_inv[i]))
        self._corde8_amplitude5_callback(self.corde8_amplitude5)
        _corde8_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde8_amplitude5(self._corde8_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde8_amplitude5_check_box, 15, 4, 1, 1)
        for r in range(15, 16):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde8_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde8_amplitude4_choices = {True: True, False: False}
        self._corde8_amplitude4_choices_inv = dict((v,k) for k,v in self._corde8_amplitude4_choices.items())
        self._corde8_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde8_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde8_amplitude4_choices_inv[i]))
        self._corde8_amplitude4_callback(self.corde8_amplitude4)
        _corde8_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde8_amplitude4(self._corde8_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde8_amplitude4_check_box, 15, 3, 1, 1)
        for r in range(15, 16):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde8_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde8_amplitude3_choices = {True: True, False: False}
        self._corde8_amplitude3_choices_inv = dict((v,k) for k,v in self._corde8_amplitude3_choices.items())
        self._corde8_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde8_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde8_amplitude3_choices_inv[i]))
        self._corde8_amplitude3_callback(self.corde8_amplitude3)
        _corde8_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde8_amplitude3(self._corde8_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde8_amplitude3_check_box, 15, 2, 1, 1)
        for r in range(15, 16):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde8_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde8_amplitude2_choices = {True: True, False: False}
        self._corde8_amplitude2_choices_inv = dict((v,k) for k,v in self._corde8_amplitude2_choices.items())
        self._corde8_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde8_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde8_amplitude2_choices_inv[i]))
        self._corde8_amplitude2_callback(self.corde8_amplitude2)
        _corde8_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde8_amplitude2(self._corde8_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde8_amplitude2_check_box, 15, 1, 1, 1)
        for r in range(15, 16):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde8_amplitude1_check_box = Qt.QCheckBox('Corde 8 Amplitude 1')
        self._corde8_amplitude1_choices = {True: True, False: False}
        self._corde8_amplitude1_choices_inv = dict((v,k) for k,v in self._corde8_amplitude1_choices.items())
        self._corde8_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde8_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde8_amplitude1_choices_inv[i]))
        self._corde8_amplitude1_callback(self.corde8_amplitude1)
        _corde8_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde8_amplitude1(self._corde8_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde8_amplitude1_check_box, 15, 0, 1, 1)
        for r in range(15, 16):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde7_frequence5_range = Range(1, 200, 0.01, corde7_frequence5_saved, 200)
        self._corde7_frequence5_win = RangeWidget(self._corde7_frequence5_range, self.set_corde7_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde7_frequence5_win, 14, 4, 1, 1)
        for r in range(14, 15):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde7_frequence4_range = Range(1, 200, 0.01, corde7_frequence4_saved, 200)
        self._corde7_frequence4_win = RangeWidget(self._corde7_frequence4_range, self.set_corde7_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde7_frequence4_win, 14, 3, 1, 1)
        for r in range(14, 15):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde7_frequence3_range = Range(1, 200, 0.01, corde7_frequence3_saved, 200)
        self._corde7_frequence3_win = RangeWidget(self._corde7_frequence3_range, self.set_corde7_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde7_frequence3_win, 14, 2, 1, 1)
        for r in range(14, 15):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde7_frequence2_range = Range(1, 200, 0.01, corde7_frequence2_saved, 200)
        self._corde7_frequence2_win = RangeWidget(self._corde7_frequence2_range, self.set_corde7_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde7_frequence2_win, 14, 1, 1, 1)
        for r in range(14, 15):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde7_frequence1_range = Range(1, 200, 0.01, corde7_frequence1_saved, 200)
        self._corde7_frequence1_win = RangeWidget(self._corde7_frequence1_range, self.set_corde7_frequence1, 'Corde 7 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde7_frequence1_win, 14, 0, 1, 1)
        for r in range(14, 15):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde7_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde7_amplitude5_choices = {True: True, False: False}
        self._corde7_amplitude5_choices_inv = dict((v,k) for k,v in self._corde7_amplitude5_choices.items())
        self._corde7_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde7_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde7_amplitude5_choices_inv[i]))
        self._corde7_amplitude5_callback(self.corde7_amplitude5)
        _corde7_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde7_amplitude5(self._corde7_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde7_amplitude5_check_box, 13, 4, 1, 1)
        for r in range(13, 14):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde7_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde7_amplitude4_choices = {True: True, False: False}
        self._corde7_amplitude4_choices_inv = dict((v,k) for k,v in self._corde7_amplitude4_choices.items())
        self._corde7_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde7_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde7_amplitude4_choices_inv[i]))
        self._corde7_amplitude4_callback(self.corde7_amplitude4)
        _corde7_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde7_amplitude4(self._corde7_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde7_amplitude4_check_box, 13, 3, 1, 1)
        for r in range(13, 14):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde7_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde7_amplitude3_choices = {True: True, False: False}
        self._corde7_amplitude3_choices_inv = dict((v,k) for k,v in self._corde7_amplitude3_choices.items())
        self._corde7_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde7_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde7_amplitude3_choices_inv[i]))
        self._corde7_amplitude3_callback(self.corde7_amplitude3)
        _corde7_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde7_amplitude3(self._corde7_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde7_amplitude3_check_box, 13, 2, 1, 1)
        for r in range(13, 14):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde7_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde7_amplitude2_choices = {True: True, False: False}
        self._corde7_amplitude2_choices_inv = dict((v,k) for k,v in self._corde7_amplitude2_choices.items())
        self._corde7_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde7_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde7_amplitude2_choices_inv[i]))
        self._corde7_amplitude2_callback(self.corde7_amplitude2)
        _corde7_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde7_amplitude2(self._corde7_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde7_amplitude2_check_box, 13, 1, 1, 1)
        for r in range(13, 14):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde7_amplitude1_check_box = Qt.QCheckBox('Corde 7 Amplitude 1')
        self._corde7_amplitude1_choices = {True: True, False: False}
        self._corde7_amplitude1_choices_inv = dict((v,k) for k,v in self._corde7_amplitude1_choices.items())
        self._corde7_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde7_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde7_amplitude1_choices_inv[i]))
        self._corde7_amplitude1_callback(self.corde7_amplitude1)
        _corde7_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde7_amplitude1(self._corde7_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde7_amplitude1_check_box, 13, 0, 1, 1)
        for r in range(13, 14):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde6_frequence5_range = Range(1, 200, 0.01, corde6_frequence5_saved, 200)
        self._corde6_frequence5_win = RangeWidget(self._corde6_frequence5_range, self.set_corde6_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde6_frequence5_win, 12, 4, 1, 1)
        for r in range(12, 13):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde6_frequence4_range = Range(1, 200, 0.01, corde6_frequence4_saved, 200)
        self._corde6_frequence4_win = RangeWidget(self._corde6_frequence4_range, self.set_corde6_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde6_frequence4_win, 12, 3, 1, 1)
        for r in range(12, 13):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde6_frequence3_range = Range(1, 200, 0.01, corde6_frequence3_saved, 200)
        self._corde6_frequence3_win = RangeWidget(self._corde6_frequence3_range, self.set_corde6_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde6_frequence3_win, 12, 2, 1, 1)
        for r in range(12, 13):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde6_frequence2_range = Range(1, 200, 0.01, corde6_frequence2_saved, 200)
        self._corde6_frequence2_win = RangeWidget(self._corde6_frequence2_range, self.set_corde6_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde6_frequence2_win, 12, 1, 1, 1)
        for r in range(12, 13):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde6_frequence1_range = Range(1, 200, 0.01, corde6_frequence1_saved, 200)
        self._corde6_frequence1_win = RangeWidget(self._corde6_frequence1_range, self.set_corde6_frequence1, 'Corde 6 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde6_frequence1_win, 12, 0, 1, 1)
        for r in range(12, 13):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde6_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde6_amplitude5_choices = {True: True, False: False}
        self._corde6_amplitude5_choices_inv = dict((v,k) for k,v in self._corde6_amplitude5_choices.items())
        self._corde6_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde6_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde6_amplitude5_choices_inv[i]))
        self._corde6_amplitude5_callback(self.corde6_amplitude5)
        _corde6_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde6_amplitude5(self._corde6_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde6_amplitude5_check_box, 11, 4, 1, 1)
        for r in range(11, 12):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde6_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde6_amplitude4_choices = {True: True, False: False}
        self._corde6_amplitude4_choices_inv = dict((v,k) for k,v in self._corde6_amplitude4_choices.items())
        self._corde6_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde6_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde6_amplitude4_choices_inv[i]))
        self._corde6_amplitude4_callback(self.corde6_amplitude4)
        _corde6_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde6_amplitude4(self._corde6_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde6_amplitude4_check_box, 11, 3, 1, 1)
        for r in range(11, 12):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde6_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde6_amplitude3_choices = {True: True, False: False}
        self._corde6_amplitude3_choices_inv = dict((v,k) for k,v in self._corde6_amplitude3_choices.items())
        self._corde6_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde6_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde6_amplitude3_choices_inv[i]))
        self._corde6_amplitude3_callback(self.corde6_amplitude3)
        _corde6_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde6_amplitude3(self._corde6_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde6_amplitude3_check_box, 11, 2, 1, 1)
        for r in range(11, 12):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde6_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde6_amplitude2_choices = {True: True, False: False}
        self._corde6_amplitude2_choices_inv = dict((v,k) for k,v in self._corde6_amplitude2_choices.items())
        self._corde6_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde6_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde6_amplitude2_choices_inv[i]))
        self._corde6_amplitude2_callback(self.corde6_amplitude2)
        _corde6_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde6_amplitude2(self._corde6_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde6_amplitude2_check_box, 11, 1, 1, 1)
        for r in range(11, 12):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde6_amplitude1_check_box = Qt.QCheckBox('Corde 6 Amplitude 1')
        self._corde6_amplitude1_choices = {True: True, False: False}
        self._corde6_amplitude1_choices_inv = dict((v,k) for k,v in self._corde6_amplitude1_choices.items())
        self._corde6_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde6_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde6_amplitude1_choices_inv[i]))
        self._corde6_amplitude1_callback(self.corde6_amplitude1)
        _corde6_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde6_amplitude1(self._corde6_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde6_amplitude1_check_box, 11, 0, 1, 1)
        for r in range(11, 12):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde5_frequence5_range = Range(1, 200, 0.01, corde5_frequence5_saved, 200)
        self._corde5_frequence5_win = RangeWidget(self._corde5_frequence5_range, self.set_corde5_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde5_frequence5_win, 10, 4, 1, 1)
        for r in range(10, 11):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde5_frequence4_range = Range(1, 200, 0.01, corde5_frequence4_saved, 200)
        self._corde5_frequence4_win = RangeWidget(self._corde5_frequence4_range, self.set_corde5_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde5_frequence4_win, 10, 3, 1, 1)
        for r in range(10, 11):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde5_frequence3_range = Range(1, 200, 0.01, corde5_frequence3_saved, 200)
        self._corde5_frequence3_win = RangeWidget(self._corde5_frequence3_range, self.set_corde5_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde5_frequence3_win, 10, 2, 1, 1)
        for r in range(10, 11):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde5_frequence2_range = Range(1, 200, 0.01, corde5_frequence2_saved, 200)
        self._corde5_frequence2_win = RangeWidget(self._corde5_frequence2_range, self.set_corde5_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde5_frequence2_win, 10, 1, 1, 1)
        for r in range(10, 11):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde5_frequence1_range = Range(1, 200, 0.01, corde5_frequence1_saved, 200)
        self._corde5_frequence1_win = RangeWidget(self._corde5_frequence1_range, self.set_corde5_frequence1, 'Corde 5 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde5_frequence1_win, 10, 0, 1, 1)
        for r in range(10, 11):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde5_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde5_amplitude5_choices = {True: True, False: False}
        self._corde5_amplitude5_choices_inv = dict((v,k) for k,v in self._corde5_amplitude5_choices.items())
        self._corde5_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde5_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde5_amplitude5_choices_inv[i]))
        self._corde5_amplitude5_callback(self.corde5_amplitude5)
        _corde5_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde5_amplitude5(self._corde5_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde5_amplitude5_check_box, 9, 4, 1, 1)
        for r in range(9, 10):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde5_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde5_amplitude4_choices = {True: True, False: False}
        self._corde5_amplitude4_choices_inv = dict((v,k) for k,v in self._corde5_amplitude4_choices.items())
        self._corde5_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde5_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde5_amplitude4_choices_inv[i]))
        self._corde5_amplitude4_callback(self.corde5_amplitude4)
        _corde5_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde5_amplitude4(self._corde5_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde5_amplitude4_check_box, 9, 3, 1, 1)
        for r in range(9, 10):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde5_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde5_amplitude3_choices = {True: True, False: False}
        self._corde5_amplitude3_choices_inv = dict((v,k) for k,v in self._corde5_amplitude3_choices.items())
        self._corde5_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde5_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde5_amplitude3_choices_inv[i]))
        self._corde5_amplitude3_callback(self.corde5_amplitude3)
        _corde5_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde5_amplitude3(self._corde5_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde5_amplitude3_check_box, 9, 2, 1, 1)
        for r in range(9, 10):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde5_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde5_amplitude2_choices = {True: True, False: False}
        self._corde5_amplitude2_choices_inv = dict((v,k) for k,v in self._corde5_amplitude2_choices.items())
        self._corde5_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde5_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde5_amplitude2_choices_inv[i]))
        self._corde5_amplitude2_callback(self.corde5_amplitude2)
        _corde5_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde5_amplitude2(self._corde5_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde5_amplitude2_check_box, 9, 1, 1, 1)
        for r in range(9, 10):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde5_amplitude1_check_box = Qt.QCheckBox('Corde 5 Amplitude 1')
        self._corde5_amplitude1_choices = {True: True, False: False}
        self._corde5_amplitude1_choices_inv = dict((v,k) for k,v in self._corde5_amplitude1_choices.items())
        self._corde5_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde5_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde5_amplitude1_choices_inv[i]))
        self._corde5_amplitude1_callback(self.corde5_amplitude1)
        _corde5_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde5_amplitude1(self._corde5_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde5_amplitude1_check_box, 9, 0, 1, 1)
        for r in range(9, 10):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde4_frequence5_range = Range(1, 200, 0.01, corde4_frequence5_saved, 200)
        self._corde4_frequence5_win = RangeWidget(self._corde4_frequence5_range, self.set_corde4_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde4_frequence5_win, 8, 4, 1, 1)
        for r in range(8, 9):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde4_frequence4_range = Range(1, 200, 0.01, corde4_frequence4_saved, 200)
        self._corde4_frequence4_win = RangeWidget(self._corde4_frequence4_range, self.set_corde4_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde4_frequence4_win, 8, 3, 1, 1)
        for r in range(8, 9):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde4_frequence3_range = Range(1, 200, 0.01, corde4_frequence3_saved, 200)
        self._corde4_frequence3_win = RangeWidget(self._corde4_frequence3_range, self.set_corde4_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde4_frequence3_win, 8, 2, 1, 1)
        for r in range(8, 9):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde4_frequence2_range = Range(1, 200, 0.01, corde4_frequence2_saved, 200)
        self._corde4_frequence2_win = RangeWidget(self._corde4_frequence2_range, self.set_corde4_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde4_frequence2_win, 8, 1, 1, 1)
        for r in range(8, 9):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde4_frequence1_range = Range(1, 200, 0.01, corde1_frequence1_saved, 200)
        self._corde4_frequence1_win = RangeWidget(self._corde4_frequence1_range, self.set_corde4_frequence1, 'Corde 4 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde4_frequence1_win, 8, 0, 1, 1)
        for r in range(8, 9):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde4_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde4_amplitude5_choices = {True: True, False: False}
        self._corde4_amplitude5_choices_inv = dict((v,k) for k,v in self._corde4_amplitude5_choices.items())
        self._corde4_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde4_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde4_amplitude5_choices_inv[i]))
        self._corde4_amplitude5_callback(self.corde4_amplitude5)
        _corde4_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde4_amplitude5(self._corde4_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde4_amplitude5_check_box, 7, 4, 1, 1)
        for r in range(7, 8):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde4_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde4_amplitude4_choices = {True: True, False: False}
        self._corde4_amplitude4_choices_inv = dict((v,k) for k,v in self._corde4_amplitude4_choices.items())
        self._corde4_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde4_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde4_amplitude4_choices_inv[i]))
        self._corde4_amplitude4_callback(self.corde4_amplitude4)
        _corde4_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde4_amplitude4(self._corde4_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde4_amplitude4_check_box, 7, 3, 1, 1)
        for r in range(7, 8):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde4_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde4_amplitude3_choices = {True: True, False: False}
        self._corde4_amplitude3_choices_inv = dict((v,k) for k,v in self._corde4_amplitude3_choices.items())
        self._corde4_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde4_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde4_amplitude3_choices_inv[i]))
        self._corde4_amplitude3_callback(self.corde4_amplitude3)
        _corde4_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde4_amplitude3(self._corde4_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde4_amplitude3_check_box, 7, 2, 1, 1)
        for r in range(7, 8):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde4_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde4_amplitude2_choices = {True: True, False: False}
        self._corde4_amplitude2_choices_inv = dict((v,k) for k,v in self._corde4_amplitude2_choices.items())
        self._corde4_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde4_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde4_amplitude2_choices_inv[i]))
        self._corde4_amplitude2_callback(self.corde4_amplitude2)
        _corde4_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde4_amplitude2(self._corde4_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde4_amplitude2_check_box, 7, 1, 1, 1)
        for r in range(7, 8):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde4_amplitude1_check_box = Qt.QCheckBox('Corde 4 Amplitude 1')
        self._corde4_amplitude1_choices = {True: True, False: False}
        self._corde4_amplitude1_choices_inv = dict((v,k) for k,v in self._corde4_amplitude1_choices.items())
        self._corde4_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde4_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde4_amplitude1_choices_inv[i]))
        self._corde4_amplitude1_callback(self.corde4_amplitude1)
        _corde4_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde4_amplitude1(self._corde4_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde4_amplitude1_check_box, 7, 0, 1, 1)
        for r in range(7, 8):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde3_frequence5_range = Range(1, 200, 0.01, corde3_frequence5_saved, 200)
        self._corde3_frequence5_win = RangeWidget(self._corde3_frequence5_range, self.set_corde3_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde3_frequence5_win, 6, 4, 1, 1)
        for r in range(6, 7):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde3_frequence4_range = Range(1, 200, 0.01, corde3_frequence4_saved, 200)
        self._corde3_frequence4_win = RangeWidget(self._corde3_frequence4_range, self.set_corde3_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde3_frequence4_win, 6, 3, 1, 1)
        for r in range(6, 7):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde3_frequence3_range = Range(1, 200, 0.01, corde3_frequence3_saved, 200)
        self._corde3_frequence3_win = RangeWidget(self._corde3_frequence3_range, self.set_corde3_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde3_frequence3_win, 6, 2, 1, 1)
        for r in range(6, 7):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde3_frequence2_range = Range(1, 200, 0.01, corde3_frequence2_saved, 200)
        self._corde3_frequence2_win = RangeWidget(self._corde3_frequence2_range, self.set_corde3_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde3_frequence2_win, 6, 1, 1, 1)
        for r in range(6, 7):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde3_frequence1_range = Range(1, 200, 0.01, corde3_frequence1_saved, 200)
        self._corde3_frequence1_win = RangeWidget(self._corde3_frequence1_range, self.set_corde3_frequence1, 'Corde 3 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde3_frequence1_win, 6, 0, 1, 1)
        for r in range(6, 7):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde3_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde3_amplitude5_choices = {True: True, False: False}
        self._corde3_amplitude5_choices_inv = dict((v,k) for k,v in self._corde3_amplitude5_choices.items())
        self._corde3_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde3_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde3_amplitude5_choices_inv[i]))
        self._corde3_amplitude5_callback(self.corde3_amplitude5)
        _corde3_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde3_amplitude5(self._corde3_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde3_amplitude5_check_box, 5, 4, 1, 1)
        for r in range(5, 6):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde3_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde3_amplitude4_choices = {True: True, False: False}
        self._corde3_amplitude4_choices_inv = dict((v,k) for k,v in self._corde3_amplitude4_choices.items())
        self._corde3_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde3_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde3_amplitude4_choices_inv[i]))
        self._corde3_amplitude4_callback(self.corde3_amplitude4)
        _corde3_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde3_amplitude4(self._corde3_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde3_amplitude4_check_box, 5, 3, 1, 1)
        for r in range(5, 6):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde3_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde3_amplitude3_choices = {True: True, False: False}
        self._corde3_amplitude3_choices_inv = dict((v,k) for k,v in self._corde3_amplitude3_choices.items())
        self._corde3_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde3_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde3_amplitude3_choices_inv[i]))
        self._corde3_amplitude3_callback(self.corde3_amplitude3)
        _corde3_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde3_amplitude3(self._corde3_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde3_amplitude3_check_box, 5, 2, 1, 1)
        for r in range(5, 6):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde3_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde3_amplitude2_choices = {True: True, False: False}
        self._corde3_amplitude2_choices_inv = dict((v,k) for k,v in self._corde3_amplitude2_choices.items())
        self._corde3_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde3_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde3_amplitude2_choices_inv[i]))
        self._corde3_amplitude2_callback(self.corde3_amplitude2)
        _corde3_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde3_amplitude2(self._corde3_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde3_amplitude2_check_box, 5, 1, 1, 1)
        for r in range(5, 6):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde3_amplitude1_check_box = Qt.QCheckBox('Corde 3 Amplitude 1')
        self._corde3_amplitude1_choices = {True: True, False: False}
        self._corde3_amplitude1_choices_inv = dict((v,k) for k,v in self._corde3_amplitude1_choices.items())
        self._corde3_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde3_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde3_amplitude1_choices_inv[i]))
        self._corde3_amplitude1_callback(self.corde3_amplitude1)
        _corde3_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde3_amplitude1(self._corde3_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde3_amplitude1_check_box, 5, 0, 1, 1)
        for r in range(5, 6):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde2_frequence5_range = Range(1, 200, 0.01, corde2_frequence5_saved, 200)
        self._corde2_frequence5_win = RangeWidget(self._corde2_frequence5_range, self.set_corde2_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde2_frequence5_win, 4, 4, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde2_frequence4_range = Range(1, 200, 0.01, corde2_frequence4_saved, 200)
        self._corde2_frequence4_win = RangeWidget(self._corde2_frequence4_range, self.set_corde2_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde2_frequence4_win, 4, 3, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde2_frequence3_range = Range(1, 200, 0.01, corde2_frequence3_saved, 200)
        self._corde2_frequence3_win = RangeWidget(self._corde2_frequence3_range, self.set_corde2_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde2_frequence3_win, 4, 2, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde2_frequence2_range = Range(1, 200, 0.01, corde2_frequence2_saved, 200)
        self._corde2_frequence2_win = RangeWidget(self._corde2_frequence2_range, self.set_corde2_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde2_frequence2_win, 4, 1, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde2_frequence1_range = Range(1, 200, 0.01, corde2_frequence1_saved, 200)
        self._corde2_frequence1_win = RangeWidget(self._corde2_frequence1_range, self.set_corde2_frequence1, 'Corde 2 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde2_frequence1_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde2_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde2_amplitude5_choices = {True: True, False: False}
        self._corde2_amplitude5_choices_inv = dict((v,k) for k,v in self._corde2_amplitude5_choices.items())
        self._corde2_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde2_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde2_amplitude5_choices_inv[i]))
        self._corde2_amplitude5_callback(self.corde2_amplitude5)
        _corde2_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde2_amplitude5(self._corde2_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde2_amplitude5_check_box, 3, 4, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde2_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde2_amplitude4_choices = {True: True, False: False}
        self._corde2_amplitude4_choices_inv = dict((v,k) for k,v in self._corde2_amplitude4_choices.items())
        self._corde2_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde2_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde2_amplitude4_choices_inv[i]))
        self._corde2_amplitude4_callback(self.corde2_amplitude4)
        _corde2_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde2_amplitude4(self._corde2_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde2_amplitude4_check_box, 3, 3, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde2_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde2_amplitude3_choices = {True: True, False: False}
        self._corde2_amplitude3_choices_inv = dict((v,k) for k,v in self._corde2_amplitude3_choices.items())
        self._corde2_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde2_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde2_amplitude3_choices_inv[i]))
        self._corde2_amplitude3_callback(self.corde2_amplitude3)
        _corde2_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde2_amplitude3(self._corde2_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde2_amplitude3_check_box, 3, 2, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde2_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde2_amplitude2_choices = {True: True, False: False}
        self._corde2_amplitude2_choices_inv = dict((v,k) for k,v in self._corde2_amplitude2_choices.items())
        self._corde2_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde2_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde2_amplitude2_choices_inv[i]))
        self._corde2_amplitude2_callback(self.corde2_amplitude2)
        _corde2_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde2_amplitude2(self._corde2_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde2_amplitude2_check_box, 3, 1, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde2_amplitude1_check_box = Qt.QCheckBox('Corde 2 Amplitude 1')
        self._corde2_amplitude1_choices = {True: True, False: False}
        self._corde2_amplitude1_choices_inv = dict((v,k) for k,v in self._corde2_amplitude1_choices.items())
        self._corde2_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde2_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde2_amplitude1_choices_inv[i]))
        self._corde2_amplitude1_callback(self.corde2_amplitude1)
        _corde2_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde2_amplitude1(self._corde2_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde2_amplitude1_check_box, 3, 0, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde1_frequence5_range = Range(1, 200, 0.01, corde1_frequence5_saved, 200)
        self._corde1_frequence5_win = RangeWidget(self._corde1_frequence5_range, self.set_corde1_frequence5, ' Frequence 5', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde1_frequence5_win, 2, 4, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde1_frequence4_range = Range(1, 200, 0.01, corde1_frequence4_saved, 200)
        self._corde1_frequence4_win = RangeWidget(self._corde1_frequence4_range, self.set_corde1_frequence4, ' Frequence 4', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde1_frequence4_win, 2, 3, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde1_frequence3_range = Range(1, 200, 0.01, corde1_frequence3_saved, 200)
        self._corde1_frequence3_win = RangeWidget(self._corde1_frequence3_range, self.set_corde1_frequence3, ' Frequence 3', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde1_frequence3_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde1_frequence2_range = Range(1, 200, 0.01, corde1_frequence2_saved, 200)
        self._corde1_frequence2_win = RangeWidget(self._corde1_frequence2_range, self.set_corde1_frequence2, ' Frequence 2', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde1_frequence2_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._corde1_frequence1_range = Range(1, 200, 0.01, corde1_frequence1_saved, 200)
        self._corde1_frequence1_win = RangeWidget(self._corde1_frequence1_range, self.set_corde1_frequence1, 'Corde 1 Frequence 1', "counter", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._corde1_frequence1_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde1_amplitude5_check_box = Qt.QCheckBox('Amplitude 5')
        self._corde1_amplitude5_choices = {True: True, False: False}
        self._corde1_amplitude5_choices_inv = dict((v,k) for k,v in self._corde1_amplitude5_choices.items())
        self._corde1_amplitude5_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde1_amplitude5_check_box, "setChecked", Qt.Q_ARG("bool", self._corde1_amplitude5_choices_inv[i]))
        self._corde1_amplitude5_callback(self.corde1_amplitude5)
        _corde1_amplitude5_check_box.stateChanged.connect(lambda i: self.set_corde1_amplitude5(self._corde1_amplitude5_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde1_amplitude5_check_box, 1, 4, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(4, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde1_amplitude4_check_box = Qt.QCheckBox('Amplitude 4')
        self._corde1_amplitude4_choices = {True: True, False: False}
        self._corde1_amplitude4_choices_inv = dict((v,k) for k,v in self._corde1_amplitude4_choices.items())
        self._corde1_amplitude4_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde1_amplitude4_check_box, "setChecked", Qt.Q_ARG("bool", self._corde1_amplitude4_choices_inv[i]))
        self._corde1_amplitude4_callback(self.corde1_amplitude4)
        _corde1_amplitude4_check_box.stateChanged.connect(lambda i: self.set_corde1_amplitude4(self._corde1_amplitude4_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde1_amplitude4_check_box, 1, 3, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde1_amplitude3_check_box = Qt.QCheckBox('Amplitude 3')
        self._corde1_amplitude3_choices = {True: True, False: False}
        self._corde1_amplitude3_choices_inv = dict((v,k) for k,v in self._corde1_amplitude3_choices.items())
        self._corde1_amplitude3_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde1_amplitude3_check_box, "setChecked", Qt.Q_ARG("bool", self._corde1_amplitude3_choices_inv[i]))
        self._corde1_amplitude3_callback(self.corde1_amplitude3)
        _corde1_amplitude3_check_box.stateChanged.connect(lambda i: self.set_corde1_amplitude3(self._corde1_amplitude3_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde1_amplitude3_check_box, 1, 2, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde1_amplitude2_check_box = Qt.QCheckBox('Amplitude 2')
        self._corde1_amplitude2_choices = {True: True, False: False}
        self._corde1_amplitude2_choices_inv = dict((v,k) for k,v in self._corde1_amplitude2_choices.items())
        self._corde1_amplitude2_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde1_amplitude2_check_box, "setChecked", Qt.Q_ARG("bool", self._corde1_amplitude2_choices_inv[i]))
        self._corde1_amplitude2_callback(self.corde1_amplitude2)
        _corde1_amplitude2_check_box.stateChanged.connect(lambda i: self.set_corde1_amplitude2(self._corde1_amplitude2_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde1_amplitude2_check_box, 1, 1, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        _corde1_amplitude1_check_box = Qt.QCheckBox('Corde 1 Amplitude 1')
        self._corde1_amplitude1_choices = {True: True, False: False}
        self._corde1_amplitude1_choices_inv = dict((v,k) for k,v in self._corde1_amplitude1_choices.items())
        self._corde1_amplitude1_callback = lambda i: Qt.QMetaObject.invokeMethod(_corde1_amplitude1_check_box, "setChecked", Qt.Q_ARG("bool", self._corde1_amplitude1_choices_inv[i]))
        self._corde1_amplitude1_callback(self.corde1_amplitude1)
        _corde1_amplitude1_check_box.stateChanged.connect(lambda i: self.set_corde1_amplitude1(self._corde1_amplitude1_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_2.addWidget(_corde1_amplitude1_check_box, 1, 0, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._Low_Pass_Filter_cut_of_frequency_range = Range(0, 3e5, 1e3, 9e4, 200)
        self._Low_Pass_Filter_cut_of_frequency_win = RangeWidget(self._Low_Pass_Filter_cut_of_frequency_range, self.set_Low_Pass_Filter_cut_of_frequency, 'Bandwitdh', "counter_slider", float)
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._Low_Pass_Filter_cut_of_frequency_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self._Low_Pass_Filter_Transition_Width_range = Range(0, 1e6, 1e3, 1e4, 200)
        self._Low_Pass_Filter_Transition_Width_win = RangeWidget(self._Low_Pass_Filter_Transition_Width_range, self.set_Low_Pass_Filter_Transition_Width, 'Transition', "counter_slider", float)
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._Low_Pass_Filter_Transition_Width_win, 3, 1, 1, 1)
        for r in range(3, 4):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self._volume_headphone_slider_range = Range(0, 1, 0.01, 0.5, 200)
        self._volume_headphone_slider_win = RangeWidget(self._volume_headphone_slider_range, self.set_volume_headphone_slider, 'Volume Headphone', "counter_slider", float)
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._volume_headphone_slider_win, 0, 0, 1, 2)
        for r in range(0, 1):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 2):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self._volume_cordes_slider_range = Range(0, 1, 0.01, volume_cordes_saved, 200)
        self._volume_cordes_slider_win = RangeWidget(self._volume_cordes_slider_range, self.set_volume_cordes_slider, 'Volume Cordes', "counter_slider", float)
        self.qtgui_tab_widget_grid_layout_2.addWidget(self._volume_cordes_slider_win, 0, 1, 1, 4)
        for r in range(0, 1):
            self.qtgui_tab_widget_grid_layout_2.setRowStretch(r, 1)
        for c in range(1, 5):
            self.qtgui_tab_widget_grid_layout_2.setColumnStretch(c, 1)
        self._time_stop_on_frequency_range = Range(0, 120, 0.1, time_stop_on_frequency_saved, 200)
        self._time_stop_on_frequency_win = RangeWidget(self._time_stop_on_frequency_range, self.set_time_stop_on_frequency, 'time stop on frequency', "counter_slider", float)
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._time_stop_on_frequency_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self._time_between_frequencies_range = Range(0, 120, 0.1, time_between_frequencies_saved, 200)
        self._time_between_frequencies_win = RangeWidget(self._time_between_frequencies_range, self.set_time_between_frequencies, 'time between frequencies', "counter_slider", float)
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._time_between_frequencies_win, 4, 1, 1, 1)
        for r in range(4, 5):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ""
        )
        self.rtlsdr_source_0.set_time_source('gpsdo', 0)
        self.rtlsdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.rtlsdr_source_0.set_sample_rate(radio_sample_rate)
        self.rtlsdr_source_0.set_center_freq(radio_frequency_center, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_gain(49, 0)
        self.rtlsdr_source_0.set_if_gain(1, 0)
        self.rtlsdr_source_0.set_bb_gain(1, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        _radio_scann_check_box = Qt.QCheckBox('Auto Scann')
        self._radio_scann_choices = {True: True, False: False}
        self._radio_scann_choices_inv = dict((v,k) for k,v in self._radio_scann_choices.items())
        self._radio_scann_callback = lambda i: Qt.QMetaObject.invokeMethod(_radio_scann_check_box, "setChecked", Qt.Q_ARG("bool", self._radio_scann_choices_inv[i]))
        self._radio_scann_callback(self.radio_scann)
        _radio_scann_check_box.stateChanged.connect(lambda i: self.set_radio_scann(self._radio_scann_choices[bool(i)]))
        self.qtgui_tab_widget_grid_layout_1.addWidget(_radio_scann_check_box, 1, 1, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        # Create the options list
        self._radio_frequency_center_menu_options = [0]
        # Create the labels list
        self._radio_frequency_center_menu_labels = []
        # Create the combo box
        self._radio_frequency_center_menu_tool_bar = Qt.QToolBar(self)
        self._radio_frequency_center_menu_tool_bar.addWidget(Qt.QLabel('Radio Frequency' + ": "))
        self._radio_frequency_center_menu_combo_box = Qt.QComboBox()
        self._radio_frequency_center_menu_tool_bar.addWidget(self._radio_frequency_center_menu_combo_box)
        for _label in self._radio_frequency_center_menu_labels: self._radio_frequency_center_menu_combo_box.addItem(_label)
        self._radio_frequency_center_menu_callback = lambda i: Qt.QMetaObject.invokeMethod(self._radio_frequency_center_menu_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._radio_frequency_center_menu_options.index(i)))
        self._radio_frequency_center_menu_callback(self.radio_frequency_center_menu)
        self._radio_frequency_center_menu_combo_box.currentIndexChanged.connect(
            lambda i: self.set_radio_frequency_center_menu(self._radio_frequency_center_menu_options[i]))
        # Create the radio buttons
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._radio_frequency_center_menu_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)
        self.qtgui_vector_sink_f_0_0 = qtgui.vector_sink_f(
            int(FFT_size/2),
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0.set_y_axis(0, 10)
        self.qtgui_vector_sink_f_0_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0.set_ref_level(0)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_vector_sink_f_0_0_win, 0, 0, 1, 4)
        for r in range(0, 1):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 4):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde8_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_0_0_0_win, 2, 3, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde7_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_0_0_win, 2, 2, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0_0_0_0_0 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde6_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_0_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0_0_0_0 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde5_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_1_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0_0_0 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde4_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0.set_update_time(1)
        self.qtgui_time_sink_x_1_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_0_0_win, 1, 3, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(3, 4):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0_0 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde3_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0.set_update_time(1)
        self.qtgui_time_sink_x_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_0_win, 1, 2, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(2, 3):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde2_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(1)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0.enable_tags(True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            32000, #size
            audio_sample_rate, #samp_rate
            'Corde1_signal', #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(1)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_3.addWidget(self._qtgui_time_sink_x_1_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_3.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_3.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            int(audio_sample_rate *0.1), #size
            audio_sample_rate, #samp_rate
            "", #name
            1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.01)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_0.addWidget(self._qtgui_time_sink_x_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.qtgui_tab_widget_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            radio_frequency_center, #fc
            radio_sample_rate, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-70, -20)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(0.2)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_grid_layout_0.addWidget(self._qtgui_freq_sink_x_1_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.qtgui_tab_widget_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.qtgui_tab_widget_grid_layout_0.setColumnStretch(c, 1)
        self.high_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.high_pass(
                1,
                audio_sample_rate,
                40.0,
                10.0,
                firdes.WIN_HAMMING,
                6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(2,  firdes.low_pass_2(1,radio_sample_rate,Low_Pass_Filter_cut_of_frequency,Low_Pass_Filter_Transition_Width,40), radio_frequency__delta_MHz*1e6, radio_sample_rate)
        self.fft_vxx_0 = fft.fft_vfc(FFT_size, True, window.blackmanharris(FFT_size), 1)
        self.epy_block_0_1_0 = epy_block_0_1_0.blk(in_vector_size=FFT_size, nb_cordes=8, nb_harmoniques=5, nb_cordes_out=8, on_off=radio_on_cordes)
        self.epy_block_0_0 = epy_block_0_0.blk(in_vector_size=FFT_size, out_vector_size=512, example_parameter=1.0)
        self.blocks_vector_to_stream_0_0_3_0_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_3_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_3_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_3_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_3_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_3_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_3 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2_0_0_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2_0_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_2 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1_1_0_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1_1_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1_1_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1_1_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1_1_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1_1_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1_1 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_1 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_2_0_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_2_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_2_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_2_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_2_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_2_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_2 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0_1_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0_1_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0_1_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0_1 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 1024)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_float*1, FFT_size)
        self.blocks_multiply_xx_0_2_0_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_1_0_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_1_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_1_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_1_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_1_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_2_0_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_2_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_2_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_2_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_2_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_2_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_1_0_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_1_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_1_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_1_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_xx_1_2 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_1_1_0 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_1_1 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_1_0_1 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_1_0_0_0 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_1_0_0 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_1_0 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_1 = blocks.multiply_const_ff(volume_cordes, 1)
        self.blocks_multiply_const_xx_0_0_0 = blocks.multiply_const_ff(volume_headphone, 1)
        self.blocks_multiply_const_xx_0_0 = blocks.multiply_const_ff(volume_headphone, 1)
        self.blocks_multiply_const_xx_0 = blocks.multiply_const_ff(volume_headphone, 1)
        self.blocks_add_xx_0_1_5_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_5 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_4 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_3 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_2 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0_2_6_0 = blocks.add_const_ff(corde8_amplitude3)
        self.blocks_add_const_vxx_0_2_6 = blocks.add_const_ff(corde7_amplitude3)
        self.blocks_add_const_vxx_0_2_5 = blocks.add_const_ff(corde6_amplitude3)
        self.blocks_add_const_vxx_0_2_4 = blocks.add_const_ff(corde5_amplitude3)
        self.blocks_add_const_vxx_0_2_3 = blocks.add_const_ff(corde4_amplitude3)
        self.blocks_add_const_vxx_0_2_2 = blocks.add_const_ff(corde3_amplitude3)
        self.blocks_add_const_vxx_0_2_1 = blocks.add_const_ff(corde2_amplitude3)
        self.blocks_add_const_vxx_0_2 = blocks.add_const_ff(corde1_amplitude3)
        self.blocks_add_const_vxx_0_1_5_0 = blocks.add_const_ff(corde8_amplitude1)
        self.blocks_add_const_vxx_0_1_5 = blocks.add_const_ff(corde7_amplitude1)
        self.blocks_add_const_vxx_0_1_4 = blocks.add_const_ff(corde6_amplitude1)
        self.blocks_add_const_vxx_0_1_3 = blocks.add_const_ff(corde5_amplitude1)
        self.blocks_add_const_vxx_0_1_2 = blocks.add_const_ff(corde4_amplitude1)
        self.blocks_add_const_vxx_0_1_1 = blocks.add_const_ff(corde3_amplitude1)
        self.blocks_add_const_vxx_0_1_0 = blocks.add_const_ff(corde2_amplitude1)
        self.blocks_add_const_vxx_0_1 = blocks.add_const_ff(corde1_amplitude1)
        self.blocks_add_const_vxx_0_0_1_6_0 = blocks.add_const_ff(corde8_amplitude2)
        self.blocks_add_const_vxx_0_0_1_6 = blocks.add_const_ff(corde7_amplitude2)
        self.blocks_add_const_vxx_0_0_1_5 = blocks.add_const_ff(corde6_amplitude2)
        self.blocks_add_const_vxx_0_0_1_4 = blocks.add_const_ff(corde5_amplitude2)
        self.blocks_add_const_vxx_0_0_1_3 = blocks.add_const_ff(corde4_amplitude2)
        self.blocks_add_const_vxx_0_0_1_2 = blocks.add_const_ff(corde3_amplitude2)
        self.blocks_add_const_vxx_0_0_1_1 = blocks.add_const_ff(corde2_amplitude2)
        self.blocks_add_const_vxx_0_0_1_0_7_0 = blocks.add_const_ff(corde8_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_7 = blocks.add_const_ff(corde7_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_6 = blocks.add_const_ff(corde6_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_5 = blocks.add_const_ff(corde5_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_4 = blocks.add_const_ff(corde4_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_3 = blocks.add_const_ff(corde3_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_2 = blocks.add_const_ff(corde2_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_1_6_0 = blocks.add_const_ff(corde8_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_6 = blocks.add_const_ff(corde7_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_5 = blocks.add_const_ff(corde6_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_4 = blocks.add_const_ff(corde5_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_3 = blocks.add_const_ff(corde4_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_2 = blocks.add_const_ff(corde3_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_1 = blocks.add_const_ff(corde2_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1 = blocks.add_const_ff(corde1_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0 = blocks.add_const_ff(corde1_amplitude4)
        self.blocks_add_const_vxx_0_0_1 = blocks.add_const_ff(corde1_amplitude2)
        self.audio_sink_0 = audio.sink(audio_sample_rate, 'plughw:CARD=UMC1820,DEV=0', True)
        self.analog_wfm_rcv_pll_0 = analog.wfm_rcv_pll(
        	demod_rate=audio_sample_rate*WBFM_Receive_PLL_Audio_Decimation,
        	audio_decimation=WBFM_Receive_PLL_Audio_Decimation,
        )
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=audio_sample_rate*WBFM_Receive_PLL_Audio_Decimation,
        	audio_decimation=WBFM_Receive_PLL_Audio_Decimation,
        )
        self.analog_sig_source_x_0_7_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde8_frequence1, 0.5, 0, 0)
        self.analog_sig_source_x_0_7 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde7_frequence1, 0.5, 0, 0)
        self.analog_sig_source_x_0_6 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde6_frequence1, 0.5, 0, 0)
        self.analog_sig_source_x_0_5 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde5_frequence1, 0.5, 0, 0)
        self.analog_sig_source_x_0_4 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde4_frequence1, 0.5, 0, 0)
        self.analog_sig_source_x_0_3 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde3_frequence1, 0.5, 0, 0)
        self.analog_sig_source_x_0_2 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde2_frequence1, 0.5, 0, 0)
        self.analog_sig_source_x_0_1_6_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde8_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_1_6 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde7_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_1_5 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde6_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_1_4 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde5_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_1_3 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde4_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_1_2 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde3_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_1_1 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde2_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde1_frequence3, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_6_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde8_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_6 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde7_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_5 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde6_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_4 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde5_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_3 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde4_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_2 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde3_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_1 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde2_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_7_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde8_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_7 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde7_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_6 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde6_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_5 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde5_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_4 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde4_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_3 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde3_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_2 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde2_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1_6_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde8_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1_6 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde7_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1_5 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde6_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1_4 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde5_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1_3 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde4_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1_2 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde3_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1_1 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde2_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0_1 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde1_frequence5, 0.5, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde1_frequence4, 0.5, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde1_frequence2, 0.5, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(audio_sample_rate, analog.GR_SIN_WAVE, corde1_frequence1, 0.5, 0, 0)
        self.analog_agc2_xx_0 = analog.agc2_cc(1e-2, 1e-2, 1.0, 0)
        self.analog_agc2_xx_0.set_max_gain(4)
        self._Frequency_tool_bar = Qt.QToolBar(self)

        if None:
            self._Frequency_formatter = None
        else:
            self._Frequency_formatter = lambda x: str(x)

        self._Frequency_tool_bar.addWidget(Qt.QLabel(" " + ": "))
        self._Frequency_label = Qt.QLabel(str(self._Frequency_formatter(self.Frequency)))
        self._Frequency_tool_bar.addWidget(self._Frequency_label)
        self.qtgui_tab_widget_grid_layout_1.addWidget(self._Frequency_tool_bar, 2, 1, 1, 1)
        for r in range(2, 3):
            self.qtgui_tab_widget_grid_layout_1.setRowStretch(r, 1)
        for c in range(1, 2):
            self.qtgui_tab_widget_grid_layout_1.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_wfm_rcv_0, 0))
        self.connect((self.analog_agc2_xx_0, 0), (self.analog_wfm_rcv_pll_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1, 0), (self.blocks_multiply_xx_0_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1_1, 0), (self.blocks_multiply_xx_0_0_1_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1_2, 0), (self.blocks_multiply_xx_0_0_1_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1_3, 0), (self.blocks_multiply_xx_0_0_1_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1_4, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1_5, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1_6, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_1_6_0, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_2, 0), (self.blocks_multiply_xx_0_0_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0_0_3, 0), (self.blocks_multiply_xx_0_0_0_1_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_4, 0), (self.blocks_multiply_xx_0_0_0_1_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_5, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_6, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_7, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0_7_0, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_1, 0), (self.blocks_multiply_xx_0_0_2, 0))
        self.connect((self.analog_sig_source_x_0_0_2, 0), (self.blocks_multiply_xx_0_0_2_0, 0))
        self.connect((self.analog_sig_source_x_0_0_3, 0), (self.blocks_multiply_xx_0_0_2_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_4, 0), (self.blocks_multiply_xx_0_0_2_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_5, 0), (self.blocks_multiply_xx_0_0_2_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_6, 0), (self.blocks_multiply_xx_0_0_2_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_6_0, 0), (self.blocks_multiply_xx_0_0_2_0_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_0_1_1, 0), (self.blocks_multiply_xx_0_1_1, 0))
        self.connect((self.analog_sig_source_x_0_1_2, 0), (self.blocks_multiply_xx_0_1_1_0, 0))
        self.connect((self.analog_sig_source_x_0_1_3, 0), (self.blocks_multiply_xx_0_1_1_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1_4, 0), (self.blocks_multiply_xx_0_1_1_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1_5, 0), (self.blocks_multiply_xx_0_1_1_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1_6, 0), (self.blocks_multiply_xx_0_1_1_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_1_6_0, 0), (self.blocks_multiply_xx_0_1_1_0_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.analog_sig_source_x_0_3, 0), (self.blocks_multiply_xx_0_2_0, 0))
        self.connect((self.analog_sig_source_x_0_4, 0), (self.blocks_multiply_xx_0_2_0_0, 0))
        self.connect((self.analog_sig_source_x_0_5, 0), (self.blocks_multiply_xx_0_2_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_6, 0), (self.blocks_multiply_xx_0_2_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_7, 0), (self.blocks_multiply_xx_0_2_0_0_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_7_0, 0), (self.blocks_multiply_xx_0_2_0_0_0_0_0_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_xx_0_0_0, 0))
        self.connect((self.analog_wfm_rcv_0, 0), (self.high_pass_filter_0, 0))
        self.connect((self.analog_wfm_rcv_pll_0, 0), (self.blocks_multiply_const_xx_0, 0))
        self.connect((self.analog_wfm_rcv_pll_0, 1), (self.blocks_multiply_const_xx_0_0, 0))
        self.connect((self.blocks_add_const_vxx_0_0_1, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1, 0), (self.blocks_multiply_xx_0_0_1, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1_1, 0), (self.blocks_multiply_xx_0_0_1_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1_2, 0), (self.blocks_multiply_xx_0_0_1_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1_3, 0), (self.blocks_multiply_xx_0_0_1_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1_4, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1_5, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1_6, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_1_6_0, 0), (self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_2, 0), (self.blocks_multiply_xx_0_0_0_1, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_3, 0), (self.blocks_multiply_xx_0_0_0_1_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_4, 0), (self.blocks_multiply_xx_0_0_0_1_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_5, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_6, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_7, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_0_7_0, 0), (self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_1, 0), (self.blocks_multiply_xx_0_0_2, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_2, 0), (self.blocks_multiply_xx_0_0_2_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_3, 0), (self.blocks_multiply_xx_0_0_2_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_4, 0), (self.blocks_multiply_xx_0_0_2_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_5, 0), (self.blocks_multiply_xx_0_0_2_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_6, 0), (self.blocks_multiply_xx_0_0_2_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_0_1_6_0, 0), (self.blocks_multiply_xx_0_0_2_0_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1_0, 0), (self.blocks_multiply_xx_0_2, 1))
        self.connect((self.blocks_add_const_vxx_0_1_1, 0), (self.blocks_multiply_xx_0_2_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1_2, 0), (self.blocks_multiply_xx_0_2_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1_3, 0), (self.blocks_multiply_xx_0_2_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1_4, 0), (self.blocks_multiply_xx_0_2_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1_5, 0), (self.blocks_multiply_xx_0_2_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_1_5_0, 0), (self.blocks_multiply_xx_0_2_0_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_2, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_add_const_vxx_0_2_1, 0), (self.blocks_multiply_xx_0_1_1, 1))
        self.connect((self.blocks_add_const_vxx_0_2_2, 0), (self.blocks_multiply_xx_0_1_1_0, 1))
        self.connect((self.blocks_add_const_vxx_0_2_3, 0), (self.blocks_multiply_xx_0_1_1_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_2_4, 0), (self.blocks_multiply_xx_0_1_1_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_2_5, 0), (self.blocks_multiply_xx_0_1_1_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_2_6, 0), (self.blocks_multiply_xx_0_1_1_0_0_0_0_0, 1))
        self.connect((self.blocks_add_const_vxx_0_2_6_0, 0), (self.blocks_multiply_xx_0_1_1_0_0_0_0_0_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 1))
        self.connect((self.blocks_add_xx_0_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_add_xx_0_1_0, 0), (self.blocks_multiply_const_xx_1_0, 0))
        self.connect((self.blocks_add_xx_0_1_0, 0), (self.qtgui_time_sink_x_1_0, 0))
        self.connect((self.blocks_add_xx_0_1_0_0, 0), (self.blocks_multiply_const_xx_1, 0))
        self.connect((self.blocks_add_xx_0_1_0_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_add_xx_0_1_1, 0), (self.blocks_multiply_const_xx_1_1, 0))
        self.connect((self.blocks_add_xx_0_1_1, 0), (self.qtgui_time_sink_x_1_0_0, 0))
        self.connect((self.blocks_add_xx_0_1_2, 0), (self.blocks_multiply_const_xx_1_0_0, 0))
        self.connect((self.blocks_add_xx_0_1_2, 0), (self.qtgui_time_sink_x_1_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_1_3, 0), (self.blocks_multiply_const_xx_1_2, 0))
        self.connect((self.blocks_add_xx_0_1_3, 0), (self.qtgui_time_sink_x_1_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_1_4, 0), (self.blocks_multiply_const_xx_1_0_1, 0))
        self.connect((self.blocks_add_xx_0_1_4, 0), (self.qtgui_time_sink_x_1_0_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_1_5, 0), (self.blocks_multiply_const_xx_1_1_0, 0))
        self.connect((self.blocks_add_xx_0_1_5, 0), (self.qtgui_time_sink_x_1_0_0_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_1_5_0, 0), (self.blocks_multiply_const_xx_1_0_0_0, 0))
        self.connect((self.blocks_add_xx_0_1_5_0, 0), (self.qtgui_time_sink_x_1_0_0_0_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_xx_0, 0), (self.blocks_add_xx_0_0, 0))
        self.connect((self.blocks_multiply_const_xx_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_xx_0_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_xx_0_0_0, 0), (self.blocks_add_xx_0_0, 1))
        self.connect((self.blocks_multiply_const_xx_1, 0), (self.audio_sink_0, 2))
        self.connect((self.blocks_multiply_const_xx_1_0, 0), (self.audio_sink_0, 3))
        self.connect((self.blocks_multiply_const_xx_1_0_0, 0), (self.audio_sink_0, 5))
        self.connect((self.blocks_multiply_const_xx_1_0_0_0, 0), (self.audio_sink_0, 9))
        self.connect((self.blocks_multiply_const_xx_1_0_1, 0), (self.audio_sink_0, 7))
        self.connect((self.blocks_multiply_const_xx_1_1, 0), (self.audio_sink_0, 4))
        self.connect((self.blocks_multiply_const_xx_1_1_0, 0), (self.audio_sink_0, 8))
        self.connect((self.blocks_multiply_const_xx_1_2, 0), (self.audio_sink_0, 6))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0_1_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0_1_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.blocks_add_xx_0_1_0_0, 3))
        self.connect((self.blocks_multiply_xx_0_0_0_1, 0), (self.blocks_add_xx_0_1_0, 3))
        self.connect((self.blocks_multiply_xx_0_0_0_1_0, 0), (self.blocks_add_xx_0_1_1, 3))
        self.connect((self.blocks_multiply_xx_0_0_0_1_0_0, 0), (self.blocks_add_xx_0_1_2, 3))
        self.connect((self.blocks_multiply_xx_0_0_0_1_0_0_0, 0), (self.blocks_add_xx_0_1_3, 3))
        self.connect((self.blocks_multiply_xx_0_0_0_1_0_0_0_0, 0), (self.blocks_add_xx_0_1_4, 3))
        self.connect((self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5, 3))
        self.connect((self.blocks_multiply_xx_0_0_0_1_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5_0, 3))
        self.connect((self.blocks_multiply_xx_0_0_1, 0), (self.blocks_add_xx_0_1_0_0, 4))
        self.connect((self.blocks_multiply_xx_0_0_1_0, 0), (self.blocks_add_xx_0_1_0, 4))
        self.connect((self.blocks_multiply_xx_0_0_1_0_0, 0), (self.blocks_add_xx_0_1_1, 4))
        self.connect((self.blocks_multiply_xx_0_0_1_0_0_0, 0), (self.blocks_add_xx_0_1_2, 4))
        self.connect((self.blocks_multiply_xx_0_0_1_0_0_0_0, 0), (self.blocks_add_xx_0_1_3, 4))
        self.connect((self.blocks_multiply_xx_0_0_1_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_4, 4))
        self.connect((self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5, 4))
        self.connect((self.blocks_multiply_xx_0_0_1_0_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5_0, 4))
        self.connect((self.blocks_multiply_xx_0_0_2, 0), (self.blocks_add_xx_0_1_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_2_0, 0), (self.blocks_add_xx_0_1_1, 1))
        self.connect((self.blocks_multiply_xx_0_0_2_0_0, 0), (self.blocks_add_xx_0_1_2, 1))
        self.connect((self.blocks_multiply_xx_0_0_2_0_0_0, 0), (self.blocks_add_xx_0_1_3, 1))
        self.connect((self.blocks_multiply_xx_0_0_2_0_0_0_0, 0), (self.blocks_add_xx_0_1_4, 1))
        self.connect((self.blocks_multiply_xx_0_0_2_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5, 1))
        self.connect((self.blocks_multiply_xx_0_0_2_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5_0, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_add_xx_0_1_0_0, 2))
        self.connect((self.blocks_multiply_xx_0_1_1, 0), (self.blocks_add_xx_0_1_0, 2))
        self.connect((self.blocks_multiply_xx_0_1_1_0, 0), (self.blocks_add_xx_0_1_1, 2))
        self.connect((self.blocks_multiply_xx_0_1_1_0_0, 0), (self.blocks_add_xx_0_1_2, 2))
        self.connect((self.blocks_multiply_xx_0_1_1_0_0_0, 0), (self.blocks_add_xx_0_1_3, 2))
        self.connect((self.blocks_multiply_xx_0_1_1_0_0_0_0, 0), (self.blocks_add_xx_0_1_4, 2))
        self.connect((self.blocks_multiply_xx_0_1_1_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5, 2))
        self.connect((self.blocks_multiply_xx_0_1_1_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5_0, 2))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_add_xx_0_1_0, 0))
        self.connect((self.blocks_multiply_xx_0_2_0, 0), (self.blocks_add_xx_0_1_1, 0))
        self.connect((self.blocks_multiply_xx_0_2_0_0, 0), (self.blocks_add_xx_0_1_2, 0))
        self.connect((self.blocks_multiply_xx_0_2_0_0_0, 0), (self.blocks_add_xx_0_1_3, 0))
        self.connect((self.blocks_multiply_xx_0_2_0_0_0_0, 0), (self.blocks_add_xx_0_1_4, 0))
        self.connect((self.blocks_multiply_xx_0_2_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5, 0))
        self.connect((self.blocks_multiply_xx_0_2_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_5_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.fft_vxx_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_add_const_vxx_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0_1, 0), (self.blocks_add_const_vxx_0_0_1_0_2, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0_1_0, 0), (self.blocks_add_const_vxx_0_0_1_0_3, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0_1_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_4, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0_1_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_5, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_6, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_7, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_7_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_2, 0), (self.blocks_add_const_vxx_0_0_1_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_2_0, 0), (self.blocks_add_const_vxx_0_0_1_2, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_2_0_0, 0), (self.blocks_add_const_vxx_0_0_1_3, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_2_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_4, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_2_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_5, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_2_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_6, 0))
        self.connect((self.blocks_vector_to_stream_0_0_0_2_0_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_6_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1, 0), (self.blocks_add_const_vxx_0_2, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1_1, 0), (self.blocks_add_const_vxx_0_2_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1_1_0, 0), (self.blocks_add_const_vxx_0_2_2, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1_1_0_0, 0), (self.blocks_add_const_vxx_0_2_3, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1_1_0_0_0, 0), (self.blocks_add_const_vxx_0_2_4, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1_1_0_0_0_0, 0), (self.blocks_add_const_vxx_0_2_5, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1_1_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_2_6, 0))
        self.connect((self.blocks_vector_to_stream_0_0_1_1_0_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_2_6_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2, 0), (self.blocks_add_const_vxx_0_0_1_0_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2_0, 0), (self.blocks_add_const_vxx_0_0_1_0_1_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_1_2, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_1_3, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_1_4, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_1_5, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2_0_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_1_6, 0))
        self.connect((self.blocks_vector_to_stream_0_0_2_0_0_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_0_1_0_1_6_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0_3, 0), (self.blocks_add_const_vxx_0_1_0, 0))
        self.connect((self.blocks_vector_to_stream_0_0_3_0, 0), (self.blocks_add_const_vxx_0_1_1, 0))
        self.connect((self.blocks_vector_to_stream_0_0_3_0_0, 0), (self.blocks_add_const_vxx_0_1_2, 0))
        self.connect((self.blocks_vector_to_stream_0_0_3_0_0_0, 0), (self.blocks_add_const_vxx_0_1_3, 0))
        self.connect((self.blocks_vector_to_stream_0_0_3_0_0_0_0, 0), (self.blocks_add_const_vxx_0_1_4, 0))
        self.connect((self.blocks_vector_to_stream_0_0_3_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_1_5, 0))
        self.connect((self.blocks_vector_to_stream_0_0_3_0_0_0_0_0_0, 0), (self.blocks_add_const_vxx_0_1_5_0, 0))
        self.connect((self.epy_block_0_0, 0), (self.qtgui_vector_sink_f_0_0, 0))
        self.connect((self.epy_block_0_1_0, 0), (self.blocks_vector_to_stream_0_0, 0))
        self.connect((self.epy_block_0_1_0, 1), (self.blocks_vector_to_stream_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 3), (self.blocks_vector_to_stream_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 8), (self.blocks_vector_to_stream_0_0_0_0_1, 0))
        self.connect((self.epy_block_0_1_0, 13), (self.blocks_vector_to_stream_0_0_0_0_1_0, 0))
        self.connect((self.epy_block_0_1_0, 18), (self.blocks_vector_to_stream_0_0_0_0_1_0_0, 0))
        self.connect((self.epy_block_0_1_0, 23), (self.blocks_vector_to_stream_0_0_0_0_1_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 28), (self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 33), (self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 38), (self.blocks_vector_to_stream_0_0_0_0_1_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 6), (self.blocks_vector_to_stream_0_0_0_2, 0))
        self.connect((self.epy_block_0_1_0, 11), (self.blocks_vector_to_stream_0_0_0_2_0, 0))
        self.connect((self.epy_block_0_1_0, 16), (self.blocks_vector_to_stream_0_0_0_2_0_0, 0))
        self.connect((self.epy_block_0_1_0, 21), (self.blocks_vector_to_stream_0_0_0_2_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 26), (self.blocks_vector_to_stream_0_0_0_2_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 31), (self.blocks_vector_to_stream_0_0_0_2_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 36), (self.blocks_vector_to_stream_0_0_0_2_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 2), (self.blocks_vector_to_stream_0_0_1, 0))
        self.connect((self.epy_block_0_1_0, 7), (self.blocks_vector_to_stream_0_0_1_1, 0))
        self.connect((self.epy_block_0_1_0, 12), (self.blocks_vector_to_stream_0_0_1_1_0, 0))
        self.connect((self.epy_block_0_1_0, 17), (self.blocks_vector_to_stream_0_0_1_1_0_0, 0))
        self.connect((self.epy_block_0_1_0, 22), (self.blocks_vector_to_stream_0_0_1_1_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 27), (self.blocks_vector_to_stream_0_0_1_1_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 32), (self.blocks_vector_to_stream_0_0_1_1_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 37), (self.blocks_vector_to_stream_0_0_1_1_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 4), (self.blocks_vector_to_stream_0_0_2, 0))
        self.connect((self.epy_block_0_1_0, 9), (self.blocks_vector_to_stream_0_0_2_0, 0))
        self.connect((self.epy_block_0_1_0, 14), (self.blocks_vector_to_stream_0_0_2_0_0, 0))
        self.connect((self.epy_block_0_1_0, 19), (self.blocks_vector_to_stream_0_0_2_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 24), (self.blocks_vector_to_stream_0_0_2_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 29), (self.blocks_vector_to_stream_0_0_2_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 34), (self.blocks_vector_to_stream_0_0_2_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 39), (self.blocks_vector_to_stream_0_0_2_0_0_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 5), (self.blocks_vector_to_stream_0_0_3, 0))
        self.connect((self.epy_block_0_1_0, 10), (self.blocks_vector_to_stream_0_0_3_0, 0))
        self.connect((self.epy_block_0_1_0, 15), (self.blocks_vector_to_stream_0_0_3_0_0, 0))
        self.connect((self.epy_block_0_1_0, 20), (self.blocks_vector_to_stream_0_0_3_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 25), (self.blocks_vector_to_stream_0_0_3_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 30), (self.blocks_vector_to_stream_0_0_3_0_0_0_0_0, 0))
        self.connect((self.epy_block_0_1_0, 35), (self.blocks_vector_to_stream_0_0_3_0_0_0_0_0_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.epy_block_0_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.epy_block_0_1_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.analog_agc2_xx_0, 0))
        self.connect((self.high_pass_filter_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.high_pass_filter_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_freq_sink_x_1, 0))
        self.installEventFilter(self)
    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Ether_Gnu_Radio_Companion")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume_cordes_saved(self):
        return self.volume_cordes_saved

    def set_volume_cordes_saved(self, volume_cordes_saved):
        self.volume_cordes_saved = volume_cordes_saved
        self.set_volume_cordes_slider(self.volume_cordes_saved)

    def get_radio_frequency_center_menu(self):
        return self.radio_frequency_center_menu

    def set_radio_frequency_center_menu(self, radio_frequency_center_menu):
        self.radio_frequency_center_menu = radio_frequency_center_menu
        self.set_radio_frequency_center(self.radio_frequency_center_menu)
        self._radio_frequency_center_menu_callback(self.radio_frequency_center_menu)

    def get_radio_frequency__delta_MHz(self):
        return self.radio_frequency__delta_MHz

    def set_radio_frequency__delta_MHz(self, radio_frequency__delta_MHz):
        self.radio_frequency__delta_MHz = radio_frequency__delta_MHz
        self.set_WBFM_Receive_PLL_Audio_Decimation_0(self.radio_frequency__delta_MHz * 1e6)
        self.set_radio_frequency_delta(self.radio_frequency__delta_MHz * 1e6)
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.radio_frequency__delta_MHz*1e6)

    def get_volume_headphone_slider(self):
        return self.volume_headphone_slider

    def set_volume_headphone_slider(self, volume_headphone_slider):
        self.volume_headphone_slider = volume_headphone_slider
        self.set_volume_headphone(self.volume_headphone_slider * self.volume_headphone_max)

    def get_volume_headphone_max(self):
        return self.volume_headphone_max

    def set_volume_headphone_max(self, volume_headphone_max):
        self.volume_headphone_max = volume_headphone_max
        self.set_volume_headphone(self.volume_headphone_slider * self.volume_headphone_max)

    def get_volume_cordes_slider(self):
        return self.volume_cordes_slider

    def set_volume_cordes_slider(self, volume_cordes_slider):
        self.volume_cordes_slider = volume_cordes_slider
        self.set_volume_cordes(self.volume_cordes_slider * self.volume_cordes_max)
        self._volume_cordes_saved_config = ConfigParser.ConfigParser()
        self._volume_cordes_saved_config.read('Harmonic_frequencies')
        if not self._volume_cordes_saved_config.has_section('main'):
        	self._volume_cordes_saved_config.add_section('main')
        self._volume_cordes_saved_config.set('main', 'volume_cordes_slider', str(self.volume_cordes_slider))
        self._volume_cordes_saved_config.write(open('Harmonic_frequencies', 'w'))

    def get_volume_cordes_max(self):
        return self.volume_cordes_max

    def set_volume_cordes_max(self, volume_cordes_max):
        self.volume_cordes_max = volume_cordes_max
        self.set_volume_cordes(self.volume_cordes_slider * self.volume_cordes_max)

    def get_time_stop_on_frequency_saved(self):
        return self.time_stop_on_frequency_saved

    def set_time_stop_on_frequency_saved(self, time_stop_on_frequency_saved):
        self.time_stop_on_frequency_saved = time_stop_on_frequency_saved
        self.set_time_stop_on_frequency(self.time_stop_on_frequency_saved)

    def get_time_between_frequencies_saved(self):
        return self.time_between_frequencies_saved

    def set_time_between_frequencies_saved(self, time_between_frequencies_saved):
        self.time_between_frequencies_saved = time_between_frequencies_saved
        self.set_time_between_frequencies(self.time_between_frequencies_saved)

    def get_radio_frequency_delta(self):
        return self.radio_frequency_delta

    def set_radio_frequency_delta(self, radio_frequency_delta):
        self.radio_frequency_delta = radio_frequency_delta
        self.set_Frequency(self._Frequency_formatter(str(round((self.radio_frequency_center+self.radio_frequency_delta)*1e-6,3))+ " Mhz"))

    def get_radio_frequency_center(self):
        return self.radio_frequency_center

    def set_radio_frequency_center(self, radio_frequency_center):
        self.radio_frequency_center = radio_frequency_center
        self.set_Frequency(self._Frequency_formatter(str(round((self.radio_frequency_center+self.radio_frequency_delta)*1e-6,3))+ " Mhz"))
        self.qtgui_freq_sink_x_1.set_frequency_range(self.radio_frequency_center, self.radio_sample_rate)
        self.rtlsdr_source_0.set_center_freq(self.radio_frequency_center, 0)

    def get_corde8_frequence5_saved(self):
        return self.corde8_frequence5_saved

    def set_corde8_frequence5_saved(self, corde8_frequence5_saved):
        self.corde8_frequence5_saved = corde8_frequence5_saved
        self.set_corde8_frequence5(self.corde8_frequence5_saved)

    def get_corde8_frequence4_saved(self):
        return self.corde8_frequence4_saved

    def set_corde8_frequence4_saved(self, corde8_frequence4_saved):
        self.corde8_frequence4_saved = corde8_frequence4_saved
        self.set_corde8_frequence4(self.corde8_frequence4_saved)

    def get_corde8_frequence3_saved(self):
        return self.corde8_frequence3_saved

    def set_corde8_frequence3_saved(self, corde8_frequence3_saved):
        self.corde8_frequence3_saved = corde8_frequence3_saved
        self.set_corde8_frequence3(self.corde8_frequence3_saved)

    def get_corde8_frequence2_saved(self):
        return self.corde8_frequence2_saved

    def set_corde8_frequence2_saved(self, corde8_frequence2_saved):
        self.corde8_frequence2_saved = corde8_frequence2_saved
        self.set_corde8_frequence2(self.corde8_frequence2_saved)

    def get_corde8_frequence1_saved(self):
        return self.corde8_frequence1_saved

    def set_corde8_frequence1_saved(self, corde8_frequence1_saved):
        self.corde8_frequence1_saved = corde8_frequence1_saved
        self.set_corde8_frequence1(self.corde8_frequence1_saved)

    def get_corde7_frequence5_saved(self):
        return self.corde7_frequence5_saved

    def set_corde7_frequence5_saved(self, corde7_frequence5_saved):
        self.corde7_frequence5_saved = corde7_frequence5_saved
        self.set_corde7_frequence5(self.corde7_frequence5_saved)

    def get_corde7_frequence4_saved(self):
        return self.corde7_frequence4_saved

    def set_corde7_frequence4_saved(self, corde7_frequence4_saved):
        self.corde7_frequence4_saved = corde7_frequence4_saved
        self.set_corde7_frequence4(self.corde7_frequence4_saved)

    def get_corde7_frequence3_saved(self):
        return self.corde7_frequence3_saved

    def set_corde7_frequence3_saved(self, corde7_frequence3_saved):
        self.corde7_frequence3_saved = corde7_frequence3_saved
        self.set_corde7_frequence3(self.corde7_frequence3_saved)

    def get_corde7_frequence2_saved(self):
        return self.corde7_frequence2_saved

    def set_corde7_frequence2_saved(self, corde7_frequence2_saved):
        self.corde7_frequence2_saved = corde7_frequence2_saved
        self.set_corde7_frequence2(self.corde7_frequence2_saved)

    def get_corde7_frequence1_saved(self):
        return self.corde7_frequence1_saved

    def set_corde7_frequence1_saved(self, corde7_frequence1_saved):
        self.corde7_frequence1_saved = corde7_frequence1_saved
        self.set_corde7_frequence1(self.corde7_frequence1_saved)

    def get_corde6_frequence5_saved(self):
        return self.corde6_frequence5_saved

    def set_corde6_frequence5_saved(self, corde6_frequence5_saved):
        self.corde6_frequence5_saved = corde6_frequence5_saved
        self.set_corde6_frequence5(self.corde6_frequence5_saved)

    def get_corde6_frequence4_saved(self):
        return self.corde6_frequence4_saved

    def set_corde6_frequence4_saved(self, corde6_frequence4_saved):
        self.corde6_frequence4_saved = corde6_frequence4_saved
        self.set_corde6_frequence4(self.corde6_frequence4_saved)

    def get_corde6_frequence3_saved(self):
        return self.corde6_frequence3_saved

    def set_corde6_frequence3_saved(self, corde6_frequence3_saved):
        self.corde6_frequence3_saved = corde6_frequence3_saved
        self.set_corde6_frequence3(self.corde6_frequence3_saved)

    def get_corde6_frequence2_saved(self):
        return self.corde6_frequence2_saved

    def set_corde6_frequence2_saved(self, corde6_frequence2_saved):
        self.corde6_frequence2_saved = corde6_frequence2_saved
        self.set_corde6_frequence2(self.corde6_frequence2_saved)

    def get_corde6_frequence1_saved(self):
        return self.corde6_frequence1_saved

    def set_corde6_frequence1_saved(self, corde6_frequence1_saved):
        self.corde6_frequence1_saved = corde6_frequence1_saved
        self.set_corde6_frequence1(self.corde6_frequence1_saved)

    def get_corde5_frequence5_saved(self):
        return self.corde5_frequence5_saved

    def set_corde5_frequence5_saved(self, corde5_frequence5_saved):
        self.corde5_frequence5_saved = corde5_frequence5_saved
        self.set_corde5_frequence5(self.corde5_frequence5_saved)

    def get_corde5_frequence4_saved(self):
        return self.corde5_frequence4_saved

    def set_corde5_frequence4_saved(self, corde5_frequence4_saved):
        self.corde5_frequence4_saved = corde5_frequence4_saved
        self.set_corde5_frequence4(self.corde5_frequence4_saved)

    def get_corde5_frequence3_saved(self):
        return self.corde5_frequence3_saved

    def set_corde5_frequence3_saved(self, corde5_frequence3_saved):
        self.corde5_frequence3_saved = corde5_frequence3_saved
        self.set_corde5_frequence3(self.corde5_frequence3_saved)

    def get_corde5_frequence2_saved(self):
        return self.corde5_frequence2_saved

    def set_corde5_frequence2_saved(self, corde5_frequence2_saved):
        self.corde5_frequence2_saved = corde5_frequence2_saved
        self.set_corde5_frequence2(self.corde5_frequence2_saved)

    def get_corde5_frequence1_saved(self):
        return self.corde5_frequence1_saved

    def set_corde5_frequence1_saved(self, corde5_frequence1_saved):
        self.corde5_frequence1_saved = corde5_frequence1_saved
        self.set_corde5_frequence1(self.corde5_frequence1_saved)

    def get_corde4_frequence5_saved(self):
        return self.corde4_frequence5_saved

    def set_corde4_frequence5_saved(self, corde4_frequence5_saved):
        self.corde4_frequence5_saved = corde4_frequence5_saved
        self.set_corde4_frequence5(self.corde4_frequence5_saved)

    def get_corde4_frequence4_saved(self):
        return self.corde4_frequence4_saved

    def set_corde4_frequence4_saved(self, corde4_frequence4_saved):
        self.corde4_frequence4_saved = corde4_frequence4_saved
        self.set_corde4_frequence4(self.corde4_frequence4_saved)

    def get_corde4_frequence3_saved(self):
        return self.corde4_frequence3_saved

    def set_corde4_frequence3_saved(self, corde4_frequence3_saved):
        self.corde4_frequence3_saved = corde4_frequence3_saved
        self.set_corde4_frequence3(self.corde4_frequence3_saved)

    def get_corde4_frequence2_saved(self):
        return self.corde4_frequence2_saved

    def set_corde4_frequence2_saved(self, corde4_frequence2_saved):
        self.corde4_frequence2_saved = corde4_frequence2_saved
        self.set_corde4_frequence2(self.corde4_frequence2_saved)

    def get_corde3_frequence5_saved(self):
        return self.corde3_frequence5_saved

    def set_corde3_frequence5_saved(self, corde3_frequence5_saved):
        self.corde3_frequence5_saved = corde3_frequence5_saved
        self.set_corde3_frequence5(self.corde3_frequence5_saved)

    def get_corde3_frequence4_saved(self):
        return self.corde3_frequence4_saved

    def set_corde3_frequence4_saved(self, corde3_frequence4_saved):
        self.corde3_frequence4_saved = corde3_frequence4_saved
        self.set_corde3_frequence4(self.corde3_frequence4_saved)

    def get_corde3_frequence3_saved(self):
        return self.corde3_frequence3_saved

    def set_corde3_frequence3_saved(self, corde3_frequence3_saved):
        self.corde3_frequence3_saved = corde3_frequence3_saved
        self.set_corde3_frequence3(self.corde3_frequence3_saved)

    def get_corde3_frequence2_saved(self):
        return self.corde3_frequence2_saved

    def set_corde3_frequence2_saved(self, corde3_frequence2_saved):
        self.corde3_frequence2_saved = corde3_frequence2_saved
        self.set_corde3_frequence2(self.corde3_frequence2_saved)

    def get_corde3_frequence1_saved(self):
        return self.corde3_frequence1_saved

    def set_corde3_frequence1_saved(self, corde3_frequence1_saved):
        self.corde3_frequence1_saved = corde3_frequence1_saved
        self.set_corde3_frequence1(self.corde3_frequence1_saved)

    def get_corde2_frequence5_saved(self):
        return self.corde2_frequence5_saved

    def set_corde2_frequence5_saved(self, corde2_frequence5_saved):
        self.corde2_frequence5_saved = corde2_frequence5_saved
        self.set_corde2_frequence5(self.corde2_frequence5_saved)

    def get_corde2_frequence4_saved(self):
        return self.corde2_frequence4_saved

    def set_corde2_frequence4_saved(self, corde2_frequence4_saved):
        self.corde2_frequence4_saved = corde2_frequence4_saved
        self.set_corde2_frequence4(self.corde2_frequence4_saved)

    def get_corde2_frequence3_saved(self):
        return self.corde2_frequence3_saved

    def set_corde2_frequence3_saved(self, corde2_frequence3_saved):
        self.corde2_frequence3_saved = corde2_frequence3_saved
        self.set_corde2_frequence3(self.corde2_frequence3_saved)

    def get_corde2_frequence2_saved(self):
        return self.corde2_frequence2_saved

    def set_corde2_frequence2_saved(self, corde2_frequence2_saved):
        self.corde2_frequence2_saved = corde2_frequence2_saved
        self.set_corde2_frequence2(self.corde2_frequence2_saved)

    def get_corde2_frequence1_saved(self):
        return self.corde2_frequence1_saved

    def set_corde2_frequence1_saved(self, corde2_frequence1_saved):
        self.corde2_frequence1_saved = corde2_frequence1_saved
        self.set_corde2_frequence1(self.corde2_frequence1_saved)

    def get_corde1_frequence5_saved(self):
        return self.corde1_frequence5_saved

    def set_corde1_frequence5_saved(self, corde1_frequence5_saved):
        self.corde1_frequence5_saved = corde1_frequence5_saved
        self.set_corde1_frequence5(self.corde1_frequence5_saved)

    def get_corde1_frequence4_saved(self):
        return self.corde1_frequence4_saved

    def set_corde1_frequence4_saved(self, corde1_frequence4_saved):
        self.corde1_frequence4_saved = corde1_frequence4_saved
        self.set_corde1_frequence4(self.corde1_frequence4_saved)

    def get_corde1_frequence3_saved(self):
        return self.corde1_frequence3_saved

    def set_corde1_frequence3_saved(self, corde1_frequence3_saved):
        self.corde1_frequence3_saved = corde1_frequence3_saved
        self.set_corde1_frequence3(self.corde1_frequence3_saved)

    def get_corde1_frequence2_saved(self):
        return self.corde1_frequence2_saved

    def set_corde1_frequence2_saved(self, corde1_frequence2_saved):
        self.corde1_frequence2_saved = corde1_frequence2_saved
        self.set_corde1_frequence2(self.corde1_frequence2_saved)

    def get_corde1_frequence1_saved(self):
        return self.corde1_frequence1_saved

    def set_corde1_frequence1_saved(self, corde1_frequence1_saved):
        self.corde1_frequence1_saved = corde1_frequence1_saved
        self.set_corde1_frequence1(self.corde1_frequence1_saved)
        self.set_corde4_frequence1(self.corde1_frequence1_saved)

    def get_audio_sample_rate(self):
        return self.audio_sample_rate

    def set_audio_sample_rate(self, audio_sample_rate):
        self.audio_sample_rate = audio_sample_rate
        self.set_radio_sample_rate(self.audio_sample_rate*self.WBFM_Receive_PLL_Audio_Decimation*self.Low_Pass_Filter_Decimation)
        self.analog_sig_source_x_0.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1_1.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1_2.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1_3.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1_4.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1_5.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1_6.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_1_6_0.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_2.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_3.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_4.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_5.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_6.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_7.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_0_7_0.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_1.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_2.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_3.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_4.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_5.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_6.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_0_6_0.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1_1.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1_2.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1_3.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1_4.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1_5.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1_6.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_1_6_0.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_3.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_4.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_5.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_6.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_7.set_sampling_freq(self.audio_sample_rate)
        self.analog_sig_source_x_0_7_0.set_sampling_freq(self.audio_sample_rate)
        self.high_pass_filter_0.set_taps(firdes.high_pass(1, self.audio_sample_rate, 40.0, 10.0, firdes.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1_0_0.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1_0_0_0.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1_0_0_0_0.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0.set_samp_rate(self.audio_sample_rate)
        self.qtgui_time_sink_x_1_0_0_0_0_0_0_0.set_samp_rate(self.audio_sample_rate)

    def get_WBFM_Receive_PLL_Audio_Decimation(self):
        return self.WBFM_Receive_PLL_Audio_Decimation

    def set_WBFM_Receive_PLL_Audio_Decimation(self, WBFM_Receive_PLL_Audio_Decimation):
        self.WBFM_Receive_PLL_Audio_Decimation = WBFM_Receive_PLL_Audio_Decimation
        self.set_radio_sample_rate(self.audio_sample_rate*self.WBFM_Receive_PLL_Audio_Decimation*self.Low_Pass_Filter_Decimation)

    def get_Low_Pass_Filter_Decimation(self):
        return self.Low_Pass_Filter_Decimation

    def set_Low_Pass_Filter_Decimation(self, Low_Pass_Filter_Decimation):
        self.Low_Pass_Filter_Decimation = Low_Pass_Filter_Decimation
        self.set_radio_sample_rate(self.audio_sample_rate*self.WBFM_Receive_PLL_Audio_Decimation*self.Low_Pass_Filter_Decimation)

    def get_volume_headphone(self):
        return self.volume_headphone

    def set_volume_headphone(self, volume_headphone):
        self.volume_headphone = volume_headphone
        self.blocks_multiply_const_xx_0.set_k(self.volume_headphone)
        self.blocks_multiply_const_xx_0_0.set_k(self.volume_headphone)
        self.blocks_multiply_const_xx_0_0_0.set_k(self.volume_headphone)

    def get_volume_cordes(self):
        return self.volume_cordes

    def set_volume_cordes(self, volume_cordes):
        self.volume_cordes = volume_cordes
        self.blocks_multiply_const_xx_1.set_k(self.volume_cordes)
        self.blocks_multiply_const_xx_1_0.set_k(self.volume_cordes)
        self.blocks_multiply_const_xx_1_0_0.set_k(self.volume_cordes)
        self.blocks_multiply_const_xx_1_0_0_0.set_k(self.volume_cordes)
        self.blocks_multiply_const_xx_1_0_1.set_k(self.volume_cordes)
        self.blocks_multiply_const_xx_1_1.set_k(self.volume_cordes)
        self.blocks_multiply_const_xx_1_1_0.set_k(self.volume_cordes)
        self.blocks_multiply_const_xx_1_2.set_k(self.volume_cordes)

    def get_time_stop_on_frequency(self):
        return self.time_stop_on_frequency

    def set_time_stop_on_frequency(self, time_stop_on_frequency):
        self.time_stop_on_frequency = time_stop_on_frequency
        self._time_stop_on_frequency_saved_config = ConfigParser.ConfigParser()
        self._time_stop_on_frequency_saved_config.read('Harmonic_frequencies')
        if not self._time_stop_on_frequency_saved_config.has_section('main'):
        	self._time_stop_on_frequency_saved_config.add_section('main')
        self._time_stop_on_frequency_saved_config.set('main', 'time_stop_on_frequency', str(self.time_stop_on_frequency))
        self._time_stop_on_frequency_saved_config.write(open('Harmonic_frequencies', 'w'))

    def get_time_between_frequencies(self):
        return self.time_between_frequencies

    def set_time_between_frequencies(self, time_between_frequencies):
        self.time_between_frequencies = time_between_frequencies
        self._time_between_frequencies_saved_config = ConfigParser.ConfigParser()
        self._time_between_frequencies_saved_config.read('Harmonic_frequencies')
        if not self._time_between_frequencies_saved_config.has_section('main'):
        	self._time_between_frequencies_saved_config.add_section('main')
        self._time_between_frequencies_saved_config.set('main', 'time_between_frequencies', str(self.time_between_frequencies))
        self._time_between_frequencies_saved_config.write(open('Harmonic_frequencies', 'w'))

    def get_radio_scann(self):
        return self.radio_scann

    def set_radio_scann(self, radio_scann):
        self.radio_scann = radio_scann
        self._radio_scann_callback(self.radio_scann)

    def get_radio_sample_rate(self):
        return self.radio_sample_rate

    def set_radio_sample_rate(self, radio_sample_rate):
        self.radio_sample_rate = radio_sample_rate
        self.freq_xlating_fir_filter_xxx_0.set_taps( firdes.low_pass_2(1,self.radio_sample_rate,self.Low_Pass_Filter_cut_of_frequency,self.Low_Pass_Filter_Transition_Width,40))
        self.qtgui_freq_sink_x_1.set_frequency_range(self.radio_frequency_center, self.radio_sample_rate)
        self.rtlsdr_source_0.set_sample_rate(self.radio_sample_rate)

    def get_radio_on_cordes(self):
        return self.radio_on_cordes

    def set_radio_on_cordes(self, radio_on_cordes):
        self.radio_on_cordes = radio_on_cordes
        self._radio_on_cordes_callback(self.radio_on_cordes)
        self.epy_block_0_1_0.on_off = self.radio_on_cordes

    def get_corde8_frequence5(self):
        return self.corde8_frequence5

    def set_corde8_frequence5(self, corde8_frequence5):
        self.corde8_frequence5 = corde8_frequence5
        self._corde8_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde8_frequence5_saved_config.has_section('main'):
        	self._corde8_frequence5_saved_config.add_section('main')
        self._corde8_frequence5_saved_config.set('main', 'corde8_frequence5', str(self.corde8_frequence5))
        self._corde8_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1_6_0.set_frequency(self.corde8_frequence5)

    def get_corde8_frequence4(self):
        return self.corde8_frequence4

    def set_corde8_frequence4(self, corde8_frequence4):
        self.corde8_frequence4 = corde8_frequence4
        self._corde8_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde8_frequence4_saved_config.has_section('main'):
        	self._corde8_frequence4_saved_config.add_section('main')
        self._corde8_frequence4_saved_config.set('main', 'corde8_frequence4', str(self.corde8_frequence4))
        self._corde8_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_7_0.set_frequency(self.corde8_frequence4)

    def get_corde8_frequence3(self):
        return self.corde8_frequence3

    def set_corde8_frequence3(self, corde8_frequence3):
        self.corde8_frequence3 = corde8_frequence3
        self._corde8_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde8_frequence3_saved_config.has_section('main'):
        	self._corde8_frequence3_saved_config.add_section('main')
        self._corde8_frequence3_saved_config.set('main', 'corde8_frequence3', str(self.corde8_frequence3))
        self._corde8_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1_6_0.set_frequency(self.corde8_frequence3)

    def get_corde8_frequence2(self):
        return self.corde8_frequence2

    def set_corde8_frequence2(self, corde8_frequence2):
        self.corde8_frequence2 = corde8_frequence2
        self._corde8_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde8_frequence2_saved_config.has_section('main'):
        	self._corde8_frequence2_saved_config.add_section('main')
        self._corde8_frequence2_saved_config.set('main', 'corde8_frequence2', str(self.corde8_frequence2))
        self._corde8_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_6_0.set_frequency(self.corde8_frequence2)

    def get_corde8_frequence1(self):
        return self.corde8_frequence1

    def set_corde8_frequence1(self, corde8_frequence1):
        self.corde8_frequence1 = corde8_frequence1
        self._corde8_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde8_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde8_frequence1_saved_config.has_section('main'):
        	self._corde8_frequence1_saved_config.add_section('main')
        self._corde8_frequence1_saved_config.set('main', 'corde8_frequence1', str(self.corde8_frequence1))
        self._corde8_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_7_0.set_frequency(self.corde8_frequence1)

    def get_corde8_amplitude5(self):
        return self.corde8_amplitude5

    def set_corde8_amplitude5(self, corde8_amplitude5):
        self.corde8_amplitude5 = corde8_amplitude5
        self._corde8_amplitude5_callback(self.corde8_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_6_0.set_k(self.corde8_amplitude5)

    def get_corde8_amplitude4(self):
        return self.corde8_amplitude4

    def set_corde8_amplitude4(self, corde8_amplitude4):
        self.corde8_amplitude4 = corde8_amplitude4
        self._corde8_amplitude4_callback(self.corde8_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_7_0.set_k(self.corde8_amplitude4)

    def get_corde8_amplitude3(self):
        return self.corde8_amplitude3

    def set_corde8_amplitude3(self, corde8_amplitude3):
        self.corde8_amplitude3 = corde8_amplitude3
        self._corde8_amplitude3_callback(self.corde8_amplitude3)
        self.blocks_add_const_vxx_0_2_6_0.set_k(self.corde8_amplitude3)

    def get_corde8_amplitude2(self):
        return self.corde8_amplitude2

    def set_corde8_amplitude2(self, corde8_amplitude2):
        self.corde8_amplitude2 = corde8_amplitude2
        self._corde8_amplitude2_callback(self.corde8_amplitude2)
        self.blocks_add_const_vxx_0_0_1_6_0.set_k(self.corde8_amplitude2)

    def get_corde8_amplitude1(self):
        return self.corde8_amplitude1

    def set_corde8_amplitude1(self, corde8_amplitude1):
        self.corde8_amplitude1 = corde8_amplitude1
        self._corde8_amplitude1_callback(self.corde8_amplitude1)
        self.blocks_add_const_vxx_0_1_5_0.set_k(self.corde8_amplitude1)

    def get_corde7_frequence5(self):
        return self.corde7_frequence5

    def set_corde7_frequence5(self, corde7_frequence5):
        self.corde7_frequence5 = corde7_frequence5
        self._corde7_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde7_frequence5_saved_config.has_section('main'):
        	self._corde7_frequence5_saved_config.add_section('main')
        self._corde7_frequence5_saved_config.set('main', 'corde7_frequence5', str(self.corde7_frequence5))
        self._corde7_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1_6.set_frequency(self.corde7_frequence5)

    def get_corde7_frequence4(self):
        return self.corde7_frequence4

    def set_corde7_frequence4(self, corde7_frequence4):
        self.corde7_frequence4 = corde7_frequence4
        self._corde7_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde7_frequence4_saved_config.has_section('main'):
        	self._corde7_frequence4_saved_config.add_section('main')
        self._corde7_frequence4_saved_config.set('main', 'corde7_frequence4', str(self.corde7_frequence4))
        self._corde7_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_7.set_frequency(self.corde7_frequence4)

    def get_corde7_frequence3(self):
        return self.corde7_frequence3

    def set_corde7_frequence3(self, corde7_frequence3):
        self.corde7_frequence3 = corde7_frequence3
        self._corde7_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde7_frequence3_saved_config.has_section('main'):
        	self._corde7_frequence3_saved_config.add_section('main')
        self._corde7_frequence3_saved_config.set('main', 'corde7_frequence3', str(self.corde7_frequence3))
        self._corde7_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1_6.set_frequency(self.corde7_frequence3)

    def get_corde7_frequence2(self):
        return self.corde7_frequence2

    def set_corde7_frequence2(self, corde7_frequence2):
        self.corde7_frequence2 = corde7_frequence2
        self._corde7_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde7_frequence2_saved_config.has_section('main'):
        	self._corde7_frequence2_saved_config.add_section('main')
        self._corde7_frequence2_saved_config.set('main', 'corde7_frequence2', str(self.corde7_frequence2))
        self._corde7_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_6.set_frequency(self.corde7_frequence2)

    def get_corde7_frequence1(self):
        return self.corde7_frequence1

    def set_corde7_frequence1(self, corde7_frequence1):
        self.corde7_frequence1 = corde7_frequence1
        self._corde7_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde7_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde7_frequence1_saved_config.has_section('main'):
        	self._corde7_frequence1_saved_config.add_section('main')
        self._corde7_frequence1_saved_config.set('main', 'corde7_frequence1', str(self.corde7_frequence1))
        self._corde7_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_7.set_frequency(self.corde7_frequence1)

    def get_corde7_amplitude5(self):
        return self.corde7_amplitude5

    def set_corde7_amplitude5(self, corde7_amplitude5):
        self.corde7_amplitude5 = corde7_amplitude5
        self._corde7_amplitude5_callback(self.corde7_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_6.set_k(self.corde7_amplitude5)

    def get_corde7_amplitude4(self):
        return self.corde7_amplitude4

    def set_corde7_amplitude4(self, corde7_amplitude4):
        self.corde7_amplitude4 = corde7_amplitude4
        self._corde7_amplitude4_callback(self.corde7_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_7.set_k(self.corde7_amplitude4)

    def get_corde7_amplitude3(self):
        return self.corde7_amplitude3

    def set_corde7_amplitude3(self, corde7_amplitude3):
        self.corde7_amplitude3 = corde7_amplitude3
        self._corde7_amplitude3_callback(self.corde7_amplitude3)
        self.blocks_add_const_vxx_0_2_6.set_k(self.corde7_amplitude3)

    def get_corde7_amplitude2(self):
        return self.corde7_amplitude2

    def set_corde7_amplitude2(self, corde7_amplitude2):
        self.corde7_amplitude2 = corde7_amplitude2
        self._corde7_amplitude2_callback(self.corde7_amplitude2)
        self.blocks_add_const_vxx_0_0_1_6.set_k(self.corde7_amplitude2)

    def get_corde7_amplitude1(self):
        return self.corde7_amplitude1

    def set_corde7_amplitude1(self, corde7_amplitude1):
        self.corde7_amplitude1 = corde7_amplitude1
        self._corde7_amplitude1_callback(self.corde7_amplitude1)
        self.blocks_add_const_vxx_0_1_5.set_k(self.corde7_amplitude1)

    def get_corde6_frequence5(self):
        return self.corde6_frequence5

    def set_corde6_frequence5(self, corde6_frequence5):
        self.corde6_frequence5 = corde6_frequence5
        self._corde6_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde6_frequence5_saved_config.has_section('main'):
        	self._corde6_frequence5_saved_config.add_section('main')
        self._corde6_frequence5_saved_config.set('main', 'corde6_frequence5', str(self.corde6_frequence5))
        self._corde6_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1_5.set_frequency(self.corde6_frequence5)

    def get_corde6_frequence4(self):
        return self.corde6_frequence4

    def set_corde6_frequence4(self, corde6_frequence4):
        self.corde6_frequence4 = corde6_frequence4
        self._corde6_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde6_frequence4_saved_config.has_section('main'):
        	self._corde6_frequence4_saved_config.add_section('main')
        self._corde6_frequence4_saved_config.set('main', 'corde6_frequence4', str(self.corde6_frequence4))
        self._corde6_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_6.set_frequency(self.corde6_frequence4)

    def get_corde6_frequence3(self):
        return self.corde6_frequence3

    def set_corde6_frequence3(self, corde6_frequence3):
        self.corde6_frequence3 = corde6_frequence3
        self._corde6_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde6_frequence3_saved_config.has_section('main'):
        	self._corde6_frequence3_saved_config.add_section('main')
        self._corde6_frequence3_saved_config.set('main', 'corde6_frequence3', str(self.corde6_frequence3))
        self._corde6_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1_5.set_frequency(self.corde6_frequence3)

    def get_corde6_frequence2(self):
        return self.corde6_frequence2

    def set_corde6_frequence2(self, corde6_frequence2):
        self.corde6_frequence2 = corde6_frequence2
        self._corde6_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde6_frequence2_saved_config.has_section('main'):
        	self._corde6_frequence2_saved_config.add_section('main')
        self._corde6_frequence2_saved_config.set('main', 'corde6_frequence2', str(self.corde6_frequence2))
        self._corde6_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_5.set_frequency(self.corde6_frequence2)

    def get_corde6_frequence1(self):
        return self.corde6_frequence1

    def set_corde6_frequence1(self, corde6_frequence1):
        self.corde6_frequence1 = corde6_frequence1
        self._corde6_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde6_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde6_frequence1_saved_config.has_section('main'):
        	self._corde6_frequence1_saved_config.add_section('main')
        self._corde6_frequence1_saved_config.set('main', 'corde6_frequence1', str(self.corde6_frequence1))
        self._corde6_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_6.set_frequency(self.corde6_frequence1)

    def get_corde6_amplitude5(self):
        return self.corde6_amplitude5

    def set_corde6_amplitude5(self, corde6_amplitude5):
        self.corde6_amplitude5 = corde6_amplitude5
        self._corde6_amplitude5_callback(self.corde6_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_5.set_k(self.corde6_amplitude5)

    def get_corde6_amplitude4(self):
        return self.corde6_amplitude4

    def set_corde6_amplitude4(self, corde6_amplitude4):
        self.corde6_amplitude4 = corde6_amplitude4
        self._corde6_amplitude4_callback(self.corde6_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_6.set_k(self.corde6_amplitude4)

    def get_corde6_amplitude3(self):
        return self.corde6_amplitude3

    def set_corde6_amplitude3(self, corde6_amplitude3):
        self.corde6_amplitude3 = corde6_amplitude3
        self._corde6_amplitude3_callback(self.corde6_amplitude3)
        self.blocks_add_const_vxx_0_2_5.set_k(self.corde6_amplitude3)

    def get_corde6_amplitude2(self):
        return self.corde6_amplitude2

    def set_corde6_amplitude2(self, corde6_amplitude2):
        self.corde6_amplitude2 = corde6_amplitude2
        self._corde6_amplitude2_callback(self.corde6_amplitude2)
        self.blocks_add_const_vxx_0_0_1_5.set_k(self.corde6_amplitude2)

    def get_corde6_amplitude1(self):
        return self.corde6_amplitude1

    def set_corde6_amplitude1(self, corde6_amplitude1):
        self.corde6_amplitude1 = corde6_amplitude1
        self._corde6_amplitude1_callback(self.corde6_amplitude1)
        self.blocks_add_const_vxx_0_1_4.set_k(self.corde6_amplitude1)

    def get_corde5_frequence5(self):
        return self.corde5_frequence5

    def set_corde5_frequence5(self, corde5_frequence5):
        self.corde5_frequence5 = corde5_frequence5
        self._corde5_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde5_frequence5_saved_config.has_section('main'):
        	self._corde5_frequence5_saved_config.add_section('main')
        self._corde5_frequence5_saved_config.set('main', 'corde5_frequence5', str(self.corde5_frequence5))
        self._corde5_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1_4.set_frequency(self.corde5_frequence5)

    def get_corde5_frequence4(self):
        return self.corde5_frequence4

    def set_corde5_frequence4(self, corde5_frequence4):
        self.corde5_frequence4 = corde5_frequence4
        self._corde5_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde5_frequence4_saved_config.has_section('main'):
        	self._corde5_frequence4_saved_config.add_section('main')
        self._corde5_frequence4_saved_config.set('main', 'corde5_frequence4', str(self.corde5_frequence4))
        self._corde5_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_5.set_frequency(self.corde5_frequence4)

    def get_corde5_frequence3(self):
        return self.corde5_frequence3

    def set_corde5_frequence3(self, corde5_frequence3):
        self.corde5_frequence3 = corde5_frequence3
        self._corde5_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde5_frequence3_saved_config.has_section('main'):
        	self._corde5_frequence3_saved_config.add_section('main')
        self._corde5_frequence3_saved_config.set('main', 'corde5_frequence3', str(self.corde5_frequence3))
        self._corde5_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1_4.set_frequency(self.corde5_frequence3)

    def get_corde5_frequence2(self):
        return self.corde5_frequence2

    def set_corde5_frequence2(self, corde5_frequence2):
        self.corde5_frequence2 = corde5_frequence2
        self._corde5_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde5_frequence2_saved_config.has_section('main'):
        	self._corde5_frequence2_saved_config.add_section('main')
        self._corde5_frequence2_saved_config.set('main', 'corde5_frequence2', str(self.corde5_frequence2))
        self._corde5_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_4.set_frequency(self.corde5_frequence2)

    def get_corde5_frequence1(self):
        return self.corde5_frequence1

    def set_corde5_frequence1(self, corde5_frequence1):
        self.corde5_frequence1 = corde5_frequence1
        self._corde5_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde5_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde5_frequence1_saved_config.has_section('main'):
        	self._corde5_frequence1_saved_config.add_section('main')
        self._corde5_frequence1_saved_config.set('main', 'corde5_frequence1', str(self.corde5_frequence1))
        self._corde5_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_5.set_frequency(self.corde5_frequence1)

    def get_corde5_amplitude5(self):
        return self.corde5_amplitude5

    def set_corde5_amplitude5(self, corde5_amplitude5):
        self.corde5_amplitude5 = corde5_amplitude5
        self._corde5_amplitude5_callback(self.corde5_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_4.set_k(self.corde5_amplitude5)

    def get_corde5_amplitude4(self):
        return self.corde5_amplitude4

    def set_corde5_amplitude4(self, corde5_amplitude4):
        self.corde5_amplitude4 = corde5_amplitude4
        self._corde5_amplitude4_callback(self.corde5_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_5.set_k(self.corde5_amplitude4)

    def get_corde5_amplitude3(self):
        return self.corde5_amplitude3

    def set_corde5_amplitude3(self, corde5_amplitude3):
        self.corde5_amplitude3 = corde5_amplitude3
        self._corde5_amplitude3_callback(self.corde5_amplitude3)
        self.blocks_add_const_vxx_0_2_4.set_k(self.corde5_amplitude3)

    def get_corde5_amplitude2(self):
        return self.corde5_amplitude2

    def set_corde5_amplitude2(self, corde5_amplitude2):
        self.corde5_amplitude2 = corde5_amplitude2
        self._corde5_amplitude2_callback(self.corde5_amplitude2)
        self.blocks_add_const_vxx_0_0_1_4.set_k(self.corde5_amplitude2)

    def get_corde5_amplitude1(self):
        return self.corde5_amplitude1

    def set_corde5_amplitude1(self, corde5_amplitude1):
        self.corde5_amplitude1 = corde5_amplitude1
        self._corde5_amplitude1_callback(self.corde5_amplitude1)
        self.blocks_add_const_vxx_0_1_3.set_k(self.corde5_amplitude1)

    def get_corde4_frequence5(self):
        return self.corde4_frequence5

    def set_corde4_frequence5(self, corde4_frequence5):
        self.corde4_frequence5 = corde4_frequence5
        self._corde4_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde4_frequence5_saved_config.has_section('main'):
        	self._corde4_frequence5_saved_config.add_section('main')
        self._corde4_frequence5_saved_config.set('main', 'corde4_frequence5', str(self.corde4_frequence5))
        self._corde4_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1_3.set_frequency(self.corde4_frequence5)

    def get_corde4_frequence4(self):
        return self.corde4_frequence4

    def set_corde4_frequence4(self, corde4_frequence4):
        self.corde4_frequence4 = corde4_frequence4
        self._corde4_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde4_frequence4_saved_config.has_section('main'):
        	self._corde4_frequence4_saved_config.add_section('main')
        self._corde4_frequence4_saved_config.set('main', 'corde4_frequence4', str(self.corde4_frequence4))
        self._corde4_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_4.set_frequency(self.corde4_frequence4)

    def get_corde4_frequence3(self):
        return self.corde4_frequence3

    def set_corde4_frequence3(self, corde4_frequence3):
        self.corde4_frequence3 = corde4_frequence3
        self._corde4_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde4_frequence3_saved_config.has_section('main'):
        	self._corde4_frequence3_saved_config.add_section('main')
        self._corde4_frequence3_saved_config.set('main', 'corde4_frequence3', str(self.corde4_frequence3))
        self._corde4_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1_3.set_frequency(self.corde4_frequence3)

    def get_corde4_frequence2(self):
        return self.corde4_frequence2

    def set_corde4_frequence2(self, corde4_frequence2):
        self.corde4_frequence2 = corde4_frequence2
        self._corde4_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde4_frequence2_saved_config.has_section('main'):
        	self._corde4_frequence2_saved_config.add_section('main')
        self._corde4_frequence2_saved_config.set('main', 'corde4_frequence2', str(self.corde4_frequence2))
        self._corde4_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_3.set_frequency(self.corde4_frequence2)

    def get_corde4_frequence1_saved(self):
        return self.corde4_frequence1_saved

    def set_corde4_frequence1_saved(self, corde4_frequence1_saved):
        self.corde4_frequence1_saved = corde4_frequence1_saved

    def get_corde4_frequence1(self):
        return self.corde4_frequence1

    def set_corde4_frequence1(self, corde4_frequence1):
        self.corde4_frequence1 = corde4_frequence1
        self._corde4_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde4_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde4_frequence1_saved_config.has_section('main'):
        	self._corde4_frequence1_saved_config.add_section('main')
        self._corde4_frequence1_saved_config.set('main', 'corde4_frequence1', str(self.corde4_frequence1))
        self._corde4_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_4.set_frequency(self.corde4_frequence1)

    def get_corde4_amplitude5(self):
        return self.corde4_amplitude5

    def set_corde4_amplitude5(self, corde4_amplitude5):
        self.corde4_amplitude5 = corde4_amplitude5
        self._corde4_amplitude5_callback(self.corde4_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_3.set_k(self.corde4_amplitude5)

    def get_corde4_amplitude4(self):
        return self.corde4_amplitude4

    def set_corde4_amplitude4(self, corde4_amplitude4):
        self.corde4_amplitude4 = corde4_amplitude4
        self._corde4_amplitude4_callback(self.corde4_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_4.set_k(self.corde4_amplitude4)

    def get_corde4_amplitude3(self):
        return self.corde4_amplitude3

    def set_corde4_amplitude3(self, corde4_amplitude3):
        self.corde4_amplitude3 = corde4_amplitude3
        self._corde4_amplitude3_callback(self.corde4_amplitude3)
        self.blocks_add_const_vxx_0_2_3.set_k(self.corde4_amplitude3)

    def get_corde4_amplitude2(self):
        return self.corde4_amplitude2

    def set_corde4_amplitude2(self, corde4_amplitude2):
        self.corde4_amplitude2 = corde4_amplitude2
        self._corde4_amplitude2_callback(self.corde4_amplitude2)
        self.blocks_add_const_vxx_0_0_1_3.set_k(self.corde4_amplitude2)

    def get_corde4_amplitude1(self):
        return self.corde4_amplitude1

    def set_corde4_amplitude1(self, corde4_amplitude1):
        self.corde4_amplitude1 = corde4_amplitude1
        self._corde4_amplitude1_callback(self.corde4_amplitude1)
        self.blocks_add_const_vxx_0_1_2.set_k(self.corde4_amplitude1)

    def get_corde3_frequence5(self):
        return self.corde3_frequence5

    def set_corde3_frequence5(self, corde3_frequence5):
        self.corde3_frequence5 = corde3_frequence5
        self._corde3_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde3_frequence5_saved_config.has_section('main'):
        	self._corde3_frequence5_saved_config.add_section('main')
        self._corde3_frequence5_saved_config.set('main', 'corde3_frequence5', str(self.corde3_frequence5))
        self._corde3_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1_2.set_frequency(self.corde3_frequence5)

    def get_corde3_frequence4(self):
        return self.corde3_frequence4

    def set_corde3_frequence4(self, corde3_frequence4):
        self.corde3_frequence4 = corde3_frequence4
        self._corde3_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde3_frequence4_saved_config.has_section('main'):
        	self._corde3_frequence4_saved_config.add_section('main')
        self._corde3_frequence4_saved_config.set('main', 'corde3_frequence4', str(self.corde3_frequence4))
        self._corde3_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_3.set_frequency(self.corde3_frequence4)

    def get_corde3_frequence3(self):
        return self.corde3_frequence3

    def set_corde3_frequence3(self, corde3_frequence3):
        self.corde3_frequence3 = corde3_frequence3
        self._corde3_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde3_frequence3_saved_config.has_section('main'):
        	self._corde3_frequence3_saved_config.add_section('main')
        self._corde3_frequence3_saved_config.set('main', 'corde3_frequence3', str(self.corde3_frequence3))
        self._corde3_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1_2.set_frequency(self.corde3_frequence3)

    def get_corde3_frequence2(self):
        return self.corde3_frequence2

    def set_corde3_frequence2(self, corde3_frequence2):
        self.corde3_frequence2 = corde3_frequence2
        self._corde3_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde3_frequence2_saved_config.has_section('main'):
        	self._corde3_frequence2_saved_config.add_section('main')
        self._corde3_frequence2_saved_config.set('main', 'corde3_frequence2', str(self.corde3_frequence2))
        self._corde3_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_2.set_frequency(self.corde3_frequence2)

    def get_corde3_frequence1(self):
        return self.corde3_frequence1

    def set_corde3_frequence1(self, corde3_frequence1):
        self.corde3_frequence1 = corde3_frequence1
        self._corde3_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde3_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde3_frequence1_saved_config.has_section('main'):
        	self._corde3_frequence1_saved_config.add_section('main')
        self._corde3_frequence1_saved_config.set('main', 'corde3_frequence1', str(self.corde3_frequence1))
        self._corde3_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_3.set_frequency(self.corde3_frequence1)

    def get_corde3_amplitude5(self):
        return self.corde3_amplitude5

    def set_corde3_amplitude5(self, corde3_amplitude5):
        self.corde3_amplitude5 = corde3_amplitude5
        self._corde3_amplitude5_callback(self.corde3_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_2.set_k(self.corde3_amplitude5)

    def get_corde3_amplitude4(self):
        return self.corde3_amplitude4

    def set_corde3_amplitude4(self, corde3_amplitude4):
        self.corde3_amplitude4 = corde3_amplitude4
        self._corde3_amplitude4_callback(self.corde3_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_3.set_k(self.corde3_amplitude4)

    def get_corde3_amplitude3(self):
        return self.corde3_amplitude3

    def set_corde3_amplitude3(self, corde3_amplitude3):
        self.corde3_amplitude3 = corde3_amplitude3
        self._corde3_amplitude3_callback(self.corde3_amplitude3)
        self.blocks_add_const_vxx_0_2_2.set_k(self.corde3_amplitude3)

    def get_corde3_amplitude2(self):
        return self.corde3_amplitude2

    def set_corde3_amplitude2(self, corde3_amplitude2):
        self.corde3_amplitude2 = corde3_amplitude2
        self._corde3_amplitude2_callback(self.corde3_amplitude2)
        self.blocks_add_const_vxx_0_0_1_2.set_k(self.corde3_amplitude2)

    def get_corde3_amplitude1(self):
        return self.corde3_amplitude1

    def set_corde3_amplitude1(self, corde3_amplitude1):
        self.corde3_amplitude1 = corde3_amplitude1
        self._corde3_amplitude1_callback(self.corde3_amplitude1)
        self.blocks_add_const_vxx_0_1_1.set_k(self.corde3_amplitude1)

    def get_corde2_frequence5(self):
        return self.corde2_frequence5

    def set_corde2_frequence5(self, corde2_frequence5):
        self.corde2_frequence5 = corde2_frequence5
        self._corde2_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde2_frequence5_saved_config.has_section('main'):
        	self._corde2_frequence5_saved_config.add_section('main')
        self._corde2_frequence5_saved_config.set('main', 'corde2_frequence5', str(self.corde2_frequence5))
        self._corde2_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1_1.set_frequency(self.corde2_frequence5)

    def get_corde2_frequence4(self):
        return self.corde2_frequence4

    def set_corde2_frequence4(self, corde2_frequence4):
        self.corde2_frequence4 = corde2_frequence4
        self._corde2_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde2_frequence4_saved_config.has_section('main'):
        	self._corde2_frequence4_saved_config.add_section('main')
        self._corde2_frequence4_saved_config.set('main', 'corde2_frequence4', str(self.corde2_frequence4))
        self._corde2_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_2.set_frequency(self.corde2_frequence4)

    def get_corde2_frequence3(self):
        return self.corde2_frequence3

    def set_corde2_frequence3(self, corde2_frequence3):
        self.corde2_frequence3 = corde2_frequence3
        self._corde2_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde2_frequence3_saved_config.has_section('main'):
        	self._corde2_frequence3_saved_config.add_section('main')
        self._corde2_frequence3_saved_config.set('main', 'corde2_frequence3', str(self.corde2_frequence3))
        self._corde2_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1_1.set_frequency(self.corde2_frequence3)

    def get_corde2_frequence2(self):
        return self.corde2_frequence2

    def set_corde2_frequence2(self, corde2_frequence2):
        self.corde2_frequence2 = corde2_frequence2
        self._corde2_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde2_frequence2_saved_config.has_section('main'):
        	self._corde2_frequence2_saved_config.add_section('main')
        self._corde2_frequence2_saved_config.set('main', 'corde2_frequence2', str(self.corde2_frequence2))
        self._corde2_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_1.set_frequency(self.corde2_frequence2)

    def get_corde2_frequence1(self):
        return self.corde2_frequence1

    def set_corde2_frequence1(self, corde2_frequence1):
        self.corde2_frequence1 = corde2_frequence1
        self._corde2_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde2_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde2_frequence1_saved_config.has_section('main'):
        	self._corde2_frequence1_saved_config.add_section('main')
        self._corde2_frequence1_saved_config.set('main', 'corde2_frequence1', str(self.corde2_frequence1))
        self._corde2_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_2.set_frequency(self.corde2_frequence1)

    def get_corde2_amplitude5(self):
        return self.corde2_amplitude5

    def set_corde2_amplitude5(self, corde2_amplitude5):
        self.corde2_amplitude5 = corde2_amplitude5
        self._corde2_amplitude5_callback(self.corde2_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1_1.set_k(self.corde2_amplitude5)

    def get_corde2_amplitude4(self):
        return self.corde2_amplitude4

    def set_corde2_amplitude4(self, corde2_amplitude4):
        self.corde2_amplitude4 = corde2_amplitude4
        self._corde2_amplitude4_callback(self.corde2_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0_2.set_k(self.corde2_amplitude4)

    def get_corde2_amplitude3(self):
        return self.corde2_amplitude3

    def set_corde2_amplitude3(self, corde2_amplitude3):
        self.corde2_amplitude3 = corde2_amplitude3
        self._corde2_amplitude3_callback(self.corde2_amplitude3)
        self.blocks_add_const_vxx_0_2_1.set_k(self.corde2_amplitude3)

    def get_corde2_amplitude2(self):
        return self.corde2_amplitude2

    def set_corde2_amplitude2(self, corde2_amplitude2):
        self.corde2_amplitude2 = corde2_amplitude2
        self._corde2_amplitude2_callback(self.corde2_amplitude2)
        self.blocks_add_const_vxx_0_0_1_1.set_k(self.corde2_amplitude2)

    def get_corde2_amplitude1(self):
        return self.corde2_amplitude1

    def set_corde2_amplitude1(self, corde2_amplitude1):
        self.corde2_amplitude1 = corde2_amplitude1
        self._corde2_amplitude1_callback(self.corde2_amplitude1)
        self.blocks_add_const_vxx_0_1_0.set_k(self.corde2_amplitude1)

    def get_corde1_frequence5(self):
        return self.corde1_frequence5

    def set_corde1_frequence5(self, corde1_frequence5):
        self.corde1_frequence5 = corde1_frequence5
        self._corde1_frequence5_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence5_saved_config.read('Harmonic_frequencies')
        if not self._corde1_frequence5_saved_config.has_section('main'):
        	self._corde1_frequence5_saved_config.add_section('main')
        self._corde1_frequence5_saved_config.set('main', 'corde1_frequence5', str(self.corde1_frequence5))
        self._corde1_frequence5_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0_1.set_frequency(self.corde1_frequence5)

    def get_corde1_frequence4(self):
        return self.corde1_frequence4

    def set_corde1_frequence4(self, corde1_frequence4):
        self.corde1_frequence4 = corde1_frequence4
        self._corde1_frequence4_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence4_saved_config.read('Harmonic_frequencies')
        if not self._corde1_frequence4_saved_config.has_section('main'):
        	self._corde1_frequence4_saved_config.add_section('main')
        self._corde1_frequence4_saved_config.set('main', 'corde1_frequence4', str(self.corde1_frequence4))
        self._corde1_frequence4_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0_0.set_frequency(self.corde1_frequence4)

    def get_corde1_frequence3(self):
        return self.corde1_frequence3

    def set_corde1_frequence3(self, corde1_frequence3):
        self.corde1_frequence3 = corde1_frequence3
        self._corde1_frequence3_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence3_saved_config.read('Harmonic_frequencies')
        if not self._corde1_frequence3_saved_config.has_section('main'):
        	self._corde1_frequence3_saved_config.add_section('main')
        self._corde1_frequence3_saved_config.set('main', 'corde1_frequence3', str(self.corde1_frequence3))
        self._corde1_frequence3_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_1.set_frequency(self.corde1_frequence3)

    def get_corde1_frequence2(self):
        return self.corde1_frequence2

    def set_corde1_frequence2(self, corde1_frequence2):
        self.corde1_frequence2 = corde1_frequence2
        self._corde1_frequence2_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence2_saved_config.read('Harmonic_frequencies')
        if not self._corde1_frequence2_saved_config.has_section('main'):
        	self._corde1_frequence2_saved_config.add_section('main')
        self._corde1_frequence2_saved_config.set('main', 'corde1_frequence2', str(self.corde1_frequence2))
        self._corde1_frequence2_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0_0.set_frequency(self.corde1_frequence2)

    def get_corde1_frequence1(self):
        return self.corde1_frequence1

    def set_corde1_frequence1(self, corde1_frequence1):
        self.corde1_frequence1 = corde1_frequence1
        self._corde1_frequence1_saved_config = ConfigParser.ConfigParser()
        self._corde1_frequence1_saved_config.read('Harmonic_frequencies')
        if not self._corde1_frequence1_saved_config.has_section('main'):
        	self._corde1_frequence1_saved_config.add_section('main')
        self._corde1_frequence1_saved_config.set('main', 'corde1_frequence1', str(self.corde1_frequence1))
        self._corde1_frequence1_saved_config.write(open('Harmonic_frequencies', 'w'))
        self.analog_sig_source_x_0.set_frequency(self.corde1_frequence1)

    def get_corde1_amplitude5(self):
        return self.corde1_amplitude5

    def set_corde1_amplitude5(self, corde1_amplitude5):
        self.corde1_amplitude5 = corde1_amplitude5
        self._corde1_amplitude5_callback(self.corde1_amplitude5)
        self.blocks_add_const_vxx_0_0_1_0_1.set_k(self.corde1_amplitude5)

    def get_corde1_amplitude4(self):
        return self.corde1_amplitude4

    def set_corde1_amplitude4(self, corde1_amplitude4):
        self.corde1_amplitude4 = corde1_amplitude4
        self._corde1_amplitude4_callback(self.corde1_amplitude4)
        self.blocks_add_const_vxx_0_0_1_0.set_k(self.corde1_amplitude4)

    def get_corde1_amplitude3(self):
        return self.corde1_amplitude3

    def set_corde1_amplitude3(self, corde1_amplitude3):
        self.corde1_amplitude3 = corde1_amplitude3
        self._corde1_amplitude3_callback(self.corde1_amplitude3)
        self.blocks_add_const_vxx_0_2.set_k(self.corde1_amplitude3)

    def get_corde1_amplitude2(self):
        return self.corde1_amplitude2

    def set_corde1_amplitude2(self, corde1_amplitude2):
        self.corde1_amplitude2 = corde1_amplitude2
        self._corde1_amplitude2_callback(self.corde1_amplitude2)
        self.blocks_add_const_vxx_0_0_1.set_k(self.corde1_amplitude2)

    def get_corde1_amplitude1(self):
        return self.corde1_amplitude1

    def set_corde1_amplitude1(self, corde1_amplitude1):
        self.corde1_amplitude1 = corde1_amplitude1
        self._corde1_amplitude1_callback(self.corde1_amplitude1)
        self.blocks_add_const_vxx_0_1.set_k(self.corde1_amplitude1)

    def get_WBFM_Receive_PLL_Audio_Decimation_0(self):
        return self.WBFM_Receive_PLL_Audio_Decimation_0

    def set_WBFM_Receive_PLL_Audio_Decimation_0(self, WBFM_Receive_PLL_Audio_Decimation_0):
        self.WBFM_Receive_PLL_Audio_Decimation_0 = WBFM_Receive_PLL_Audio_Decimation_0

    def get_Low_Pass_Filter_cut_of_frequency(self):
        return self.Low_Pass_Filter_cut_of_frequency

    def set_Low_Pass_Filter_cut_of_frequency(self, Low_Pass_Filter_cut_of_frequency):
        self.Low_Pass_Filter_cut_of_frequency = Low_Pass_Filter_cut_of_frequency
        self.freq_xlating_fir_filter_xxx_0.set_taps( firdes.low_pass_2(1,self.radio_sample_rate,self.Low_Pass_Filter_cut_of_frequency,self.Low_Pass_Filter_Transition_Width,40))

    def get_Low_Pass_Filter_Transition_Width(self):
        return self.Low_Pass_Filter_Transition_Width

    def set_Low_Pass_Filter_Transition_Width(self, Low_Pass_Filter_Transition_Width):
        self.Low_Pass_Filter_Transition_Width = Low_Pass_Filter_Transition_Width
        self.freq_xlating_fir_filter_xxx_0.set_taps( firdes.low_pass_2(1,self.radio_sample_rate,self.Low_Pass_Filter_cut_of_frequency,self.Low_Pass_Filter_Transition_Width,40))

    def get_Frequency(self):
        return self.Frequency

    def set_Frequency(self, Frequency):
        self.Frequency = Frequency
        Qt.QMetaObject.invokeMethod(self._Frequency_label, "setText", Qt.Q_ARG("QString", self.Frequency))

    def get_FFT_size(self):
        return self.FFT_size

    def set_FFT_size(self, FFT_size):
        self.FFT_size = FFT_size
        self.epy_block_0_0.in_vector_size = self.FFT_size
        self.epy_block_0_1_0.in_vector_size = self.FFT_size



def main(top_block_cls=Ether_Gnu_Radio_Companion, options=None):
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print("Error: failed to enable real-time scheduling.")

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
