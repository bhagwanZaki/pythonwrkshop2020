#THIS IS PROGRAM MADE BY OWN THIS IS DEMO


import cv2 

# img = cv2.imread("galaxy.jpg",1)
# img1 = cv2.imread("galaxy.jpg",1)
# print(img)
# print(type(img))
# print(img.shape)
# print(img1)
# print(type(img1))
# print(img1.shape)
# print(img1.ndim)
# cv2.imshow("galaxy",img1)
# cv2.waitKey(22000)
# cv2.destr/oyAllWindows


# resize_img = cv2.resize(img1,(1000,1000))
# cv2.imshow("galaxy",resize_img)

# a = []
# a.append(input())
while True:
    a = []
    a.append(input())
    for pic in a:
        print(a)
        img = cv2.imread(pic,1)
        r_img =cv2.resize(img,(int(img.shape[1]/2),int(img.shape[1]/2)))
        cv2.imshow("galaxy",r_img)
        cv2.imwrite("fil.jpg",r_img)
        key=cv2.waitKey(1)
        key1=str(input())
        cv2.destroyAllWindows


    if(key1==ord('q')):
        cv2.destroyAllWindows
    else:
        pass
