# Images



## What are Images?

* 2-Dimensional representation of the visible light spectrum
* Each pixel point corresponds to a different color which means that reflects different wavelengths of light

<img src="https://i.imgur.com/Wp5yX3k.png" style="zoom:50%;" />



## How do Computer store images?

* OpenCV use **RGB** color space by default. [What is RGB?](https://en.wikipedia.org/wiki/RGB_color_model)
* Each pixel corrdinate (x,y) of a 2D plane contains 3 values ranging for intensities of 0 to 255 (8-bit).
  * Red
  * Green
  * Blue



### Images are stored in multi-dimensional arrays

**1-dimensional array**

<img src="https://www.mvps.net/docs/wp-content/uploads/2019/03/Array-data-structure.jpg" style="zoom:33%;" />

**2-dimensional array**

Think of it like an x y coordinate system.

<img src="https://www.tutorialspoint.com/cprogramming/images/two_dimensional_arrays.jpg" style="zoom:67%;" />

**3-dimensional array** <- Where images are stored

Think of this seeming two dimensional array but these are stacks behind them.

<img src="https://brohrer.github.io/images/image_processing/three_d_array.png" style="zoom:50%;" />

<img src="https://i.imgur.com/WfMGg6b.png" style="zoom:50%;" />





## RGB Color Space

RGB is an additive color model that generates colors by combining blue, green and red and different intensities/brightness.

OpenCV's default color space is RGB.



### RGB Color Model

![](https://i.gifer.com/ATYY.gif)

<img src="https://i.imgur.com/SL80B5f.png" style="zoom:50%;" />

* Each colour appears in its primary spectral components of R, G and B
  * A 3-D Cartesian co-ordinate system
  * The Grayscale (Points of equal RGB values) extends from origin to farthest point
  * Different colors are points on or inside the cube
* Images comprise 3 independent image plances (each for R,G,B respectively.)
* The number of bits representing each pixel in RGB space is called pixel depth
  * Each R,G,B image is an 8-bit image
  * Each RGB color pixel has a depth of 24 bits - full-color image.
  * The total number of colors = $(2^8)^3 = 16,777,216$



<img src="https://i.imgur.com/RKzvLDE.png" style="zoom:50%;" />



> Note : OpenCV actually stores color in the BGR format.
>
> 
>
> ![](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Art/color_profiles.gif)
>
> ![](https://caffe2.ai/static/images/tutorial-image-prep-BGR.png)
>
> Why? We use BRG order on computers due to how unsigned 32-bit integers are stored in memory, it still ends up being stored as RGB. The integer representing a color e.g. 0x00BBGGRR will be stored as 0xRRGGBB00.



### Grayscale

Grayscale is a range of shades of gray without apparent color. The darkest possible shade is black, which is the total absence of transmitted or reflected light. The lightest possible shade is white, the total transmission or reflection of light at all visible wavelengths.

![](https://1.bp.blogspot.com/-2wsOF9awhCQ/Vl8GqWa8OaI/AAAAAAAAA9s/iFjSnJc_m3A/s1600/grayscale.jpg)



## HSV Color Space

HSV (Hue, Saturation & Value/Brightness) is a color space that attempts to represent colors the way human perceive it. It stores color information in a cyclindrical representation of RGB color points.

### HSV Color Model

![](https://www.researchgate.net/profile/Ravindran_G/publication/321126312/figure/fig1/AS:561582682722304@1510903153364/llustration-of-the-HSV-Color-Space-B-Color-Feature-Extraction-Color-feature-is-extracted.png)

* Hue - Color Value (0-179)
* Saturation - Vibrancy of Color (0-255)
* Value - Brightness or Intensity (0-255)

![](https://raw.githubusercontent.com/shikitari/hsv_color/7bf85845e6f860e832c08493e9a1949cc8c29cf4/dist/demo.gif)

> HSV is useful in computer vision for color segmentation. In RGB, filtering specific colors isn't easy. However, HSV makes it much easier to set color ranges to filter specific colors as we perceive them.

### Color Filtering

> The Hue (Hue color range, goes from 0 to 180. NOT 360) and is mapped **differently than standard** in OpenCV.

Color Range Filters:

* Red - 165 to 15
* Green - 45 to 75
* Blue - 90 to 120

![](https://answers.opencv.org/upfiles/15186766673210035.png)

[Why is the range of Hue 0-180° in OpenCV?](https://stackoverflow.com/questions/16685707/why-is-the-range-of-hue-0-180-in-opencv)

> Now you understand why I said Hue is 0-179 in HSV space. 180 = 0.







# Getting Started with OpenCV



## What is OpenCV?

OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage then Itseez. The library is cross-platform and free for use under the open-source BSD license.

You can use either C++ or Python with it.



## OpenCV in Python

### Why Python?

* Python allows us to do to easily grasp complex concepts.
* Python is one of the easiest easiest languages for beginners 
* It stores images in numpy arrays which allows us to do some very powerful operations quite easily



