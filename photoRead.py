import cv2 as cv

img = cv.imread('photos/cat.jfif')

cv.imshow('Cat', img)

cv.waitKey(0)


