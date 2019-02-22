# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:52:12 2019

@author: Anshuman_Mahapatra
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 14:24:41 2019

@author: Anshuman_Mahapatra
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:51:19 2018

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
while True:
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale
	# channels)
	(grabbed, frame) = vs.read()
	if grabbed:
		
    
	
		#frame = imutils.resize(frame, width=450)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		##frame = np.dstack([frame, frame, frame])

		# detect faces in the grayscale frame
		rects = detector(gray, 0)

		# loop over the face detections
		for rect in rects:
			# determine the facial landmarks for the face region, then
			# convert the facial landmark (x, y)-coordinates to a NumPy
			# array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)

			# extract the left and right eye coordinates, then use the
			# coordinates to compute the eye aspect ratio for both eyes
			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)

			# average the eye aspect ratio together for both eyes
			ear = (leftEAR + rightEAR) / 2.0

			# compute the convex hull for the left and right eye, then
			# visualize each of the eyes
			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)
			#cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
			#cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

			# check to see if the eye aspect ratio is below the blink
			# threshold, and if so, increment the blink frame counter
			if ear < EYE_AR_THRESH:
				COUNTER += 1

				# if the eyes were closed for a sufficient number of
				# then sound the alarm
				if COUNTER >= EYE_AR_CONSEC_FRAMES:
					# if the alarm is not on, turn it on
					if not ALARM_ON:
						ALARM_ON = True

						# check to see if an alarm file was supplied,
						# and if so, start a thread to have the alarm
						# sound played in the background
						if (alarm_path) != "":
							t = Thread(target=sound_alarm,	args=(alarm_path,))
							t.deamon = True
							t.start()
							sleep_flag =  True

					# draw an alarm on the frame
					#cv2.putText(frame, "GET UP!", (10, 70))
                
					cv2.putText(img = frame, text = 'GET UP', org = (int(frame_width/2 - 20),int(frame_height/2 + 40)),fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale =8, color =(0, 0, 255))
						

			# otherwise, the eye aspect ratio is not below the blink
			# threshold, so reset the counter and alarm
			else:
				COUNTER = 0
				ALARM_ON = False

			# draw the computed eye aspect ratio on the frame to help
			# with debugging and setting the correct eye aspect ratio
			# thresholds and frame counters
			#cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30))
			
			
	 
		# show the frame
		#frame = cv2.flip(frame,0)
		out.write(frame)
		#cv2.imshow("Frame", frame)
		#print("Writing to Output")
	else:
		break
	 
#print(sleep_flag)
if sleep_flag:
	print("DRIVER WAS SLEEPING")
else:
	print("DRIVER WAS NOT SLEEPING")
##	fps.update()
	##key = cv2.waitKey(1) & 0xFF
 	# if the `q` key was pressed, break from the loop
	##if key == ord("q"):
	##		break
#print(frame_height)
# do a bit of cleanup
vs.release()
out.release()
cv2.destroyAllWindows()

	
