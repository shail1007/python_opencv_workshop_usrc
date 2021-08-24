import cv2
import numpy as np

def rescale_frame(frame, scale = 0.5):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

def rotate(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, scale = 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)

img = cv2.imread('..\Photos\cat.jpg')

img = rescale_frame(img)

center = (int(img.shape[1]/2), int(img.shape[0]/2))
cv2.circle(img, center, 40, (225,225,225), thickness = 1)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.blur(img, (3,3))

img = cv2.Canny(img, 150,175)

img = rotate(img, 45)

cv2.imshow('Image', img)
