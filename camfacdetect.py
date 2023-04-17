import cv2 as cv #import open cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') #reading and storing the classifier in a variable

cap = cv.VideoCapture(0) #capture the video

while True:
    _, img = cap.read() #read the video
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #converting the video to gray scale
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) #detecting the faces in the video

    for(x,y,w,h) in faces: 
        cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2) #drawing a rectangle around the face
        cv.imshow('img', img) #displaying the video
    
    if cv.waitKey(1) & 0xFF == ord('q'): #pressing q to quit the program
        cv.destroyAllWindows() #destroying all windows
        break

cap.release() #releasing the video