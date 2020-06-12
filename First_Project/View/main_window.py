#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:48:33 2020

@author: fiche
"""
from os import path

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import uic


class Ui_MainWindow(qtw.QMainWindow):
    
    init_cam = qtc.pyqtSignal(int)
    close_cam = qtc.pyqtSignal()
    
    def __init__(self, main_path):
        super().__init__()

        # Load the GUI 
        # ------------
        
        GUI_path = path.join(main_path, 'View/GUI/main_window.ui')
        uic.loadUi(GUI_path, self) # Load the pre-defined GUI
        self.show()
        
        # Defines the connection
        # ----------------------

        # self.DAQinit_Button.clicked.connect(self.initDAQ)
        # self.DAQstop_Button.clicked.connect(self.releaseDAQ)
        # self.Pump_Button.clicked.connect(self.pump_clicked)
        self.CloseGUI_Button.clicked.connect(self.closeGUI)
        self.InitCam_Button.clicked.connect(self.init_ThorlabsCam)
        self.CloseCam_Button.clicked.connect(self.release_ThorlabsCam)
          
    # def initDAQ(self):
    #     DAQ_sn = self.config_parameters['DAQ']['serial_number']
    #     daq = DAQExperiment(DAQ_sn)
    #     return daq
        
    # def releaseDAQ(self, daq):
    #     daq.stop()
        
    # def pump_clicked(self):
    #     ao_channel = self.parameter['DAQ']['ao_pump']
    #     flow_rate = self.FlowRate_Edit.text()
    #     volume = self.Volume_Edit.text()
    #     print("The volume to inject is {}µl at {}µl/min".format(volume, flow_rate))
    #     self.daq.pump_injection(float(flow_rate),float(volume),ao_channel)
        
    def init_ThorlabsCam(self):
        print('Initializing ...')
        h = self.Camhandle_Edit.text()
        # Need to check it is between 0 and 254 + not empty
        self.init_cam.emit(int(h))
        # self.cam = CameraThorlabs(0)
        # self.cam.open_connection()
        # Id = self.cam.open_connection()
        # print("{} _ {}".format(Id[0],Id[1]))
        # FullId = Id[0] + " _ " + Id[1]
        # self.CamID_Edit.setText(FullId)  
        
    def release_ThorlabsCam(self):
        self.close_cam.emit()
        # self.cam.close_connection()
                
    def closeGUI(self):
        print("Closing software")
        self.close()
        
