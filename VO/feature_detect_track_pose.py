import numpy as np
import cv2
from matplotlib import pyplot as plt
#loading the image
img1 = cv2.imread('data/image2.jpeg',0)
img2 = cv2.imread('data/image15.jpeg',0)


color = np.random.randint(0,255,(100,3))

feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
#fast = cv2.FastFeatureDetector()
p0 = cv2.goodFeaturesToTrack(img1, mask = None, **feature_params)

# find and draw the keypoints
#p0 = fast.detect(img,None)
print "number of key points " + str(len(p0))

#drawimg2 = cv2.drawKeypoints(img1, p0, color=(255,0,0))

#cv2.imshow("image with key points", drawimg2)
#cv2.waitKey(0)

#while (1) :

# feature tracking
 # Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

p1, st, err = cv2.calcOpticalFlowPyrLK(img1, img2, p0, None, **lk_params)

mask = np.zeros_like(img1)

good_new = p1[st==1]
good_old = p0[st==1]
 


for i,(new,old) in enumerate(zip(good_new,good_old)):
   a,b = new.ravel()
   c,d = old.ravel()
   mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
   frame = cv2.circle(img2,(a,b),5,color[i].tolist(),-1)
img = cv2.add(img2,mask)
cv2.imshow('frame',img)
cv2.imshow('frame 1', img1)
cv2.imshow('frame 2', img2)
cv2.waitKey(0)
#k = cv2.waitKey(30) & 0xff


#E = findEssentialMat(points2, points1, focal, pp, RANSAC, 0.999, 1.0, mask);