# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import random
import glob
import shutil

image_dirs = glob.glob('/home/weertman/Documents/Theresa_FHL/Armina_californica/*/*/*.png')
random_images = random.sample(image_dirs,500)

dlc_train_images_dir = '/home/weertman/Documents/Theresa_FHL/Armina_DeepLabCut/random_test_images/'

if os.path.exists(dlc_train_images_dir) == True:
    shutil.rmtree(dlc_train_images_dir)
    os.mkdir(dlc_train_images_dir)
if os.path.exists(dlc_train_images_dir) != True:
    os.mkdir(dlc_train_images_dir)

for imgs in random_images:
    
    new_path_img = dlc_train_images_dir + os.path.basename(imgs)

    dest = shutil.copyfile(imgs, new_path_img) 
    print(dest)
    
