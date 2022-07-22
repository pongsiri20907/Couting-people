import cv2
import numpy as np
# from tracker import *

cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()
# tracker = cv2.legacy.TrackerMedianFlow_create()
onTracking = False

while True:
    # Read Video
    frame1 = frame2
    ret, frame2 = cap.read()

    # Create Line
    # cv2.line(frame1,(0,310),(500,280),(0,0,255),3)
    # cv2.line(frame2,(0,310),(1000,280),(0,0,255),3)

    #Background subtrction
    frame_diff = cv2.absdiff(frame1,frame2)

    # Convert image to gray scale
    gray = cv2.cvtColor(frame_diff,cv2.COLOR_BGR2GRAY)

    # Blur image [LOW PASS FILTER]
    blur0 = cv2.GaussianBlur(gray,(5,5),0)
    blur = cv2.GaussianBlur(blur0,(5,5),0)

    # Threshole
    thresh, result = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    # Dilation
    dilation = cv2.dilate(result,None,iterations=15)

    detections = []
    boxes = []
    ids = 0
    # Find countour
    contours, hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    if not onTracking:
        for cnts in contours:
            # Find Contour area
            area  = cv2.contourArea(cnts)
                
            if area < 10000:
                continue
                
            # Draw bounding box
            x, y, w, h = cv2.boundingRect(cnts)
            detections.append([x,y,w,h])

            #Objects tracking
            for (x,y,w,h) in detections:
                print(x,y,w,h)
                cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
                # if tracker.init(frame1,(x,y,w,h)):
                #     onTracking = True
    else:
        # success, bbox = tracker.update(frame1)
        if success:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame1,p1,p2,(0,255,0),2)
        else:
            # tracker = cv2.legacy.TrackerMedianFlow_create()
            onTracking = False

    # Show image
    cv2.imshow('BLUR image', blur)
    cv2.imshow('LAST image', dilation)
    #cv2.imshow('Contours image', frame1)
    cv2.imshow('Box', frame1)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()