# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:47:55 2019

@author: Anshuman_Mahapatra
"""

# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
from threading import Thread
import numpy as np
import playsound
import argparse
import imutils
import time
import dlib
import cv2
import os
os.chdir('D:/Data Science/POC/opencv')

def sound_alarm(path):
	# play an alarm sound
	playsound.playsound(path)

def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)

	# return the eye aspect ratio
	return ear


# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold for to set off the
# alarm
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 4

sleep_flag = False

# initialize the frame counter as well as a boolean used to
# indicate if the alarm is going off
COUNTER = 0
ALARM_ON = False

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] LOADING facial landmark predictor...")
##My Entry
shape_predictor = "model/shape_predictor_68_face_landmarks.dat"
#alarm_path = vlc.MediaPlayer("Pune.m4a")
alarm_path = "beep-01a.mp3"
detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor(args["shape_predictor"])
predictor = dlib.shape_predictor(shape_predictor)

# grab the indexes of the facial landmarks for the left and
# right eye, respectively
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# start the video stream thread
print("[INFO] starting video stream ...")
##Based on the no of webcams the src can be defined here.For my case integrated webcam will do
##vs = VideoStream(src=0).start()
##vs = cv2.FileVideoStream("rec_vid")

##video with sleep
vs = cv2.VideoCapture("rec_vid.mp4")
##Video without sleep
#vs = cv2.VideoCapture("rec_vid_wosleep.mp4")

##fps = FPS().start()

frame_width = int(vs.get(3))
frame_height = int(vs.get(4))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
##out = cv2.VideoWriter('testop1.avi',fourcc, 15.0, (frame_width,frame_height))
out = cv2.VideoWriter('testop1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10.0, (frame_width,frame_height))


#time.sleep(1.0)

# loop over frames from the video stream
while(True):
  ret, frame = vs.read()
 
  if ret == True: 
    cv2.putText(img = frame, text = 'GET UP', org = (int(frame_width/2 - 20),int(frame_height/2)),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale =0.7, color =(0, 0, 255))
    # Write the frame into the file 'output.avi'
    out.write(frame)
 
    # Display the resulting frame    
    cv2.imshow('frame',frame)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 

vs.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows() 