import cv2

video=cv2.VideoCapture(r"cats.webm")    
print(type(video))
check = True        
while check:
    face_cascade=cv2.CascadeClassifier("dog.xml")
    check, frame =video.read()
    img = frame
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey_img,scaleFactor=1.01,minNeighbors=5)

    for x,y,w,h in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(50,255,64),3)
    
    
    cv2.imshow("video ka frame",frame)
    key=cv2.waitKey(1)
    
    
    if(key== ord('q')):
        break

cv2.destroyAllWindows
video.release()