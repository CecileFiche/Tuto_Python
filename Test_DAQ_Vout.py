
# Load the modules for controlling the DAQ
# ----------------------------------------

from uldaq import (get_daq_device_inventory, DaqDevice, InterfaceType, AOutFlag)
from os import system
from sys import stdout

# Clean the terminal window
# -------------------------

system('clear')
CURSOR_UP = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


# Define the default parameters
# -----------------------------

daq_device = None;
output_channel = 2;
interface_type = InterfaceType.USB

# Check there is a DAQ connected to the computer
# ----------------------------------------------

devices = get_daq_device_inventory(interface_type)
number_of_devices = len(devices)
if number_of_devices == 0:
    raise Exception('Error: No DAQ devices found')

print('Found', number_of_devices, 'DAQ device(s):')

# Connect to the DAQ and create the objects daq_device
# ----------------------------------------------------

daq_device = DaqDevice(devices[0])
descriptor = daq_device.get_descriptor()
print('\nConnecting to', descriptor.dev_string)
daq_device.connect()

# Define the ao_device object and return the number of ao port on the DAQ
# ------------------------------------------------------------------------

ao_device = daq_device.get_ao_device()

if ao_device is None:
    raise Exception('Error: The DAQ device does not support analog output')

ao_info = ao_device.get_info()
Nports = ao_info.get_num_chans()
Range = [ao_info.get_ranges()]
print('\nNumber of ports available :', Nports)
print('\nThe type of the port is :', Range)

# Select the output range
# ------------------------

output_range = ao_info.get_ranges()[0] # The range is -10/10V

# Lauch a test using the keyboard
# -------------------------------

try:
    input('\nHit ENTER to continue')
except (NameError, SyntaxError):
    pass

system('clear')
print('Active DAQ device: ', descriptor.dev_string, ' (', descriptor.unique_id, ')\n', sep='')
print('*Enter non-numeric value to exit')
try:
    while True:
        try:
            # Get and set a user specified output value.
            out_val = input('    Enter output value (V): ')
            ao_device.a_out(output_channel, output_range, AOutFlag.DEFAULT, float(out_val))
            # Clear the previous input request before the next input request.
            stdout.write(CURSOR_UP + ERASE_LINE)
        except ValueError as error:
            print("La valeur indiquée est en dehors du range authorisé")
            print(error)
            break
        except NameError as error:
            print("Une des variables n'a pas été définie")
            print(error)
            break
        except SyntaxError as error:
            print("Erreur d'écriture")
            print(error)
            break
except KeyboardInterrupt:
    pass

# Close the connection to the DAQ
# -------------------------------

if daq_device:
    if daq_device.is_connected():
        daq_device.disconnect()
    daq_device.release()
    print('\nConnection closed')
    
