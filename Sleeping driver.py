# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:28:32 2018

@author: Anshuman_Mahapatra
"""

import cv2

from time import time



face_cascade = cv2.CascadeClassifier('C:/Users/anshuman_mahapatra/AppData/Local/Continuum/anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('C:/Users/anshuman_mahapatra/AppData/Local/Continuum/anaconda3/Lib/site-packages/cv2/data/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)





while(True):

    # Capture frame-by-frame

    ret, frame = cap.read()



    # Our operations on the frame come here

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]

        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
#        print(eyes)
        print(len(eyes))

        if(not len(eyes)):

#            t = 0
            start_time  = time()

            while(not len(eyes)):

#                t += 1

#                if t > 20:   # driver is sleeping
                end_time  = time()
                if((end_time - start_time) >= 30):

                    print("driver is sleeping !\n")

#                    time.sleep(2)

                    break

        for (ex, ey, ew, eh) in eyes:

            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)



    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break



# When everything done, release the capture

cap.release()

cv2.destroyAllWindows()