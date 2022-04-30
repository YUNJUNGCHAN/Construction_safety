# Construction_safety
Object detection for construction safety, using YOLOv3, OpenCV

Restricted Area
-------------
#### 배경   
건설산업 재해의 비중이 타 산업보다 크다. (*한국산업안전보건공단, 2022) 이로써 산업 안전에 대한 요구가 커지고 있지만 현장 규모에 적절하지 않은 소수의 안전관리자가 다수의 노동자를 관리하고 있는 실정이다. 모든 사람을 모니터링하기에는 업무 과다 등의 이유로 인적 자원의 한계가 있기 때문이다. (**한상우, 2022)
   
**2021년 산업재해 발생현황 . (2022). https://www.kosha.or.kr/kosha/index.do.*   
***한상우. (2022). 건설현장 안전관리자의 직무수행시 문제점에 관한 연구 : 건축공사를 중심으로(공학석사). 서울과학기술대학교 산업대학원*
   
#### 설명
제한 구역에 작업자가 진입했을 시, 터미널에 알림을 보내주는 코드를 제작했다. 이는 아침 교육(aka. TBM - '전날 몇 명이 제한 구역을 지나갔습니다. 주의 바랍니다.') 등에 활용할 수 있어 보인다. 한술 더 뜨자면 생산성 분석에도 쓸 수 있지 않을까 조심스레 생각해 본다.   
   
**나는 실패했다. 어렵더라.*
   
이 코드를 오픈 소스로 공유합니다. MIT라이선스에 따라 누구나 제한 없이 본 코드의 취급이 가능합니다.   
Copyright (c) 2022 YUNJUNGCHAN
   

   
![Result2](https://user-images.githubusercontent.com/101917321/166079890-9b882dfb-f2d9-4d1f-a11e-bb0547bfcdac.gif)
   
#### 동작 순서   
1. 사용자가 제한 구역을 지정(Polygon 좌표 지정)   
2. 사람(Person)이 제한 구역 안에 들어왔을 때, 초록색 박스로 강조   
3. 터미널에 알림   
   
#### 환경 (*는 필수)   
1. *Linux 우분투 20.04 LTS (Linux Ubuntu 20.04 LTS)   
2. *CMake 2.23.1   
3. *OpenCV 4.5.5   
4. *Git
5. Nvidia graphic driver 470.103.01   
6. Nvidia CUDA toolkit 11.3   
7. Nvidia CUDA Deep Neural Network library(cuDNN) 8.4.0    
8. *AlexeyAB Darknet(YOLOv3) https://github.com/AlexeyAB/darknet
9. Visual Studio Code, Vim   
   
#### 라이브러리
1. Opencv
2. Numpy, Pandas
3. Shapely
   
#### 실행하기 전에   
1. Line 27 : a) 'yolov3.cfg', b) 'yolov3.weights'를 코드에 연결해야 합니다. a)는 AlexeyAB의 Darknet를 컴파일(make)하면 생성될 것이고, b)는 https://pjreddie.com/media/files/yolov3.weights 에서 받으실 수 있습니다.   
2. 주석으로 코드 설명을 정성과 함께 담았습니다.   
   
#### 실행    
에디터(eg. VS Code) 또는, 기본 터미널에서 다음 명령어로 실행하실 수 있습니다.   

    $ python3 ./Restricted_Area.py
   
   
