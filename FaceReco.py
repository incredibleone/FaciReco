import cv2
import numpy as np
eyeCascade = cv2.CascadeClassifier("C:\\Users\\anshu\\Documents\\haarcascade_eye.xml")
faceCascade = cv2.CascadeClassifier("C:\\Users\\anshu\\Documents\\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h),(255,0,0),2)
        roiGray = gray[y:y+h, x:x+w]
        roiColor = img[y:y+h, x:x+w]

        eyes = eyeCascade.detectMultiScale(roiGray)

        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roiColor, (ex,ey), (ex+ew,ey+eh),(0,255,0),2)
        
        cv2.imshow('img',img)
        k = cv2.waitKey(30)& 0xff

        if k =='27':
            break
cap.release()
cv2.destroyAllWindows()