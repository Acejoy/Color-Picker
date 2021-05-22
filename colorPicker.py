import cv2
import numpy as np


def getColor(event, x, y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        if param == 'a':
            print('RGB color:',roi[y,x])
        elif param == 'b':
            print('HSV color:',roiHSV[y,x])

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap:
    print('Camera cant be opened')
    exit()

roi = None

cv2.namedWindow('roi')
cv2.setMouseCallback('roi',getColor,'a' )  
cv2.namedWindow('roiHSV')
cv2.setMouseCallback('roiHSV',getColor, 'b')  


while True:
    ret, flippedFrame = cap.read()
    frame = cv2.flip(flippedFrame,1)    
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if not ret:
        print('Frame not read correctly')
        break

    cv2.rectangle(frame, (330 , 90), (620, 400), (255,255,255), 2)
    roi = frame[92:388, 332:618]
    roiHSV = frameHSV[92:388, 332:618]
    
    cv2.imshow('camera feed', frame)
    cv2.imshow('roi', roi)
    cv2.imshow('roi in HSV', roiHSV)
    
    pressedKey = cv2.waitKey(1) &0xFF

    if pressedKey == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()