import cv2
import numpy as np 

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120);

while True:

	_,frame=cap.read()
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #hsv is hue sat value

	lower_red=np.array([10,150,50])
	upper_red=np.array([100,255,150])

	mask=cv2.inRange(hsv,lower_red,upper_red)
	res=cv2.bitwise_and(frame,frame,mask=mask)

	cv2.imshow('frame',frame)
	cv2.imshow('mask',mask)
	cv2.imshow('result',res)

	
	if(cv2.waitKey(1) & 0xFF==ord('q')):
		break
#cv2.resizeWindow('frame', 100,100)
cv2.destroyAllWindows()
cap.release()
