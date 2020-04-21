
# Load the modules for controlling the DAQ
# ----------------------------------------

from uldaq import (get_daq_device_inventory, DaqDevice, InterfaceType,
	AOutFlag,
	DigitalDirection,DigitalPortIoType)
from os import system
from time import sleep
import matplotlib.pyplot as plt

# Define a class called DAQ with a function for the initialization
# ----------------------------------------------------------------

class DAQ():

	# Define default settings
	# -----------------------

	DEFAULTS = {'interfacing_method' : InterfaceType.USB}

	# Define the class instanciation method
	# -------------------------------------

	def __init__(self, DAQ_id):
		self.rsc = DAQ_id
		system('clear')

	# Define the method allowing for the DAQ initialization
	# -----------------------------------------------------

	def DAQ_init(self):

		interface_type = self.DEFAULTS['interfacing_method']

    	# Check there is a DAQ connected to the computer
		# ----------------------------------------------

		devices = get_daq_device_inventory(interface_type)
		number_of_devices = len(devices)
		if number_of_devices == 0:
		    raise Exception('Error: No DAQ devices found')
		else:
			print("\nnumber of devices :{}".format(len(devices)))    
		

		# Look for the USB-3104
		# ---------------------

		for device in devices:
			id = device.unique_id
			if id == self.rsc:

				daq_device = DaqDevice(device)
				daq_device.connect()
				print('\nDevice found and connected')

			else:
				print("\nThe device {} was not found".format(self.rsc))

		return daq_device

	# Define a method to change the voltage of a given analogic output
	# ----------------------------------------------------------------  

	def set_ao_voltage(self,daq_device,ao_channel,ao_voltage):

		if daq_device.is_connected():
			ao_device = daq_device.get_ao_device()

			if ao_device is None:
				raise Exception('Error: The DAQ device does not support analog output')

			ao_info = ao_device.get_info()
			output_range = ao_info.get_ranges()[0] # The range is -10/10V
			Nports = ao_info.get_num_chans()

			if ao_channel<=Nports:
				ao_device.a_out(ao_channel, output_range, AOutFlag.DEFAULT, float(ao_voltage))
			else:
				print('The ao channel does not exist')
		else:
			print('The DAQ is not connected')

	# Read the signal from a given digital input
	# ------------------------------------------

	def read_di(self,daq_device,di_channel):

		if daq_device.is_connected():
			dio_device = daq_device.get_dio_device()

			if dio_device is None:
				raise Exception('Error: The DAQ device does not support digital input')

			dio_info = dio_device.get_info()
			Nports = dio_info.get_num_ports()
			port_types = dio_info.get_port_types()

			if di_channel<=Nports:
				port_to_read = port_types[di_channel]

			data = dio_device.d_in(port_to_read)
			return data

	# Disconnect the DAQ
	# ------------------

	def DAQ_disconnect(self,daq_device):

		if daq_device.is_connected():
			daq_device.disconnect()

		daq_device.release()
		print('\nConnection closed')

# Use the class DAQ to init the acquisition card
# ----------------------------------------------

dev = DAQ('01CF3519')
connected_daq = dev.DAQ_init()

ao_channel = 2
di_channel = 0
voltage_step = 1
voltage_max = 5

V = [];

for v_in in range(0,voltage_max,voltage_step):
	dev.set_ao_voltage(connected_daq,ao_channel,v_in)
	v = dev.read_di(connected_daq,di_channel)
	V.append(v)
	sleep(1)

voltage_step = -1
for v_in in range(voltage_max,0,voltage_step):
	dev.set_ao_voltage(connected_daq,ao_channel,v_in)
	v = dev.read_di(connected_daq,di_channel)
	V.append(v)
	sleep(1)

dev.set_ao_voltage(connected_daq,ao_channel,0)
dev.DAQ_disconnect(connected_daq)

plt.plot(V)
plt.xlabel("Measurement point", fontsize=14)
plt.ylabel("TTL output", fontsize=14)
plt.show()