import numpy as np
from skimage import color
import cv2
import matplotlib.pyplot as plt

def plotMatches(im1, im2, pts1, pts2):
    fig = plt.figure()
    # draw two images side by side
    imH = max(im1.shape[0], im2.shape[0])
    im = np.zeros((imH, im1.shape[1]+im2.shape[1]), dtype='uint8')
    im[0:im1.shape[0], 0:im1.shape[1]] = im1
    im[0:im2.shape[0], im1.shape[1]:] = im2
    plt.imshow(im, cmap='gray')

    for i in range(pts1.shape[0]):
        pt1 = pts1[i]
        pt2 = pts2[i].copy()
        pt2[0] += im1.shape[1]
        x = np.asarray([pt1[0], pt2[0]])
        y = np.asarray([pt1[1], pt2[1]])
        plt.plot(x,y,'r')
        plt.plot(x,y,'g.')
    plt.show()

def matchFeatures(im1, im2):
    # Input: two images in which the features are extracted and matched
    # Output: pts1, pts2, where the locations of the matched features are in two images

    # Convert the images to grayscale if they are RGBs
    im1Shape = im1.shape
    im2Shape = im2.shape
    numMatches = 100   # Change this parameter if encountering index out of range!

    # Detect features in both images
    # fastFeatureDetector = cv2.FastFeatureDetector_create() # Fast feature here with maximum suppression
    # keypoints1 = fastFeatureDetector.detect(im1,None)
    # keypoints2 = fastFeatureDetector.detect(im2,None)
    orbFeatureDetector = cv2.ORB_create()  # ORB feature here with maximum suppression
    keypoints1 = orbFeatureDetector.detect(im1,None)
    keypoints2 = orbFeatureDetector.detect(im2,None)

    # Extract descriptors
    #briefExtractor = cv2.xfeatures2d.BriefDescriptorExtractor_create() # BRIEF descriptor
    #keypoints1, descriptor1 = briefExtractor.compute(im1, keypoints1)
    #keypoints2, descriptor2 = briefExtractor.compute(im2, keypoints2)

    keypoints1, descriptor1 = orbFeatureDetector.compute(im1, keypoints1)
    keypoints2, descriptor2 = orbFeatureDetector.compute(im2, keypoints2)

    # Match features using the descriptors
    bfMatcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bfMatcher.match(descriptor1, descriptor2)
    matchesSorted = sorted(matches, key = lambda x:x.distance)

    # Matching points
    pts1 = np.zeros((numMatches,2), dtype='int')
    pts2 = np.zeros((numMatches,2), dtype='int')

    for i in range(numMatches):
        loc1 = matchesSorted[i].queryIdx
        loc2 = matchesSorted[i].trainIdx
        pt1 = np.array(keypoints1[loc1].pt)
        pt2 = np.array(keypoints2[loc2].pt)
        pts1[i,:] = pt1
        pts2[i,:] = pt2

    #tmp = img1
    #img3 = cv2.drawMatches(im1Gray, keypoints1, im2Gray, keypoints2, matchesSorted[:10], flags=2, outImg=tmp)
    #plt.imshow(img3)
    #plt.show()
    return pts1, pts2

# im1 = cv2.imread('../data/cv_cover.jpg',0)
# im2 = cv2.imread('../data/cv_desk.png',0)
# pts1, pts2 = matchFeatures(im1, im2)
#
# # Convert the images to grayscale if they are RGBs
# im1Shape = im1.shape
# im2Shape = im2.shape
# im1Gray = None
# im2Gray = None
# numMatches = 10
# if len(im1Shape) == 3:
#     im1Gray = color.rgb2gray(im1)
# else:
#     im1Gray = im1
#
# if len(im2Shape) == 3:
#     im2Gray = color.rgb2gray(im2)
# else:
#     im2Gray = im2
#
# plotMatches(im1Gray, im2Gray, pts1, pts2)
#
