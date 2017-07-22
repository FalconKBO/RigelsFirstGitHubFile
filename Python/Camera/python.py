# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:44:51 2017

@author: KBO
"""
import cv2 as cv
img = cv.imread("C:\\Users\\KBO\\Desktop\\FR\\data\\lena.png")
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(3000)
cv.destroyAllWindows() 
