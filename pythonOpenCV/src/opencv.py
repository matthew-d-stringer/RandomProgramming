import cv2
import numpy as numpy
from grip import GripPipeline

def processImg(dir, gripCode):
    img = cv2.imread(dir, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (320,240))
    out = gripCode.process(img)
    scale = 2
    out = cv2.resize(out, (320*scale,240*scale))
    cv2.imshow(dir,out)

dirBegin = '../resources/'

gripCode = GripPipeline()

processImg(dirBegin+'cargoship.png',gripCode)
processImg(dirBegin+'cargoship2.png',gripCode)
processImg(dirBegin+'cargoshipNoise.png',gripCode)
processImg(dirBegin+'confusingTarget.png',gripCode)
processImg(dirBegin+'missingPart.png',gripCode)
processImg(dirBegin+'multipleTargets.png',gripCode)
processImg(dirBegin+'target.png',gripCode)

cv2.waitKey(0)
cv2.destroyAllWindows()