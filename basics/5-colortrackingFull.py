# import the necessary packages
import numpy as np
import cv2
import imutils
#import time

# define the lower and upper boundaries of the "color" in the HSV color space
colorLower = np.array([0,136,0])
colorUpper = np.array([2,255,255])
# ^ Notice HSV Hue is 0 ~ 179!
 
# grab the reference to the webcam
cap = cv2.VideoCapture(0)

# in case you want to grab the reference to a video
#cap = cv2.VideoCapture("dvd.mp4")
 
# allow the camera or video file to warm up
#time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	_, frame = cap.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
 
	# resize the frame, blur it, and convert it to the HSV color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0) # eliminate noises
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color 
	mask = cv2.inRange(hsv, colorLower, colorUpper)

	# perform a series of dilations and erosions to remove any small blobs left in the mask
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current (x, y) center
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
 
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use it to compute the minimum enclosing circle
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
 
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle on the frame
			cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
 
	# show the frame to our screen
	cv2.imshow("Color Tracker", frame)
	cv2.imshow("Masked", mask)

	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# stop the camera video stream
cap.release()

# close all windows
cv2.destroyAllWindows()
