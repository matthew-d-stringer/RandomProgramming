import cv2
import numpy as numpy
from grip import GripPipeline

W = 320
H = 240

# img = cv2.imread('../resources/cargoship2.png',cv2.IMREAD_COLOR)
img = cv2.imread('../resources/missingPart.png',cv2.IMREAD_COLOR)

height, width, depth = img.shape

scaleX = W/width
scaleY = H/height
newX,newY = img.shape[1]*scaleX, img.shape[0]*scaleY
# newimg = cv2.resize(img,(int(newX),int(newY)))
newimg = cv2.resize(img,(int(320),int(240)))

gripCode = GripPipeline()
out = gripCode.process(newimg)
out = cv2.resize(out,(320*2,240*2))

# cv2.imshow('img', newimg)
cv2.imshow('out', out)
cv2.waitKey(0)
cv2.destroyAllWindows()