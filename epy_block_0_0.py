"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
	"""Embedded Python Block example - a simple multiply const"""

	def __init__(self, in_vector_size=1024,out_vector_size=512,example_parameter=1.0):  # only default arguments here
		"""arguments to this function show up as parameters in GRC"""
		self.in_vector_size= in_vector_size
		self.out_vector_size = out_vector_size
		self.example_parameter = example_parameter
		gr.sync_block.__init__(
			self,
			name='Embedded Python Block',   # will show up in GRC
			in_sig=[(np.complex64,self.in_vector_size)],
			out_sig=[(np.float32,self.out_vector_size)]
		)

	def work(self, input_items, output_items):
		"""example: multiply with constant"""
		output_items[0][:] = np.abs(input_items[0])[:,:512]
		return len(output_items[0])

