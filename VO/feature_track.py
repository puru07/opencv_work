import numpy as np
import cv2
from glob import glob
from numpy import linalg as LA
import numpy as np
# reading the files from the source folder
img_list = glob("data/*.jpeg")

#camera matrix
camMat = np.array([ (802.16370284, 0., 331.07811241), (0., 800.3178343, 227.26151634), (0., 0., 1.) ])

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
											 qualityLevel = 0.3,
											 minDistance = 7,
											 blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
									maxLevel = 2,
									criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
old_frame = cv2.imread('data/image1.jpeg')
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)


# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)


#starting the loop
img_n = 2
for img_name in img_list:
	frame = cv2.imread("data/image%d.jpeg" % img_n)
	img_n = img_n +1 
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#calculate opticsl flow
	p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params) 
	# print str(p0)
	# print str(p1)
	# print str(st)

	#select good points
	good_new = p1[st==1]
	good_old = p0[st==1]

	# draw the tracks
	for i,(new,old) in enumerate(zip(good_new,good_old)):
		a,b = new.ravel()
		c,d = old.ravel()
		mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)
		frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)
	img = cv2.add(frame,mask)
	'''
	cv2.imshow('frame',img)
	k = cv2.waitKey(0) & 0xff
	if k == 27:
		break
	'''
	focal = 800
	pp = (331,227.26)
	# getting the essential matrix and rotation & translation vectors
	E, mask2 = cv2.findEssentialMat(good_new, good_old,focal,pp,cv2.RANSAC,0.999,1.0)
	
	
	points,Rot, Trans,  mask3 = cv2.recoverPose(E,good_new, good_old,camMat,mask2)

	print str(Trans)
	print str(Rot`)
	# Now update the previous frame and previous points
	old_gray = frame_gray.copy()
	p0 = good_new.reshape(-1,1,2)


cv2.destroyAllWindows()