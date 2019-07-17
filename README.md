# 16720 Project: AR

Projecting 3D model onto real-world environment with the correct context

## Team Members: 
[Sara Misra](https://github.com/saramsra)\
[Olivia Xu](https://github.com/olimengia)\
[Naman Gupta](https://github.com/OwlCoder)

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
https://drive.google.com/open?id=1mbtFCg06tAgH0FXdSxS1u-NDhQrVKd92

## Code structure
* Repo root
  * python
    * ar_model.py: the new main function that we're going to use 
    * ar.py: old code
    * compositeWarp.py: After-warping image generation
    * loadVid.py: Convert a video file to numpy array that stores each frame
    * matchFeatures.py: find point correspondence in two images
    * unitTest.py: unit test to make sure the warping is working correctly
  * data
    * Three card images
