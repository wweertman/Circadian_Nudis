# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 21:08:47 2020

@author: wlwee
"""

import os, glob
import cv2
#import numpy as np

os.chdir(r'C:\Users\wlwee\Documents\python\image_manipulation\CODE')
images = r'C:\Users\wlwee\Documents\python\image_manipulation\DATA\girelab_instagramphoto_repository\*.jpg'
images = glob.glob(images)

data_dir = r'C:\Users\wlwee\Documents\python\image_manipulation\DATA\girelab_instagramphoto_repository'
labelled_imgs_dir = r'C:\Users\wlwee\Documents\python\image_manipulation\DATA\images_labelled'
output_video_dir = r'C:\Users\wlwee\Documents\python\image_manipulation\DATA\output_video'

ext = '.jpg'
w, h = 10000, 10000


font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (20,150)
fontScale              = 5
fontColor              = (255,255,255)
lineType               = 2

images = [f for f in os.listdir(data_dir) if f.endswith(ext)]

for image in images:

   image_text = image
   image = cv2.imread(os.path.join(data_dir, image)) 
   height,width,layers=image.shape
   #print(str(width) + ' ' + str(height))
   if (width < w):
       w = width
   if (height < h):
       h = height
       
   cv2.putText(image, 
               image_text, 
               bottomLeftCornerOfText, 
               font, 
               fontScale,
               fontColor,
               lineType)
    
   save_image_path = os.path.join(labelled_imgs_dir, image_text)
   cv2.imwrite(save_image_path, image)
   #cv2.imshow("img",image)    
   #cv2.waitKey(1)

shape = w, h

output = output_video_dir + '/instagram_girelab.avi'
fps = 2

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter(output, fourcc, fps, shape)

for image in images:
    image_path = os.path.join(labelled_imgs_dir, image)
    image = cv2.imread(image_path)
    resized=cv2.resize(image,shape) 
    video.write(resized)

video.release()