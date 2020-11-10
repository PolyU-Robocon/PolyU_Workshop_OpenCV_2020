# import the necessary packages
import numpy as np
import cv2

# define the lower and upper boundaries of the "color" in the HSV color space
colorLower = (120,50,55)
colorUpper = (180,255,255)
# ^ Notice HSV Hue is 0 ~ 180!

 
# grab the reference to the webcam
cap = cv2.VideoCapture(0)

# keep looping
while True:
	# grab the current frame
	ret, frame = cap.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
 
	# resize the frame, blur it, and convert it to the HSV color space
	frame = cv2.resize(frame, (800, 500))
	blurred = cv2.GaussianBlur(frame, (11, 11), 0) # eliminate noises
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color
	mask = cv2.inRange(hsv, colorLower, colorUpper)

    # find contours in the mask and initialize the current (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	
    if len(cnts) == 2: 
        cnts = cnts[0] # For OpenCV v2.4, v4-beta, or v4-official
    elif len(cnts) == 3:
        cnts = cnts[1] # For OpenCV v3, v4-pre, or v4-alpha
 
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
 
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
 
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
