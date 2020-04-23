import sys
sys.path.append('/home/fiche/Desktop/Workspace/Python/Tuto_Python/Pump_project/Model/DAQ/')
sys.path.append('/home/fiche/Desktop/Workspace/Python/Tuto_Python/Pump_project/Model/Experiment/')

from os import system
from daq_experiment import DAQ_Experiment

system('clear')

# Instantiate the class DAQ_Experiment
# ------------------------------------

daq = DAQ_Experiment('01CF3519')

# Run a small injection
# ---------------------

ao_channel = 2;
flow_rate = 100;
volume = 0;
daq.pump_injection(flow_rate,volume,ao_channel)

# Send a TTL trigger
# ------------------

do_channel = 0;
dt = 1;
daq.send_trigger(dt,do_channel)

# Release the DAQ
# ---------------

daq.stop()
