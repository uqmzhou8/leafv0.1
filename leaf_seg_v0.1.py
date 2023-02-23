# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 17:04:46 2023

@author: zhoum
"""

#trying to extract the image of leaves
import cv2

img =  cv2.imread('P277E.JPG')

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
mask_grey = cv2.inRange(hsv, (200,200,200), (250,255,255))
# find the orange color
mask_orange = cv2.inRange(hsv, (8, 60, 20), (30, 255, 200))


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

cv2.imwrite("masking_v0.1.jpg", res)