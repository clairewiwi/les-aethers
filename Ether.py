
from distutils.version import StrictVersion
from gnuradio import gr

if __name__ == '__main__':
	import ctypes
	import sys
	if sys.platform.startswith('linux'):
		try:
			x11 = ctypes.cdll.LoadLibrary('libX11.so')
			x11.XInitThreads()
		except:
			print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
import signal
import time
'''from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import eng_notation
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio.qtgui import Range, RangeWidget
import ConfigParser
import osmosdr
from gnuradio import qtgui'''
import threading
import csv
from Ether_Gnu_Radio_Companion import Ether_Gnu_Radio_Companion

STATIC = 0 
SCANNING = 1 



def main(top_block_cls=Ether_Gnu_Radio_Companion, options=None):
	if gr.enable_realtime_scheduling() != gr.RT_OK:
		print("Error: failed to enable real-time scheduling.")
        
	if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
		style = gr.prefs().get_string('qtgui', 'style', 'raster')
		Qt.QApplication.setGraphicsSystem(style)
	qapp = Qt.QApplication(sys.argv)
	tb = self = top_block_cls()



		
		
	 #tb.eventFilter = eventFilter
	

	
	# Import des bookmarks  --------------------------
	class CSV(csv.DictReader):
		def __init__(self,path):
			csvfile = self.inFile  = open(path, "r" , encoding = "utf-8")
			delimiter = ";"# csv.Sniffer().sniff(csvfile.readline(), delimiters=";,\t").delimiter
			start = csvfile.read().find("# Frequency")+2
			csvfile.seek(start)
			#print("dected delimiter : ",repr(delimiter))
			csv.DictReader.__init__(self,csvfile,delimiter = delimiter)
		def close(self):
			self.inFile.close()
	inCsv = CSV("bookmarks.csv"  )  
	dictsList = []  
	#labels = [""]
	#options = [0]
	frequences_labels = []
	for row in inCsv:
		rowDict = dict() 
		for key, value in row.items()  :
			if value : 
				key = key.strip()
				value  = value.strip ()
				if key in ('Frequency','Bandwidth') : 
					value = int(value)
				rowDict[key]= value 
		#print(rowDict['Tags'])
		if rowDict['Tags'] == 'ether' and rowDict['Modulation'].startswith('WFM') :
			frequences_labels.append((rowDict['Frequency'],rowDict["Name"] + " - " +  str(rowDict['Frequency']/1e6) + " MHz"))
	options , labels =  zip(*sorted(frequences_labels))
	self._radio_frequency_center_menu_labels = labels
	self._radio_frequency_center_menu_options = options
	for _label in self._radio_frequency_center_menu_labels: self._radio_frequency_center_menu_combo_box.addItem(_label)
	
	# Scann Automatique des frequences  ---------------
	#time_between_frequencies =  10
	#time_stop_on_frequency  =  10
	update_frequency = 10

	# v1 (avec thread, marche mal )-------------------
	if False : 
	    #self._radio_frequency_center_menu_combo_box.setCurrentIndex(1)
		step_float =  2000/(self.time_between_frequencies*update_frequency)
		def _radio_frequency_delta_probe():
			value = 0
			while True:
				if self.get_radio_scann():
					if int(value) != self._radio_frequency__delta_MHz_win.d_widget.value():
						value = self._radio_frequency__delta_MHz_win.d_widget.value()
					
					if (value <= 1000) and ((value + step_float) >= 1000):
						print(value)
						time.sleep(self.time_stop_on_frequency)	
						value += step_float
					value += step_float
					if value >= 2000:
						self._radio_frequency_center_menu_combo_box.setCurrentIndex( self._radio_frequency_center_menu_combo_box.currentIndex()+ 1)
						value = 0
					self._radio_frequency__delta_MHz_win.d_widget.setValue(int(value))
					time.sleep(1.0 / update_frequency)	
		_radio_frequency_delta_thread = threading.Thread(target=_radio_frequency_delta_probe)
		_radio_frequency_delta_thread.daemon = True
		_radio_frequency_delta_thread.start()
		
	# v2 (avec QTimer)-------------------
	if True : 
		self.between_frequencies_position  = 0 	
		def _radio_scann_tick():
			if self.get_radio_scann():
				self.timer.setInterval(int(1000/update_frequency))
				current_index  = self._radio_frequency_center_menu_combo_box.currentIndex()
				next_index = current_index+1
				if next_index >= self._radio_frequency_center_menu_combo_box.count() :
					next_index = 0
					self._radio_frequency_center_menu_combo_box.setCurrentIndex(next_index)
					self.between_frequencies_position = 0
					self.epy_block_0_1_0.set_mode(STATIC)
					radio_frequency = self._radio_frequency_center_menu_options[next_index]
					self.set_radio_frequency_center(radio_frequency)
					self.timer.setInterval(int(self.time_stop_on_frequency*1000))
				else : 

					radio_frequency_1 = self._radio_frequency_center_menu_options[current_index]
					radio_frequency_2 = self._radio_frequency_center_menu_options[next_index]
					radio_frequency = radio_frequency_1 + (radio_frequency_2 - radio_frequency_1) * self.between_frequencies_position
					self.set_radio_frequency_center(radio_frequency)
					self.between_frequencies_position += 1/(self.time_between_frequencies*update_frequency)
					if self.between_frequencies_position >= 1 :
						self._radio_frequency_center_menu_combo_box.setCurrentIndex(next_index)
						self.between_frequencies_position = 0
						self.epy_block_0_1_0.set_mode(STATIC)
						self.timer.setInterval(int(self.time_stop_on_frequency*1000))
					else : 
	  					self.epy_block_0_1_0.set_mode(SCANNING)

		self.timer  = Qt.QTimer(parent = qapp)
		self.timer.setInterval(int(1000/update_frequency))
		self.timer.timeout.connect(_radio_scann_tick)
		self.epy_block_0_1_0.set_mode(SCANNING)
		self.timer.start()
						
		
		
	tb.start()
	tb.show()
	tb.showFullScreen()
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
