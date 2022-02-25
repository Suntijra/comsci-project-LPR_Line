import cv2
import numpy as np
import os
import sys
import time
import Main 
import multiprocessing as mp
if(__name__=='__main__'):
    
    main = mp.Process(target=Main.main())
    main.start()
    video_input = 'http://192.168.1.109/mjpeg/1'
    camera = cv2.VideoCapture(video_input)
    
    while True:
        # reads frames from a video
        ret, frames = camera.read()
        # re = np.array(cv2.resize(cap,(600,450),fx=0,fy=0, interpolation = cv2.INTER_CUBIC))
        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray", gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    # # p1 = mp.Process(target=ov.opencv_test)
    # p1.start()
    # print('สั่งงานไปแล้ว')