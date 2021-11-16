import cv2
import numpy as np
font = cv2.FONT_HERSHEY_DUPLEX
pre_img =cv2.imread('zhong_test.png')
gray_img = cv2.cvtColor(pre_img,cv2.COLOR_RGB2GRAY)
faceCascade = cv2.CascadeClassifier(
    'haarcascade_frontalface_default.xml'
)
faces = faceCascade.detectMultiScale(
    gray_img,
    scaleFactor=1.3,
    minNeighbors = 3,
    minSize = (32,32)
)
images = []
images.append(cv2.imread('zhong1.png',cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread('zhong2.png',cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread('zhang1.png',cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread('zhang2.png',cv2.IMREAD_GRAYSCALE))

labels = [0,0,1,1]
reg = cv2.face.LBPHFaceRecognizer_create()
reg.train(images,np.array(labels))

label,confidence=reg.predict(gray_img)
for (x,y,w,h) in faces:
    cv2.rectangle(pre_img,
    (x,y),(x+w,y+h),(255,255,0),2)
    if confidence<100:
        if label ==0:
            name = 'zhongnanshan'
        else:
            name = 'zhangguimei'
    else:
        name = 'unknown'
    cv2.putText(pre_img,name,(x,y-10),font,1.0,(255,255,0),2)
cv2.imshow('face1',pre_img)
cv2.waitKey(0)
cv2.destroyAllWindows()