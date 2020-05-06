#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:12:48 2020

@author: fiche
"""

from pyueye import ueye
from MonProjet.Test_Project.Model.Camera_DCC1545.Camera_base import CameraBase

class Camera_thorlabs(CameraBase):
    
    # Define the __init__ construction method
	# ---------------------------------------

	def __init__(self):
        super().__init__()
        
    def open_connection(self):
        