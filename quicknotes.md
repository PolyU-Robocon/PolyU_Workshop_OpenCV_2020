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





* `cap.read()` returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of the video by checking this return value.
* `cv2.imshow(title,frame)` takes the title as first parameter then frame as second parameter.
* `cap.release()` and `cv2.destroyAllWindows()` are the methods to close video files or the capturing device, and destroy the window, which was created by the `imshow` method.
* `cv2.resize(frame, (width, height))` allows you to resize the video window.



## imagelayers.py



<img src="https://brohrer.github.io/images/image_processing/three_d_array.png" style="zoom:50%;" />

The above image is not correct in OpenCV's situation.

[Why OpenCV store color in BGR?](https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/)

> The reason the early developers at OpenCV chose BGR color format is that back then BGR color format was popular among camera manufacturers and software providers. E.g. in Windows, when specifying color value using [COLORREF](https://msdn.microsoft.com/en-us/library/dd183449(v=vs.85).aspx) they use the BGR format **0x00bbggrr**.
>
> BGR was a choice made for historical reasons and now we have to live with it.





* `frame[column, row, channel]`
  * `R[:,:,0]` means all columns, all rows in the first channel (which is Blue) of the frame `R`.
* `.copy()` is a method in Numpy. It will create a copy of the array you need.







## colormasking.py



[Why do we use the HSV colour space so often in vision and image processing?](https://dsp.stackexchange.com/questions/2687/why-do-we-use-the-hsv-colour-space-so-often-in-vision-and-image-processing)

> The simple answer is that unlike [RGB](http://en.wikipedia.org/wiki/RGB_color_space), [HSV](http://en.wikipedia.org/wiki/HSL_and_HSV) separates *luma*, or the image intensity, from *chroma* or the color information. This is very useful in many applications. For example, if you want to do histogram equalization of a color image, you probably want to do that only on the intensity component, and leave the color components alone. Otherwise you will get very strange colors.
>
> In computer vision you often want to separate color components from intensity for various reasons, such as robustness to lighting changes, or removing shadows.





* `np.array()` creates an array.
* `cv2.cvtColor()` allows you to convert a color into another space.
  * `cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)` from BGR to HSV
* `cv2.inRange(frame, lowerbound, upperbound)`
  * For color between lowerbound and upperbound, value become 255 (white)
  * For color not in lowerbound and upperbound, value become 0 (black)





For Tuning the mask color we want, we can use :

* http://colorizer.org/
* or use the `colorthresholder.py` script in extra folder (More robust)







## Color Tracking



* `cv2.findContours()` returns (frame,contours,hierarchy).
  * Note for some versions of opencv might only return (contours,hierarchy).
* `cv2.RETR_EXTERNAL`  retrieves only the extreme outer contours
  * You could also try with `cv2.RETR_LIST`, `cv2.RETR_CCOMP`, or `cv2.RETR_TREE`.
* `cv2.CHAIN_APPROX_SIMPLE` means the algorithm we are using for getting contours.
  * `cv2.CHAIN_APPROX_SIMPLE` removes all redundant points and compresses the contour, thereby saving memory
  * You could also try with `cv2.CHAIN_APPROX_NONE` to find all the boundary points
* https://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html
* `cv2.circle(frame, center_coordinates, radius, color, thickness)` allows you to draw a circle in your window.
  * `cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)`





## Full Code



**What is GaussianBlur?**

> GuassianBlur is typically used to reduce image noise and reduce detail.
>
> <img src="https://upload.wikimedia.org/wikipedia/commons/d/d7/Halftone%2C_Gaussian_Blur.jpg" style="zoom:50%;" />
>
> 





**What is Dilation and Erosion, Opening and Closing?**

![](https://image.slidesharecdn.com/dilationanderosion-140918230208-phpapp01/95/dilation-and-erosion-5-638.jpg?cb=1411081368)

TLDR:

* Dilation - Add pixels to the boundaries of objects in an image
* Erosion - Removes pixels at the boundaries of objects in an image
* Opening - Erosion then Dilation
* Closing - Dilation then Erosion

Note in OpenCV recognize WHITE as object itself.

> So the effect of dilation and erosion might do the reverse of what you expect.







**What is `imutils`?** 

> `imutils` is A series of convenience functions to make basic image processing functions such as translation, rotation, resizing, skeletonization, and displaying Matplotlib images easier with OpenCV and ***both*** Python 2.7 and Python 3.
>
>
> https://github.com/jrosebr1/imutils/blob/master/imutils/convenience.py



Explaination of `imutils.grab_contours()`:

<img src="https://i.imgur.com/UGaSSOF.png" style="zoom:50%;" />



Explaination of `imutils.resize()`:

<img src="https://i.imgur.com/RGtEE1O.png" style="zoom:50%;" />



