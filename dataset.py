import cv2 as cv
import math
from pathlib import Path

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)
count = 1

print("Enter the name and id of the person")

userName = input('Enter the name: ')
userId = input('Enter the id: ')

def saveImage(img, userName, imgId):
    Path("dataset/{}".format(userName)).mkdir(parents=True, exist_ok=True)
    cv.imwrite("dataset/{}/{}.jpg".format(userName, imgId), img)

while True:
    _, img = cap.read()
    origianlImg = img.copy()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        confidence = int(((w+h)/(2))%100)
        cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv.putText(img, f"{confidence}%", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        cv.imshow('img', img)

    key = cv.waitKey(1)
    
    if key == ord('s'):
        if count  <= 1000:
            saveImage(origianlImg, userName, count)
            count += 1
        else:
            break
        
    elif key == ord('q'):
        break
  

cv.destroyAllWindows()
cap.release()