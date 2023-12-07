import cv2
import sys

imagePath = "C:/Users/Arwin/Pictures/profile1.jpg"
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30))
print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

image = cv2.resize(image,(1920,1080))
cv2.imshow("Original Image", image)
cv2.waitKey(0)
