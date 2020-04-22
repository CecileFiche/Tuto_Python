import sys
sys.path.append('/home/fiche/Desktop/Workspace/Python/Tuto_Python/Pump_project/Model/DAQ/')


from analog_daq import AnalogDaq

daq = AnalogDaq('/dev/ttyACM0')
print(daq.port)

daq.idn()
