
# Load the modules for controlling the DAQ
# ----------------------------------------

from uldaq import (get_daq_device_inventory, DaqDevice, InterfaceType,
                   DigitalDirection, DigitalPortIoType)
from os import system

# Clean the terminal window
# -------------------------

system('clear')

# Define the default parameters
# -----------------------------

daq_device = None;
interface_type = InterfaceType.USB

# Check there is a DAQ connected to the computer
# ----------------------------------------------

devices = get_daq_device_inventory(interface_type)
number_of_devices = len(devices)
if number_of_devices == 0:
    raise Exception('Error: No DAQ devices found')

print('Found', number_of_devices, 'DAQ device(s):')

# Connect to the DAQ 
# ------------------

daq_device = DaqDevice(devices[0])
descriptor = daq_device.get_descriptor()
print('\nConnecting to', descriptor.dev_string, '- please wait...')
daq_device.connect()

# Define the DioDevice object and return the number of Dio port on the DAQ
# ------------------------------------------------------------------------

dio_device = daq_device.get_dio_device()
dio_info = dio_device.get_info()
Nports = dio_info.get_num_ports()
PortType = dio_info.get_port_types()
print('\nNumber of ports available :', Nports)
print('\nThe type of the port is :', PortType)

# Close the connection to the DAQ
# -------------------------------

if daq_device:
    if daq_device.is_connected():
        daq_device.disconnect()
    daq_device.release()
    print('\nConnection closed')
    
