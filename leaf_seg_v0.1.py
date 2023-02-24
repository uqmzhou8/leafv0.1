# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:04:46 2023

@author: zhoum
"""

#trying to extract the image of leaves
import cv2
import numpy as np
# img =  cv2.imread('P313D.JPG')

#perform a gaussian blurring of the image
hsv=cv2.blur(hsv, (3,3))

<<<<<<< HEAD

import os
# os.chdir('imgs')
#get current dir
pathdir=os.getcwd()
=======
# find the green color in the leaf
mask_green = cv2.inRange(hsv, (20, 20, 20), (100, 255, 255))
# find the grey color 
mask_grey = cv2.inRange(hsv, (180,180,180), (250,255,255))
# find the orange color
mask_orange = cv2.inRange(hsv, (8, 60, 20), (100, 255, 255))
>>>>>>> main


import glob

import re
 
# get the path/directory
folder_dir = 'imgs'

# iterate over files in
# that directory
for images in glob.iglob(f'{folder_dir}/*'):
   
    # check if the image ends with png
    if (images.endswith(".jpg")):
        # print(images)
        img =  cv2.imread(images)
        



        # #trying to decrease the size of the image
        # scale_percent = 35 # percent of original size
        # width = int(img.shape[1] * scale_percent / 100)
        # height = int(img.shape[0] * scale_percent / 100)
        # dim=(width,height)
        # img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        
        #convert to hsv colourmap
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        
        # find the green color in the leaf
        mask_green = cv2.inRange(hsv, (20, 20, 20), (100, 255, 255))
        # find the grey color 
        mask_grey = cv2.inRange(hsv, (100,100,100), (254,255,255))
        # find the orange color
        mask_orange = cv2.inRange(hsv, (8, 20, 20), (80, 255, 255))
        
        
        # find any of the three colors(green or brown or yellow) in the image
        mask = cv2.bitwise_or(mask_green, mask_grey)
        mask = cv2.bitwise_or(mask, mask_orange)
        
        
        
        
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(img,img, mask= mask)
        
        
        # cv2.imshow('green img', mask_green)
        # cv2.imshow('hsv',hsv)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        
        # cv2.imshow("original", img)
        # cv2.imshow("final image", res)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        s = re.findall('\\\(.*?)\.', images)
        # print(s)
        ###writing the result into images
        
        cv2.imwrite(os.path.join(pathdir , "e"+str(s)+".jpg"), res)

# #fill holes in the mask
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
# mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)



#printing out the masking for analysis


# from scipy import ndimage as ndi

<<<<<<< HEAD
# from skimage.segmentation import watershed
# from skimage.feature import peak_local_max

# distance = ndi.distance_transform_edt(mask)
# coords = peak_local_max(distance, footprint=np.ones((5, 5)), labels=mask)
# mask1 = np.zeros(distance.shape, dtype=bool)
# mask1[tuple(coords.T)] = True
# markers, _ = ndi.label(mask1)
# mask_1 = watershed(-distance, markers, mask=mask)

# cv2.imwrite("mask.jpg", mask_1)
=======
# cv2.imshow("original", img)
# cv2.imshow("final image", res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.imwrite('extracted.jpg', res)
>>>>>>> main
