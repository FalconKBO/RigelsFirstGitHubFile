# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:41:17 2017

@author: KBO
"""
import cv2 as cv
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("C:\\Users\\KBO\\Desktop\\FR\\data\\lena.png")
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows() 
