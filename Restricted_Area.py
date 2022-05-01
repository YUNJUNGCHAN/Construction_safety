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

CONFIDENCE = 0.01 # 객체의 인식율이 1% 이상일 때 반응
THRESHOLD = 0.01  # Non-Maximum Suppression
LABELS = ['person','bicycle','car','motorbike','aeroplane','bus','train','truck','boat','traffic light','fire hydrant','stop sign','parking meter','bench','bird','cat','dog','horse','sheep','cow','elephant','bear','zebra','giraffe','backpack','umbrella','handbag','tie','suitcase','frisbee','skis','snowboard','sports ball','kite','baseball bat','baseball glove','skateboard','surfboard','tennis racket','bottle','wine glass','cup','fork','knife','spoon','bowl','banana','apple','sandwich','orange','broccoli','carrot','hot dog','pizza','donut','cake','chair','sofa','pottedplant','bed','diningtable','toilet','tvmonitor','laptop','mouse','remote','keyboard','cell phone','microwave','oven','toaster','sink','refrigerator','book','clock','vase','scissors','teddy bear','hair drier','toothbrush']

cap = cv2.VideoCapture('data/test.mp4') # 비디오 불러오기
#cap = cv2.VideoCapture(0) # 웹캠 영상 불러오기
net = cv2.dnn.readNetFromDarknet('/home/yun/darknet/cfg/yolov3.cfg', '/home/yun/darknet/yolov3.weights') # Darknet의 모델을 불러오기

while cap.isOpened(): # 비디오 열기
    ret, img = cap.read() # 비디오 읽기
    if not ret:
        break

    H, W, _ = img.shape # 비디오의 가로사이즈, 세로사이즈 저장

    blob = cv2.dnn.blobFromImage(img, scalefactor=1/255, size=(608, 608), swapRB=True) # 비디오 이미지 전처리
    net.setInput(blob) # 전처리 된 blob를 모델에 입력
    output = net.forward() # 모델로부터 추출

    boxes, confidences, class_ids = [], [], [] # 변수 3개(박스, 정확도, ID)가 들어갈 자리 만들기.

    for det in output: # 모델로부터 추출된 output 열기
        box = det[:4] # 앞의 4개의 박스값 가져오기
        scores = det[5:] # 뒤의 Score 값 가져오기
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > CONFIDENCE: # 사전에 설정한 CONFIDENCE 값 이상이면 반응 시작
            cx, cy, w, h = box * np.array([W, H, W, H]) # Normalized 된 값을 픽셀로 변환
            x = cx - (w / 2)
            y = cy - (h / 2)

            boxes.append([int(x), int(y), int(w), int(h)]) # 결과 저장하기
            confidences.append(float(confidence))
            class_ids.append(class_id) 

    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # Non-Maximum Suppression

    if len(idxs) > 0: # 결과값이 존재한다면 실행
        for i in idxs.flatten(): # 1차원으로 결과 펴주기
            x, y, w, h = boxes[i]
            
            pts1 = np.array([[x1,y1], [x2,y2], [x3,y3],[x4,y4]], dtype=np.int32) # 사용자 눈에 보이는 polygon 생성을 위한 좌표 지정
            polyList = [(x1,y1),(x2,y2),(x3,y3),(x4,y4)] # 기계 연산에 사용할 polygon 생성을 위한 좌표 지정
            polygon = Polygon(polyList) # Polygon 함수를 이용해 제한 구역 지정
            
            print('')
            cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=1) # 모든 객체에 사각형 그리기
            cv2.putText(img, text='%s %.2f %d' % (LABELS[class_ids[i]], confidences[i], w), org=(x, y - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=2) # 모든 객체 상단에 객체의 종류, 정확도, 폭 그리기
            cv2.polylines(img, [pts1], True, (0,0,255), thickness=2) # 사용자 눈에 보이는 polygon 그리기
            cv2.putText(img, text='Restricted Area', org=(x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 0, 255), thickness=2) # 'Restricted Area' 문자 그리기
            
            if class_ids[i] == 0: # class_id 가 0이면 (Person 이면) 실행
                print(x+(1/2*w),y+(1/2*h)) # Person 객체의 중심 좌표를 터미널에 출력하기
                Result = polygon.contains(Point(x+(1/2*w),y+(1/2*h))) # Person 객체가 제한 구역에 진입하면 'True'값 반환
                print(Result)
                if Result == True : # 'True'값이 반환된다면 실행
                    print('작업자가 제한 구역 안에 들어와 있습니다')
                    cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2) # 제한 구역에 접근한 객체를 밝은 초록색(0,255,0)으로 마킹하기
                    
    cv2.imshow('result', img)
    if cv2.waitKey(1) == ord('q'):
        break


