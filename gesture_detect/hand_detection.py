import numpy as np
import cv2


# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
hand_cascade = cv2.CascadeClassifier('hand_haar.xml')
#creating the oject to store the video
cap = cv2.VideoCapture(0)



i = 1
while(True):
    # Capture frame-by-frame
    status, img = cap.read()
    if (status == False):
    	print "not capturing the video frames"
    	break

    # Our operations on the frame come here
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    print hand
    for (x,y,w,h) in hand:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		# roi_gray = gray[y:y+h, x:x+w]
		# roi_color = img[y:y+h, x:x+w]
		# eyes = eye_cascade.detectMultiScale(roi_gray)
		# for (ex,ey,ew,eh) in eyes:
		# 	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()