import cv2 as cv

image = cv.imread('photos/cat.jfif')
cv.imshow('cat', image)

#convert to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)    

#blur
blur = cv.GaussianBlur(image, (3547,2333), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
canny = cv.Canny(blur, 75, 75)
cv.imshow('canny', canny)

#dilating the image

dilated = cv.dilate(canny, (7,7), iterations=3)

cv.imshow('dilated', dilated)

cv.waitKey(0)