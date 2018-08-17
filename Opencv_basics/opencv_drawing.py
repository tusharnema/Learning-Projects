import numpy as np 
import cv2
import matplotlib
matplotlib.use('TkAgg') #backend (alternatives available)
import matplotlib.pyplot as plt
img= cv2.imread('/Users/tusharnema/Desktop/dog.jpg',cv2.IMREAD_COLOR) #for reading the image



cv2.line(img,(0,0),(150,150),(255,255,255),15) #for drawing a line in the image

cv2.rectangle(img,(15,25),(150,150),(0,255,0),5) #for drawing a rectangle in the image

cv2.circle(img,(350,250),(150),(0,255,255),15) #for drawing a circle in the image

pts=np.array([[10,5],[20,30],[80,65],[400,22],[350,250]],np.int32)
#pts=pts.reshape(-1,1,2)
cv2.polylines(img,[pts],True,(0,123,255),12) #for drawing a polygon in the image


font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Yo doggy',(122,321),font,4,(21,33,255),2,cv2.LINE_AA)

imS = cv2.resize(img, (460, 340)) #for resizing the window

cv2.imshow('image',imS)
cv2.waitKey(0)
cv2.destroyAllWindows()