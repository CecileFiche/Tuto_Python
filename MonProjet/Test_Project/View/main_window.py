#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:48:33 2020

@author: fiche
"""

import os

from MonProjet.Test_Project.Model.Experiment.daq_experiment import DAQ_Experiment

from PyQt5 import QtWidgets
from PyQt5 import uic

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        p = os.path.dirname(__file__) # Variable __file__ contain the full path of the currently executed code
        uic.loadUi(os.path.join(p, 'GUI/main_window.ui'), self) # Load the pre-defined GUI      
        
    def setupUi(self, MainWindow):
        self.Start_Button.clicked.connect(self.start_clicked)
        self.Stop_Button.clicked.connect(self.stop_clicked)
        self.Pump_Button.clicked.connect(self.pump_clicked)
        self.CloseGUI_Button.clicked.connect(self.closeGUI)
          
    def start_clicked(self):
        self.daq = DAQ_Experiment('01CF3519')
        self.parameter = self.daq.load_config('/home/fiche/Workspace/Python/Tuto_Python/Examples/Config/experiment.yml')
        
    def stop_clicked(self):
        self.daq.stop()
        
    def pump_clicked(self):
        ao_channel = self.parameter['DAQ']['ao_pump']
        flow_rate = self.FlowRate_Edit.text()
        volume = self.Volume_Edit.text()
        print("The volume to inject is {}µl at {}µl/min".format(volume, flow_rate))
        self.daq.pump_injection(float(flow_rate),float(volume),ao_channel)
        
    def closeGUI(self):
        print("Closing software")
        self.close()
        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    m = Ui_MainWindow() # Instencitation of the class Ui_MainWindow()
    m.setupUi(m) # Apply the method setupUi
    
    m.show()
    app.exit(app.exec_())
