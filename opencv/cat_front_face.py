import cv2
img = cv2.imread('C:/Users/hetao/Desktop/cat.png')
print(img)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('face1',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
faceCascade = cv2.CascadeClassifier(
    r'C:\Users\hetao\Desktop\haarcascade_frontalcatface.xml'
)
faces = faceCascade.detectMultiScale(
    img,
    scaleFactor = 1.3,
    minNeighbors = 3,
    minSize = (32,32)
)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



