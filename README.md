# 16720 Project: AR

Projecting 3D model onto real-world environment with the correct context

## Tested on:

Python 3.6\
opencv 3.4.2


## Usage

In the main function ar.py, modify the path for where the input videos are.

If the videos haven't been pre-processed by loadVid.py (which takes in a video file and outputs the numpy array of the frames), use the lines
```python
# The environment video
projectionVideo = loadVid('../data/projectionVideoName.mp4') 
# What you want to project
backgroundVideo = loadVid('../data/backgroundVideoName.mp4') 
```

To import existing npy files, use the lines
```python
backgroundVideo = np.load("../readVideo/backgroundName.npy") 
projectionVideo = np.load('../readVideo/projectionName.npy') 
```
## Download pre-processed npy files
Background video: https://drive.google.com/open?id=1XidFY2vSv6kGsomkj6r-bDS-c-P0SB7v \
try.mp4: https://drive.google.com/open?id=1XcybRS1RlogC0WcybCvrgoy7SLv_hLEK \
try3.mp4: https://drive.google.com/open?id=1Jl1SdAXIdKR2F9ujZE0qsYbaOzQZvR5F \

## Code structure
* Repo root
  * python
    * ar.py: the main AR generation file. Specify the input video and output video inside the code before you run it
    * compositeWarp.py: After-warping image generation
    * loadVid.py: Convert a video file to numpy array that stores each frame
    * matchFeatures.py: find point correspondence in two images
    * unitTest.py: unit test to make sure the warping is working correctly
  * data
    * book.mov: the environment video
    * cv_cover.jpg: the template. Same book as in book.mov
    * rest of the trump videos: projection videos of different frame size and frame rate (I was experimenting with what is the correct frame size and frame rate to use to avoid glitching effect. Still need to figure out)
  * results
    * Output augmented videos
  * readVideo (create this folder and put the downloaded pre-processed npy files in it)
     * trump_try_video.npy (https://drive.google.com/open?id=1XcybRS1RlogC0WcybCvrgoy7SLv_hLEK)
     * background_video.npy (https://drive.google.com/open?id=1XidFY2vSv6kGsomkj6r-bDS-c-P0SB7v)
     * trump_try3_video.npy (https://drive.google.com/open?id=1Jl1SdAXIdKR2F9ujZE0qsYbaOzQZvR5F)
