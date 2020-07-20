#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:47:23 2020

@author: weertman
"""

import deeplabcut
import glob
import os

experimenter = 'Theresa'
project = 'Armina_model_1'

videos = glob.glob('/home/weertman/Documents/Theresa_FHL/Armina_DeepLabCut/random_train_images/*.png')

path_config = '/home/weertman/Documents/Theresa_FHL/Armina_DeepLabCut/Arimina_model_1/'
if os.path.exists(path_config) != True:
    os.mkdir(path_config)
    
path_config = deeplabcut.create_new_project(project, 
                                            experimenter, 
                                            videos,
                                            copy_videos = True,
                                            working_directory = path_config)

path_config = '/home/weertman/Documents/Theresa_FHL/Armina_DeepLabCut/Arimina_model_1/Armina_model_1-Theresa-2020-07-01/config.yaml'
'''
deeplabcut.extract_frames(path_config,
                          mode = 'automatic',   
                          algo = 'uniform',
                          userfeedback = False,
                          crop = False)
'''
deeplabcut.label_frames(path_config)

deeplabcut.create_training_dataset(path_config)
deeplabcut.train_network(path_config, maxiters = 200000, displayiters = 10)
deeplabcut.evaluate_network(path_config)

deeplabcut.analyze_time_lapse_frames(path_config, 
                                     '/home/weertman/Documents/Theresa_FHL/Armina_DeepLabCut/left_test_images/',
                                     save_as_csv = True)

