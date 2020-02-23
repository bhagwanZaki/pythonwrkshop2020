# this program is to detect face in a picture
#to do this we requre .xml file in which the we compare the pixel of picture with color all ready store in it





import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")       #this is xml file

img=cv2.imread("albaik.jpg")                                                             #the file is store in variable img 
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                                              #COLOR_BGR2GRAY is the format that our xml file convert

faces = face_cascade.detectMultiScale(grey_img,scaleFactor=1.009,minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)                                      #(x,y)this are the coodrdinates,(x+w,y+h) this is length and breadth of rectangle,(0,255,0) this is color code of(BGR),3 is the border width

print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[0]/3),int(img.shape[0]/3)))                #this will resize the picture
cv2.imshow("picture",resized)
cv2.waitKey(0)
cv2.destroyAllWindows




