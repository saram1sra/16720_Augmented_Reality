import numpy as np
import cv2
from loadVid import loadVid
from matchFeatures import matchFeatures
from compositeWarp import compositeWarp
from skimage import color

# Load the video as numpy array
#backgroundVideo = loadVid("../data/charmander_rotate_short.mov") # The video serves as the background

backgroundVideo = np.load("../readVideo/charmander_rotate_short.npy") # The video serves as the background

# -- TODO: classification here to determine which template and 3D model to load --
templateImage = cv2.imread("../data/Charmander_card.jpg") # Load the card image

# -- TODO: use 3d model instead --
projectionImage = templateImage # The 3d model in obj format. For now it's just the template image

outVideo = cv2.VideoWriter('../results/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (backgroundVideo[0].shape[1],backgroundVideo[0].shape[0]))

templateImage = projectionImage

for i in range(len(backgroundVideo)):
    backgroundImage = backgroundVideo[i]
    projectionImageCropped = projectionImage # Currently no cropping is needed

    # Extract features and match
    # -- Note: if index out of range error occurs, lower numMatches variable in matchFeatures.py --
    pts1, pts2 = matchFeatures(templateImage, backgroundImage)

    # Compute homography using RANSAC
    M, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 8.0) # If performance sub-optimal, consider change the inlier threshold here

    # Generate composite image
    # TODO: -- replace the composite function with the 3D model version --
    compositeImage = compositeWarp(M, projectionImageCropped, backgroundImage)
    outVideo.write(compositeImage)
    if i % 50 == 0:
        print("Frame {} is recorded.".format(i))
    # cv2.imshow("Composite image", compositeImage)
    # cv2.waitKey(0)

outVideo.release()