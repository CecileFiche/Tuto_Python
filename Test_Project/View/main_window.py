#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:48:33 2020

@author: fiche
"""

import os

from Test_Project.Model.Experiment.daq_experiment import DAQ_Experiment
from Test_Project.Model.Camera_DCC1545.camera_DCC1545M import Camera_thorlabs

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
        self.InitCam_Button.clicked.connect(self.init_ThorlabsCam)
        self.CloseCam_Button.clicked.connect(self.release_ThorlabsCam)
          
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
        
    def init_ThorlabsCam(self):
        self.cam = Camera_thorlabs(8,1)
        Id = self.cam.open_connection()
        print("{} _ {}".format(Id[0],Id[1]))
        FullId = Id[0] + " _ " + Id[1]
        self.CamID_Edit.setText(FullId)  
        
    def release_ThorlabsCam(self):
        self.cam.close_connection()
        
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    m = Ui_MainWindow() # Instencitation of the class Ui_MainWindow()
    m.setupUi(m) # Apply the method setupUi
    
    m.show()
    app.exit(app.exec_())
