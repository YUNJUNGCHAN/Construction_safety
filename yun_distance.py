from re import X
import cv2
import numpy as np

CONFIDENCE = 0.5
THRESHOLD = 0.3
LABELS = ['Person','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','Cell Phone','','','','','','','','','','','','','','','','','']

cap = cv2.VideoCapture(0)
net = cv2.dnn.readNetFromDarknet('cfg/yolov4.cfg', 'yolov4.weights')

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    H, W, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, scalefactor=1/255., size=(416, 416), swapRB=True)
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
            
            print('')
            cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
            cv2.putText(img, text='%s %.2f %d' % (LABELS[class_ids[i]], confidences[i], w), org=(x, y - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
            cv2.rectangle(img, pt1=(400,200), pt2=(900, 500), color=(0, 0, 255), thickness=2)
            cv2.putText(img, text='Restricted Area', org=(400, 200 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 0, 255), thickness=2)
            
   
            if class_ids[i] == 67:
                # cv2.imshow('result2', img[y:y+h , x:x+w])
                if x > 400 and y > 200 and x < 900 and y < 500 :
                    print('귀하의 스마트폰이 제한 구역에 들어와 있습니다!')
                    
    
    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break


