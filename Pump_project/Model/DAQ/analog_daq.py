
import uldaq
from Pump_project.Model.DAQ.base import DAQBase

class AnalogDaq(DAQBase):
	def __init__(self, port):
		self.port = port