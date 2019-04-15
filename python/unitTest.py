import numpy as np
import cv2
from matchFeatures import matchFeatures
from matchFeatures import plotMatches
from compositeWarp import compositeWarp
from skimage import color


im1 = cv2.imread('../data/cv_cover.jpg',0)
im2 = cv2.imread('../data/cv_desk.png',0)

# Test for matchFeatures
pts1, pts2 = matchFeatures(im1, im2)

# Convert the images to grayscale if they are RGBs
im1Shape = im1.shape
im2Shape = im2.shape
im1Gray = None
im2Gray = None
numMatches = 10
if len(im1Shape) == 3:
    im1Gray = color.rgb2gray(im1)
else:
    im1Gray = im1

if len(im2Shape) == 3:
    im2Gray = color.rgb2gray(im2)
else:
    im2Gray = im2

#plotMatches(im1Gray, im2Gray, pts1, pts2)

# Test for compositeWarp

# Compute homography using RANSAC
M, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
templateWarpped = compositeWarp(M, im1Gray, im2Gray)
cv2.imshow("Composite image", templateWarpped)
cv2.waitKey(0)