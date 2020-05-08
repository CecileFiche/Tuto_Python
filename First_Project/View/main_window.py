#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:48:33 2020

@author: fiche
"""
import os.path as path
from First_Project.Model.Experiment.daq_experiment import DAQ_Experiment
from First_Project.Model.Camera_DCC1545.camera_DCC1545M import Camera_thorlabs

from PyQt5 import QtWidgets
from PyQt5 import uic

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, config_parameters, main_path, parent=None):
        super().__init__(parent)
        
        # Load the config parameters
        # --------------------------
        self.config_parameters = config_parameters
        
        # Load the GUI 
        # ------------
        uic.loadUi(path.join(main_path, 'View/GUI/main_window.ui'), self) # Load the pre-defined GUI
        
        
    def setupUi(self, MainWindow):
        self.DAQinit_Button.clicked.connect(self.initDAQ)
        self.DAQstop_Button.clicked.connect(self.releaseDAQ)
        self.Pump_Button.clicked.connect(self.pump_clicked)
        self.CloseGUI_Button.clicked.connect(self.closeGUI)
        self.InitCam_Button.clicked.connect(self.init_ThorlabsCam)
        self.CloseCam_Button.clicked.connect(self.release_ThorlabsCam)
          
    def initDAQ(self):
        DAQ_sn = self.config_parameters['DAQ']['serial_number']
        daq = DAQ_Experiment(DAQ_sn)
        return daq
        
    def releaseDAQ(self, daq):
        daq.stop()
        
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
