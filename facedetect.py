import cv2 as cv #impost open cv as cv
import numpy as np

img = cv.imread('photos/human.jpeg') #reading the image

#gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #make the image gray 
cv.imshow('Human', gray) 

haar_cascade = cv.CascadeClassifier('haar_face.xml') #read the haar xml file

facerec = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) #storing the dtetction value and position 

print(f'Number of faces found = {len(facerec)}') #printing the number of faces

for (x,y,w,h) in facerec: #making a loop for the rectengle
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2) #drawing a rectengle in the detection position 

cv.imshow('detected faces:',img) #show the detected face

cv.waitKey(0) #delay