#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:12:48 2020

@author: fiche
"""

from pyueye import ueye
import cv2
import time
# from First_Project.Model.Camera_Thorlabs.camera_base import CameraBase

class Camera_thorlabs():
    
    # Define the __init__ construction method
	# ---------------------------------------
    
    def __init__(self, camID):
        super().__init__()
        
        # Define the variables that will be used to retrieve the properties
        # of the camera (generic dictionnaries from ueye)
        # -----------------------------------------------
        
        self.hcam = ueye.HIDS(camID) # 0 for the first available camera - 1-254 when we already have a specified ID
        self.sensor_info = ueye.SENSORINFO()
        self.cam_info = ueye.CAMINFO()
        self.rectAOI = ueye.IS_RECT()
        self.init = False # Indicate that the initialization procedure was not launched yet
        
    def open_connection(self):
        
        # Starts the driver and establishes the connection to the camera
        # --------------------------------------------------------------
        
        Init = ueye.is_InitCamera(self.hcam, None)
        if Init != ueye.IS_SUCCESS:
            print("is_InitCamera ERROR - make sure the camera is properly connected")
            return
        else:
            print('success')
            
        # Reads out the data hard-coded in the non-volatile camera memory and 
        # writes it to the data structure that cInfo points to
        # ----------------------------------------------------
        
        read_cam_info = ueye.is_GetCameraInfo(self.hcam, self.cam_info)
        if read_cam_info != ueye.IS_SUCCESS:
            print("is_GetCameraInfo ERROR")
            return

        # You can query additional information about the sensor type used in 
        # the camera
        # ----------
        
        read_sensor_info = ueye.is_GetSensorInfo(self.hcam, self.sensor_info)
        if read_sensor_info != ueye.IS_SUCCESS:
            print("is_GetSensorInfo ERROR")
            return

        # Reset buffer and all the display parameters to the default values
        # -----------------------------------------------------------------

        reset = ueye.is_ResetToDefault(self.hcam)
        if reset != ueye.IS_SUCCESS:
            print("is_ResetToDefault ERROR")
            return

        # Set display mode to DIB - the image is directly saved on the RAM
        # ----------------------------------------------------------------

        ueye.is_SetDisplayMode(self.hcam, ueye.IS_SET_DM_DIB)
        
        # Set the color mode according to the sensor properties
        # -----------------------------------------------------
        
        if int.from_bytes(self.sensor_info.nColorMode.value, byteorder='big') == ueye.IS_COLORMODE_CBYCRY:
            # for color camera models use RGB32 mode
            self.m_nColorMode = ueye.IS_CM_BGRA8_PACKED
            self.nBitsPerPixel = ueye.INT(32)
            self.bytes_per_pixel = int(self.nBitsPerPixel / 8)
            self.color_mode = 'RGB'
        
        elif int.from_bytes(self.sensor_info.nColorMode.value, byteorder='big') == ueye.IS_COLORMODE_MONOCHROME:
            # for color camera models use RGB32 mode
            self.m_nColorMode = ueye.IS_CM_MONO8
            self.nBitsPerPixel = ueye.INT(8)
            self.bytes_per_pixel = int(self.nBitsPerPixel / 8)
            self.color_mode = 'Monochrome'
        
        else:
            print('Error : the camera type is unknown.')
            return
        
        # Define a dictionary with the main properties of the camera selected
        # -------------------------------------------------------------------
        
        ueye.is_AOI(self.hcam, ueye.IS_AOI_IMAGE_GET_AOI, self.rectAOI, ueye.sizeof(self.rectAOI))
        
        self.Properties = {'Camera sensor model (from IDS)': self.sensor_info.strSensorName.decode('utf-8'),
                      'Camera s/n': self.cam_info.SerNo.decode('utf-8'),
                      'Color mode': self.color_mode,
                      'Image width': int(self.rectAOI.s32Width),
                      'Image height': int(self.rectAOI.s32Height),
                      }
            
        # Indicate that the initialization procedure was completed
        # --------------------------------------------------------
        
        print('Thorlabs camera was found and initialized')
        self.init = True
        
    def close_connection(self):
        
        ueye.is_ExitCamera(self.hcam)
        print('Connection to the camera was closed')
        
        
if __name__ == "__main__":
    
    cam = Camera_thorlabs(0)
    cam.open_connection()
    cam.close_connection()
    