import numpy as np
import cv2
img=cv2.imread('/users/tusharnema/Desktop/dog.jpg',cv2.IMREAD_COLOR)

px=img[55,55] #color value for the given pixel
img[55,55]=[255,0,255] #changing color of that pixel
#print(px)

#region of image

roi=img[100:350, 120:229]
#print(roi)
img[100:350, 120:229]=[255,255,255] #changing color of the entire region

dog_face=img[520:610,520:600] #copying a region

img[0:90,0:80]=dog_face #pasting that region

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()