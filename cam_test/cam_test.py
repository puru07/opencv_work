import numpy as np
import cv2
import matplotlib.pyplot as plt

#creating the oject to store the video
cap = cv2.VideoCapture(0)
#cv2.VideoCapture.set(int(CV_CAP_PROP_FPS),15)
i = 1
while(True):
    # Capture frame-by-frame
    status, img = cap.read()
    if (status == False):
    	print "not capturing the video frames"
    	break

    # Our operations on the frame come here
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',frame)	

    cv2.imshow('image',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()