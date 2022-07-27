activation = True  # switch

# ------------------------------------------------

import cv2, os
import datetime
import time

faceDir = 'facedata'
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # width
cam.set(4, 480)  # height
faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier('haarcascade_eye.xml')
CollectData = 1

while (activation == True):
    time = datetime.datetime.now()
    time_now = time.strftime("%A.%B.%d.%Y.%H.%M.%S")
    retV, frame = cam.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(grey, 1.3, 5)  # frame, scaleFactor, minNe___
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
        fileName = 'face.' + time_now + '.jpg'
        cv2.imwrite(faceDir+'/'+fileName, frame)
        CollectData += 1
        roiGrey = grey[y:y+h,x:x+w]
        roiColor = frame[y:y+h, x:x+w]
        eyes = eyeDetector.detectMultiScale(roiGrey)
        for (xe, ye, we, he) in eyes:
            cv2.rectangle(roiColor, (xe,ye), (xe+we,ye+he), (0,255,255), 1)

    #cv2.imshow('Webcam', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break
    elif CollectData > 1:
        break

cam.release()
cv2.destroyAllWindows()