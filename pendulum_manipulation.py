# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:05:35 2020

@author: wlwee
"""

import glob, os
import numpy as np
import imutils
import cv2
import random

path_dir = r'C:\Users\wlwee\Documents\python\michael_dlc\CODE'
path_data = r'C:\Users\wlwee\Documents\python\michael_dlc\DATA\Testing_Images'
path_mod_data = r'C:\Users\wlwee\Documents\python\michael_dlc\DATA\Modified_Images'

images = glob.glob(path_data + '/*.png')

for image in images:
    
    image_name = os.path.basename(image).split('.')
    
    image = cv2.imread(image)
    width = (image.shape[1])
    height = (image.shape[0])
    
    for angle in np.arange(0, 360, 15):
    
        r_scale = random.uniform(50.0,600.0)/1000
        w = int(width * r_scale)
        h = int(height * r_scale)
        dsize = (w,h)
        image = cv2.resize(image, dsize)
        
        image_save_path = path_mod_data + '/' + image_name[0] + \
        '_angle_' + str(int(angle)) + \
        '_scale_' + str(int(r_scale*100)) + \
        '.' + image_name[1]
        
        rotated = imutils.rotate_bound(image, angle)
        cv2.imshow("pendulum", rotated)
        cv2.waitKey(100)
        cv2.imwrite(image_save_path, rotated)
    
    cv2.destroyAllWindows()




   