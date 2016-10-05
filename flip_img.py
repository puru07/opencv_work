import numpy as np
import cv2

img=cv2.imread('1.png')
rimg=img.copy()
fimg=img.copy()
rimg=cv2.flip(img,1)
fimg=cv2.flip(img,0)
cv2.imshow("Original", img)
cv2.imshow("vertical flip", rimg)
cv2.imshow("horizontal flip", fimg)
cv2.waitKey(0)
cv2.destroyAllWindows()