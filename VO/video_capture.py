import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
#creating the oject to store the video
cap = cv2.VideoCapture(1)
# setting the FPS to 15 ::::: CV_CAP_PROP_FPS its integer value is 5
cap.set(5,10)

print str(cap.get(5))
i = 1
while(True):
    print str(i) + "\n"
    # Capture frame-by-frame
    status, img = cap.read()
    if (status == False):
    	print "not capturing the video frames"
    	break

    # Our operations on the frame come here
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',frame)	

    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(i>10) :              # waiting for image to stabilize the colours
        path = "data/image" + str(i-10) + ".jpeg"
        retVal =  cv2.imwrite(path,img)
        if (retVal == False):
            print "not saving the picture"
            break   
    i = i+1 
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()