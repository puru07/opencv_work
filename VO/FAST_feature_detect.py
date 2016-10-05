import numpy as np
import cv2
from matplotlib import pyplot as plt
#loading the image
img = cv2.imread('data/image2.jpeg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector()

# find and draw the keypoints
kp = fast.detect(img,None)

img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))

cv2.imshow("image with key points", img2)
cv2.waitKey(0)

# Print all default params
print "Threshold: ", fast.getInt('threshold')
print "nonmaxSuppression: ", fast.getBool('nonmaxSuppression')
#print "neighborhood: ", fast.getInt('type')
print "Total Keypoints with nonmaxSuppression: ", len(kp)


# Disable nonmaxSuppression
fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)
print "Total Keypoints without nonmaxSuppression: ", len(kp)

img3 = cv2.drawKeypoints(img, kp, color=(255,0,0))
cv2.imshow("image with nonmaxSuppression disabled ", img3)
cv2.waitKey(0)