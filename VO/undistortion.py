'''
Discription:
This file takes the images from data folder, undistorts thema 
and saves them in undist folder with name starting from image
The camera mat (camMat) and distortion coefecients (distCoef) are 
hard coded in the script
'''

import numpy as np
import cv2
from glob import glob

camMat = np.array([ (802.16370284, 0., 331.07811241), (0., 800.3178343, 227.26151634), (0., 0., 1.) ])
distCoef = np.array([.0988377156, -1.47250476, 0.00295115277, .000583523751, 5.82444317])

# output folder and files
undist_name = "undist/image"

# reading the files from the source folder
img_list = glob("data/*.jpeg")
#running the loop for undistorting the images
img_n = 1
for img_name in img_list:
	src_img = cv2.imread("data/image%d.jpeg" % img_n) 


	undist_img = cv2.undistort(src_img,camMat,distCoef)
	cv2.imwrite(undist_name + str(img_n) + ".jpg" , undist_img)
	img_n = img_n + 1