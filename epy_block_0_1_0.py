"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import random 
from scipy.interpolate import InterpolatedUnivariateSpline
from collections import deque
STATIC = 0 
SCANNING = 1 

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
	"""Embedded Python Block example - a simple multiply const"""

	def __init__(self, in_vector_size=1024,nb_cordes = 8,nb_harmoniques = 5,nb_cordes_out = 8,on_off = True ):  # only default arguments here
		"""arguments to this function show up as parameters in GRC"""
		self.in_vector_size= in_vector_size
		self.nb_cordes = nb_cordes
		self.nb_cordes_out = nb_cordes_out
		self.nb_harmoniques = nb_harmoniques
		self.on_off = on_off
		self.fft_block_counter = 0
		self.cordes_harmonique_range =   [[1,2],[1,2],[2,3],[2,3],[2,3],[2,3],[1,2],[1,2]]
		self.cordes_harmonique =   [1,1,2,2,2,2,1,1]
		self.cordes_phase  =  [1,1,1,1,1,1,1,1]
		self.alpha = 0.1
		self.num_corde_to_change = 0
		gr.sync_block.__init__(
			self,
			name='Embedded Python Block',   # will show up in GRC
			in_sig=[(np.complex64,self.in_vector_size)],
			out_sig = [(np.float32,self.in_vector_size)]*nb_cordes_out * nb_harmoniques
		)
		self.last_controls = np.zeros((self.nb_cordes_out,self.nb_harmoniques))
		#self.deque_len = 8
		#self.deque_range = range(self.deque_len )
		#self.lasts_controls = deque(maxlen =self.deque_len )
		#for i in range(self.deque_len):
		#	self.lasts_controls.append(np.zeros((self.nb_cordes_out,self.nb_harmoniques)))
	  
	def change_on_harmonique(self):
		
		#num_corde_to_change = self.num_corde_to_change = random.randint(0,self.nb_cordes-1)
		num_corde_to_change = self.num_corde_to_change = (self.num_corde_to_change+1)%8
		old_harmonique  = self.cordes_harmonique[num_corde_to_change]
		new_harmonique  =  random.choice(self.cordes_harmonique_range[num_corde_to_change])
		if old_harmonique == new_harmonique:
			self.cordes_phase[num_corde_to_change]   *= -1
		self.cordes_harmonique[num_corde_to_change] = new_harmonique


	def work(self, input_items, output_items):
		"""example: multiply with constant"""
		for fft_bloc_number in range(len(input_items[0])): 
			self.fft_block_counter += 1
			if self.fft_block_counter % 10 == 0 : 
				self.change_on_harmonique()
			fft_block = np.abs(input_items[0][fft_bloc_number])
			
			new_controls = np.zeros((self.nb_cordes_out,self.nb_harmoniques))
			#filtered_new_controls = np.zeros((self.nb_cordes_out,self.nb_harmoniques))
			if self.on_off:
				if self.mode == STATIC:
					for corde,harmonique in enumerate(self.cordes_harmonique) : 
						new_controls[corde,harmonique] = self.cordes_phase[corde] #volume
						new_controls[corde,harmonique] = self.alpha *new_controls[corde,harmonique] + (1 - self.alpha) * self.last_controls[corde,harmonique]
				else: 
					for corde in range(self.nb_cordes_out):
						for harmonique in range(5):#self.nb_harmoniques):
							width = 2**harmonique
							start = (self.nb_cordes + corde) * width
							end = start + width
							#new_controls[corde,harmonique] = self.alpha * np.minimum(fft_block[start:end].sum()*0.01,1.)  + (1 - self.alpha) * self.lasts_controls[-1][corde,harmonique]
							#new_controls[corde,harmonique] = self.alpha *(fft_block[start:end].sum()*0.01 ) + (1 - self.alpha) * self.lasts_controls[-1][corde,harmonique]
							#new_controls[corde,harmonique] = self.alpha *(fft_block[start:end].sum()*0.01 ) + (1 - self.alpha) * self.last_controls[corde,harmonique]
							new_controls[corde,harmonique] = fft_block[start:end].sum()*0.015
							new_controls[corde,harmonique] = self.alpha *new_controls[corde,harmonique] + (1 - self.alpha) * self.last_controls[corde,harmonique]

			#self.lasts_controls_numpy = np.array(self.lasts_controls)
			for corde in range(self.nb_cordes_out):
				for harmonique in range(self.nb_harmoniques):
					#spl = InterpolatedUnivariateSpline(self.deque_range, self.lasts_controls_numpy[:,corde,harmonique])
					#xs = np.linspace(3, 4, self.in_vector_size)
					#interp  = spl(xs)
					interp = np.linspace(self.last_controls[corde,harmonique], new_controls[corde,harmonique],self.in_vector_size)
					output_items[corde* self.nb_harmoniques + harmonique][fft_bloc_number][:] = interp
			#self.lasts_controls.append(new_controls)
			self.last_controls = new_controls
		return len(output_items[0])

	def set_mode(self,mode): 
		self.mode = mode 

	def set_on_off(self,on_off):
		self.on_off = on_off
