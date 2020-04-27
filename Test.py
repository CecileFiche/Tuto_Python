# A METTRE DANS LE FICHIER CONFIG

import sys
sys.path.append('/home/fiche/Desktop/Workspace/Python/Tuto_Python/Pump_project/Model/DAQ/')
sys.path.append('/home/fiche/Desktop/Workspace/Python/Tuto_Python/Pump_project/Model/Experiment/')

from os import system
from daq_experiment import DAQ_Experiment

system('clear')

# Instantiate the class DAQ_Experiment
# ------------------------------------

daq = DAQ_Experiment('01CF3519')
parameter = daq.load_config('/home/fiche/Desktop/Workspace/Python/Tuto_Python/Examples/Config/experiment.yml')

# Run a small injection
# ---------------------

ao_channel = parameter['DAQ']['ao_pump'];
flow_rate = 100;
volume = 0;
daq.pump_injection(flow_rate,volume,ao_channel)

# Send a TTL trigger
# ------------------

do_channel = parameter['DAQ']['do_trigger'];
dt = 1;
daq.send_trigger(dt,do_channel)

# Release the DAQ
# ---------------

daq.stop()