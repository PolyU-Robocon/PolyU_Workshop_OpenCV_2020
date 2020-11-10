# Quick Notes for OpenCV



## checking.py

```python
# Import OpenCV
import cv2

# Import platform
import platform

print("---------------------------------------")

# Print my Python version
print("My Python version is:",platform.python_version())

# Print my OpenCV version
print("My OpenCV version is:",cv2.__version__)

print("---------------------------------------")

```



You should see something like this:



```shell
---------------------------------------
My Python version is: 3.7.4
My OpenCV version is: 4.4.0
---------------------------------------
```



Now you should be able to run the other files.



## webcam.py

```python
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# keep looping
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # frame = cv2.resize(frame, (800, 500)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```



* `cap.read()` returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
* `cv2.imshow(title,frame)` takes the title as first parameter then frame as second parameter.
* `cap.release()` and `cv2.destroyAllWindows()` are the methods to close video files or the capturing device, and destroy the window, which was created by the `imshow` method.
* `cv2.resize(frame, (width, height))` allows you to resize the video window.



## imagelayers.py

```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# keep looping
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # Note OpenCV store colors in BGR format.

    frame = cv2.resize(frame, (800, 500))

    R = frame.copy()
    R[:,:,0] = 0 # Turn Blue channel to 0
    R[:,:,1] = 0 # Turn Green channel to 0
    # Now R has Red channel only

    G = frame.copy()
    G[:,:,0] = 0 # Turn Blue channel to 0
    G[:,:,2] = 0 # Turn Red channel to 0
    # Now R has Green channel only

    B = frame.copy()
    B[:,:,1] = 0 # Turn Green channel to 0
    B[:,:,2] = 0 # Turn Red channel to 0
    # Now R has Blue channel only

    # Display the resulting frame
    cv2.imshow('frame, Red Channel',R)
    cv2.imshow('frame, Green Channel',G)
    cv2.imshow('frame, Blue Channel',B)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```



<img src="https://brohrer.github.io/images/image_processing/three_d_array.png" style="zoom:50%;" />

`frame[column, row, channel]`

* `R[:,:,0]` means all columns, all rows in the first channel (which is Blue) of the frame `R`.





[Why OpenCV store color in BGR?](https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/)

> The reason the early developers at OpenCV chose BGR color format is that back then BGR color format was popular among camera manufacturers and software providers. E.g. in Windows, when specifying color value using [COLORREF](https://msdn.microsoft.com/en-us/library/dd183449(v=vs.85).aspx) they use the BGR format **0x00bbggrr**.
>
> BGR was a choice made for historical reasons and now we have to live with it.





## colormasking.py



```python
# import the necessary packages
import numpy as np
import cv2

# define the lower and upper boundaries of the "color" in the HSV color space
colorLower = (120,50,55)
colorUpper = (180,255,255)
# ^ Notice HSV Hue is 0 ~ 180!

# grab the reference to the webcam
cap = cv2.VideoCapture(0)

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
	frame = cv2.resize(frame, (800, 500))
	blurred = cv2.GaussianBlur(frame, (11, 11), 0) # eliminate noises
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
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

```



[Why do we use the HSV colour space so often in vision and image processing?](https://dsp.stackexchange.com/questions/2687/why-do-we-use-the-hsv-colour-space-so-often-in-vision-and-image-processing)

> The simple answer is that unlike [RGB](http://en.wikipedia.org/wiki/RGB_color_space), [HSV](http://en.wikipedia.org/wiki/HSL_and_HSV) separates *luma*, or the image intensity, from *chroma* or the color information. This is very useful in many applications. For example, if you want to do histogram equalization of a color image, you probably want to do that only on the intensity component, and leave the color components alone. Otherwise you will get very strange colors.
>
> In computer vision you often want to separate color components from intensity for various reasons, such as robustness to lighting changes, or removing shadows.



## Full Code



```python
# import the necessary packages
import numpy as np
import cv2
import imutils
#import time

# define the lower and upper boundaries of the "color" in the HSV color space
colorLower = (120,50,55)
colorUpper = (180,255,255)
# ^ Notice HSV Hue is 0 ~ 180!

 
# grab the reference to the webcam
#cap = cv2.VideoCapture(0)

# in case you want to grab the reference to a video
cap = cv2.VideoCapture("dvd.mp4")
 
# allow the camera or video file to warm up
#time.sleep(2.0)

# keep looping
while True:
	# grab the current frame
	#frame = vs.read()
	ret, frame = cap.read()

	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if frame is None:
		break
 
	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color, then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, colorLower, colorUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
 
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

```





What is `imutils`? 

> `imutils` is A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV and ***both*** Python 2.7 and Python 3.
>
>
> https://github.com/jrosebr1/imutils/blob/master/imutils/convenience.py



Explaination of `imutils.grab_contours()`:

<img src="https://i.imgur.com/UGaSSOF.png" style="zoom:50%;" />



Explaination of `imutils.resize()`:

<img src="https://i.imgur.com/RGtEE1O.png" style="zoom:50%;" />



