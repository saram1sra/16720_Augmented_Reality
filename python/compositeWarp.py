import numpy as np
import cv2

def compositeWarp(H, template, img):
    # Input: the 3x3 homography that warps template onto the image
    # Output: a composited image with the warping applied

    # Warp template by appropriate homography
    templateWarpped = cv2.warpPerspective(template, H, (img.shape[1],img.shape[0]))

    # cv2.imshow("warpped", templateWarpped)
    # cv2.waitKey(0)
    # Use mask to combine the warped template and the image
    templateWarpped[np.where(templateWarpped == 0)] = img[np.where(templateWarpped == 0)]

    return templateWarpped

