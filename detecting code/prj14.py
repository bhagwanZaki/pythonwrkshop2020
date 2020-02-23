# this program is used to detcte the the face in video
# every video consist of frame so here like previous program we have to detect face in each frame of whole video bu while loop
import cv2

video=cv2.VideoCapture(r"faceDetection.mp4")    
print(type(video))
# check, frame =video.read()      #check as boolean type and frame as numpy type this because the value return by video.read() one is boolean and another is numpy
check = True        
while check:
    face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    check, frame =video.read()
    img = frame
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey_img,scaleFactor=3.5,minNeighbors=5)

    for x,y,w,h in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(50,255,64),3)
    
    
    cv2.imshow("video ka frame",frame)
    key=cv2.waitKey(1)
    
    
    if(key== ord('q')):
        break

cv2.destroyAllWindows
video.release()

