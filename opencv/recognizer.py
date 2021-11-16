import cv2
import numpy as np
# from numpy.core.records import array

images = []
images.append(cv2.imread('zhong1.png',cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread('zhong2.png',cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread('zhang1.png',cv2.IMREAD_GRAYSCALE))
images.append(cv2.imread('zhang2.png',cv2.IMREAD_GRAYSCALE))
print(images)

labels = [0,0,1,1]
reg = cv2.face.LBPHFaceRecognizer_create()
reg.train(images,np.array(labels))
