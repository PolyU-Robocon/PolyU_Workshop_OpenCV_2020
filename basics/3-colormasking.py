# import the necessary packages
import numpy as np
import cv2

# define the lower and upper boundaries of the "color" in the HSV color space
# Yellow Ball
#colorLower = np.array([21,92,0])
#colorUpper = np.array([67,255,255])
# Pink/Red Ball
colorLower = np.array([160,135,25])
colorUpper = np.array([179,255,255])
# ^ Notice HSV Hue is 0 ~ 179!

# grab the reference to the webcam
cap = cv2.VideoCapture(0)

# keep looping
while True:
	# grab the current frame
	_, frame = cap.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
 
	# resize the frame, blur it, and convert it to the HSV color space
	frame = cv2.resize(frame, (848, 480))
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color
	mask = cv2.inRange(hsv, colorLower, colorUpper)

	# show the frame to our screen
	cv2.imshow("Color", frame)
	cv2.imshow("Masked", mask)

	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# stop the camera video stream
cap.release()

# close all windows
cv2.destroyAllWindows()
