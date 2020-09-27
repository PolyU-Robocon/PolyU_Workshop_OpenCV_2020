# PolyU_Workshop_OpenCV_2020


This workshop will briefly introduce Image Processing and OpenCV, a robust library for processing images.



## Prerequisite

* Have Python3 Installed
* Have PIP installed



## Preparation



Download the Repo through `git clone`

```shell
$ git clone https://github.com/PolyU-Robocon/PolyU_Workshop_OpenCV_2020.git
```

or download the Repo hitting that `Download ZIP` Button.

<img src="https://i.imgur.com/9kyv1pQ.png" style="zoom:33%;" />





Install the libraries needed (You need to first `cd` to the repo.)

```shell
$ pip install -U -r requirement.txt
```



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

### Scripts

* `webcam.py` - start camera through opencv
* `canny.py` - cannyedge detection
* `colortracking.py` - color tracker for learning HSV
* `selectable-tracker.py` - selectable object tracker (Bonus)


### Demo Videos

* `max_heli.mp4` - a short clip of 3D modelling. Author @vinesmsuic
* `dvd.mp4` - a short clip of dvd screensaver. source from https://www.youtube.com/watch?v=3hc-GxV1BS8 
 

