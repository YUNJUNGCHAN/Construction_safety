from re import X
import cv2
import numpy as np

import pandas as pd
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

#좌측 상단
x1, y1 = 600, 400

#우측 상단
x2, y2 = 1000, 400

#우측 하단
x3, y3 = 1200, 500

#좌측 하단
x4, y4 = 500, 500

CONFIDENCE = 0.01
THRESHOLD = 0.01
LABELS = ['person','bicycle','car','motorbike','aeroplane','bus','train','truck','boat','traffic light','fire hydrant','stop sign','parking meter','bench','bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe','backpack','umbrella','handbag','tie','suitcase','frisbee','skis','snowboard','sports ball','kite','baseball bat','baseball glove','skateboard','surfboard','tennis racket','bottle','wine glass','cup','fork','knife','spoon','bowl','banana','apple','sandwich','orange','broccoli','carrot','hot dog','pizza','donut','cake','chair','sofa','pottedplant','bed','diningtable','toilet','tvmonitor','laptop','mouse','remote','keyboard','cell phone','microwave','oven','toaster','sink','refrigerator','book','clock','vase','scissors','teddy bear','hair drier','toothbrush']

cap = cv2.VideoCapture('data/test.mp4')
#cap = cv2.VideoCapture(0)
net = cv2.dnn.readNetFromDarknet('/home/yun/darknet/cfg/yolov3.cfg', '/home/yun/darknet/yolov3.weights')

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    H, W, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, scalefactor=1/255, size=(608, 608), swapRB=True)
    net.setInput(blob)
    output = net.forward()

    boxes, confidences, class_ids = [], [], []

    for det in output:
        box = det[:4]
        scores = det[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > CONFIDENCE:
            cx, cy, w, h = box * np.array([W, H, W, H])
            x = cx - (w / 2)
            y = cy - (h / 2)

            boxes.append([int(x), int(y), int(w), int(h)])
            confidences.append(float(confidence))
            class_ids.append(class_id)

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD)

    if len(idxs) > 0:
        for i in idxs.flatten():
            x, y, w, h = boxes[i]
            
            pts1 = np.array([[x1,y1], [x2,y2], [x3,y3],[x4,y4]], dtype=np.int32) 
            polyList = [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
            polygon = Polygon(polyList)
            
            print('')
            cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=1)
            cv2.putText(img, text='%s %.2f %d' % (LABELS[class_ids[i]], confidences[i], w), org=(x, y - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=2)
            cv2.polylines(img, [pts1], True, (0,0,255), thickness=2)  
            cv2.putText(img, text='Restricted Area', org=(x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 255), thickness=2)
            
            if class_ids[i] == 0:
                print(x+(1/2*w),y+(1/2*h))
                Result = polygon.contains(Point(x+(1/2*w),y+(1/2*h)))
                print(Result)
                if Result == True :
                    print('작업자가 제한 구역 안에 들어와 있습니다')
                    cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)
                    
    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break


