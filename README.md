# PolyU_Workshop_OpenCV_2020

Host : The Hong Kong Institution of Engineers(HKIE), HKIESC-PolyU , PolyU Enginnering Club, PolyU Robotics Team
Presenter : @vinesmsuic (From PolyU Robotics Team)


This workshop will briefly introduce Computer Vision and OpenCV. 
OpenCV is a robust library for processing images.


## Prerequisite

* Have Python3 Installed
* Have PIP3 installed
* Basic knowledge of Python


## Preparation

Download the Repo through `git clone`

```shell
$ git clone https://github.com/PolyU-Robocon/PolyU_Workshop_OpenCV_2020.git
```

or download the Repo hitting that `Download ZIP` Button.

<img src="https://i.imgur.com/9kyv1pQ.png" style="zoom:33%;" />


Install the libraries needed (You need to first `cd` to the repo.)

```shell
$ pip3 install -U -r requirement.txt
```

In case the above code got error, try to install those dependencies on your own.

* `opencv-python`
* `imutils`
* `opencv-contrib-python`

> For Windows/MacOS, you may use [anaconda](https://www.anaconda.com/) to get opencv
> Firstly, install [anaconda](https://www.anaconda.com/) , then type the commands:
> ```shell
> $ conda install -c conda-forge opencv
> $ sudo pip3 install imutils
> $ sudo pip3 install opencv-contrib-python
> ```

> For Linux distro, use the below command to get opencv
> ```shell
> $ sudo apt install python3-opencv
> $ sudo pip3 install imutils
> $ sudo pip3 install opencv-contrib-python
> ```


Then run `checking.py` to verify installation (You need to `cd` to the `scripts` folder)

```shell
$ cd scripts
$ python3 checking.py 
```

You should see something like this:

```
---------------------------------------
My Python version is: 3.7.4
My OpenCV version is: 4.4.0
---------------------------------------
```

Now you should be able to run the other files.

## Content

### Notes

* `lecturenotes.md` - Conceptual notes.
* `quicknotes.md` - Explain python code.

### Basics

* `checking.py` - check python and opencv versions
* `webcam.py` - start camera through opencv
* `imagelayers.py` - learn about the image layers
* `colormasking` - learn about masking
* `colortracking.py` - color tracker for learning color filtering
* `colortrackingFull.py` - brief introduction to imutil

### Extra

* `colorthresholder.py` - color filter picker
* `canny.py` - cannyedge detection
* `selectable-tracker.py` - selectable object tracking using tracker

### Demo Videos

* `max_heli.mp4` - a short clip of 3D modelling. Author @vinesmsuic
* `dvd.mp4` - a short clip of dvd screensaver. source from https://www.youtube.com/watch?v=3hc-GxV1BS8 
 

