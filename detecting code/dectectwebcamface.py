#program do to live detecting
import cv2

video=cv2.VideoCapture(0)    #if we put 0 this means we are accessing from webcam
print(type(video))
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
