import numpy as np
import cv2
from loadVid import loadVid
from matchFeatures import matchFeatures
from compositeWarp import compositeWarp

# Load the video as numpy array
#backgroundVideo = loadVid("../data/book.mov") # The video serves as the background

# -- ***Note: Projection video CANNOT have more frames than the background video*** --

#projectionVideo = loadVid('../data/try.mp4') # The video to project onto the tracker in the background
backgroundVideo = np.load("../readVideo/background_video.npy") # The video serves as the background
projectionVideo = np.load('../readVideo/trump_try3_video.npy') # The video to project onto the tracker in the background

# Trim the longer background video to the shorter projection video
backgroundVideo = backgroundVideo[:len(projectionVideo)]
outVideo = cv2.VideoWriter('../results/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (backgroundVideo[0].shape[1],backgroundVideo[0].shape[0]))

templateImage = cv2.imread("../data/cv_cover.jpg")

for i in range(len(backgroundVideo)):
    backgroundImage = backgroundVideo[i]
    projectionImage = projectionVideo[i]
    projectionImageCropped = projectionImage[60:60+templateImage.shape[0], 250:250+templateImage.shape[1],:]
    #cv2.imshow("trump frame", projectionImageCropped)
    #cv2.waitKey(0)

    # Extract features and match
    pts1, pts2 = matchFeatures(templateImage, backgroundImage)

    # Compute homography using RANSAC
    M, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)

    # Display composite image
    compositeImage = compositeWarp(M, projectionImageCropped, backgroundImage)
    outVideo.write(compositeImage)
    if i % 50 == 0:
        print("Frame {} is recorded.".format(i))
    #cv2.imshow("Composite image", compositeImage)
    #cv2.waitKey(0)

outVideo.release()