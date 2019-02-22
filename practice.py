# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 12:32:34 2018

@author: Anshuman_Mahapatra
"""

##3Opne cv exercises

##change colors of pixels
import cv2
import numpy as np
import os
os.chdir('D:/Data Science/POC/opencv')

img = cv2.imread("D:/Data Science/opencv/0901869f8ba9f1a9.jpeg", cv2.IMREAD_COLOR)
img

img[100:150,100:150] = [255,255,255]

cv2.imshow('image', img)
cv2.waitkey(0)
cv2