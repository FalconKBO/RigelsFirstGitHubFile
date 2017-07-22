import cv2 as cv
import numpy as np

capture= cv.VideoCapture(0)
cv.namedWindow("camera")
cv.waitKey(33)
while(1):
    ret,frame=capture.read()#这句必须每次都读
    cv.cvtColor(frame, frame, cv.COLOR_BGR2GRAY)
    #cv.GaussianBlur(frame, frame, cv.Size(7, 7), 1.5, 1.5)
    
    
    cv.imshow('camera',frame)  
       
    c = cv.waitKey(33)
    if (c == 27):
        cv.destroyWindow('camera')
        break   
    
capture.releas();
cv.destroyWindow('camera')
    