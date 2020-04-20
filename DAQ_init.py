
# Load the modules for controlling the DAQ
# ----------------------------------------

from uldaq import (get_daq_device_inventory, DaqDevice, InterfaceType)
from os import system

# Define a class called DAQ with a function for the initialization
# ----------------------------------------------------------------

class DAQ():

	def __init__(self, DAQ_id):
		self.rsc = DAQ_id
		system('clear')

	def DAQ_init(self):

		daq_device = None;
		interface_type = InterfaceType.USB

    	# Check there is a DAQ connected to the computer
		# ----------------------------------------------

		devices = get_daq_device_inventory(interface_type)
		number_of_devices = len(devices)
		if number_of_devices == 0:
		    raise Exception('Error: No DAQ devices found')
		else:
			print('\nnumber of devices :', len(devices))    
		

		# Look for the USB-3104
		# ---------------------

		for device in devices:
			id = device.unique_id
			if id == self.rsc:

				daq_device = DaqDevice(device)
				daq_device.connect()
				print('\nDevice found and connected')

			else:
				print('\nThe device ', self.rsc, 'was not found')

		return daq_device

	def DAQ_disconnect(self,daq_device):

		if daq_device.is_connected():
			daq_device.disconnect()

		daq_device.release()
		print('\nConnection closed')




# Use the class DAQ to init the acquisition card
# ----------------------------------------------

dev = DAQ('01CF3519')
connected_daq = dev.DAQ_init()
dev.DAQ_disconnect(connected_daq)
