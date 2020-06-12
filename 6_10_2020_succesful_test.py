# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:29:22 2020

@author: wlwee
"""

from pypylon import pylon
import cv2
import time
import os

img_type = '.png'
width, height, exposure = 1900, 1200, 19000
fps = 50
pixel_format = "Mono12"
animal = 'test_'

path_dir = 'C:/Users/wlwee/Documents/python/fhl_pypylon/DATA/time_test/'
path_dir = path_dir + animal + time.strftime("%Y-%m-%d-%H-%M-%S") + '/'
os.mkdir(path_dir)

# conecting to the first available camera
camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()

window_name = 'camera_' + camera.DeviceSerialNumber.GetValue()

## sets the camera parameters    
camera.Width.SetValue(width)
camera.Height.SetValue(height)
camera.ExposureTime.SetValue(exposure)
camera.PixelFormat = pixel_format

camera.ReverseY.SetValue(True)

## set the frame rate
camera.AcquisitionFrameRateEnable.SetValue(True);
b = camera.AcquisitionFrameRateEnable.GetValue();

camera.AcquisitionFrameRate.SetValue(fps);
d = camera.AcquisitionFrameRate.GetValue();

print("Using device ", camera.GetDeviceInfo().GetModelName())

# Grabing Continusely (video) with minimal delay
camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly) 
converter = pylon.ImageFormatConverter()

# converting to opencv bgr format 
# opencv is better than pypylon
converter.OutputPixelFormat = pylon.PixelType_BGR8packed
converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)

    if grabResult.GrabSucceeded():
        # Access the image data
        image = converter.Convert(grabResult)
        img = image.GetArray()
        
        #below gives human readable timestamp
        #https://timestamp.online/article/how-to-get-current-timestamp-in-python
        #https://timestamp.online/article/how-to-convert-timestamp-to-datetime-in-python
        #ts = datetime.datetime.fromtimestamp(time.time()).isoformat()
        #below gives time from start of epoch, machine friendly
        ts = str(time.time())
        ts =  ts.split('.')
        ts_s = ts[0]
        ts_ms = ts[1]     
        
        ## any image test code can be put here 
        ## follow it with another nest while loop with an if statement like above
        
        '''
        position = (10,50)
        cv2.putText(
                img, #numpy array on which text is written
                ts, #text
                position, #position at which writing has to start
                cv2.FONT_HERSHEY_SIMPLEX, #font family
                1, #font size
                (209, 80, 0, 255), #font color
                3) #font stroke
        ''' 
        
        img_name = path_dir + animal + ts_s +'_' + ts_ms + img_type
        cv2.imwrite(img_name, img)
        
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)       
        cv2.imshow(window_name, img)

        ## waits 1 ms, needed for cv2.imshow() to work
        k = cv2.waitKey(1)
        if k == 27:
            break
        
        
    grabResult.Release()
    
# Releasing the resource    
camera.StopGrabbing()
camera.Close()
cv2.destroyAllWindows()