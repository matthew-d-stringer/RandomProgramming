import cv2
import numpy as numpy
from grip import GripPipeline

img = cv2.imread('../resources/cargoship2.png',cv2.IMREAD_COLOR)
# img = cv2.imread('../resources/multipleTargets.png',cv2.IMREAD_COLOR)

gripCode = GripPipeline()
out = gripCode.process(img)

# cv2.imshow('img', img)
cv2.imshow('out', out)
cv2.waitKey(0)
cv2.destroyAllWindows()