import cv2
import numpy as np

def loadVid(path):
    # input: A path of where the video file is
    # output: mov: frames of the video stored in an array ( Frames * Height * width * channel)
    video = cv2.VideoCapture(path)
    videoFrames = []
    # An initial read
    success, frame = video.read()
    videoFrames.append(frame)
    # Read the rest of the frames
    while success:
        success, frame = video.read()
        if success:
            videoFrames.append(frame)

    videoFrames = np.array(videoFrames)
    np.save("../readVideo/read_video.npy", videoFrames)
    video.release()
    print("video {} loaded".format(path))
    return videoFrames