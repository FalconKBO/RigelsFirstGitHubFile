# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 14:09:38 2017

@author: KBO
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import cv2
 
cap = cv2.VideoCapture(0)
 
while(True):
    # 读取一帧
    ret, frame = cap.read()
 
    # 转为灰度模式
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # 显示帧
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# 释放VideoCapture对象
cap.release()
cv2.destroyAllWindows()