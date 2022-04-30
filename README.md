# Construction_safety
Object detection for construction safety, using YOLOv3, OpenCV

Restricted Area
-------------
#### 배경   
건설산업 재해의 비중이 타 산업보다 크다. (*한국산업안전보건공단, 2022) 이로써 산업 안전에 대한 요구가 커지고 있지만 현장 규모에 적절하지 않은 소수의 안전관리자가 다수의 노동자를 관리하고 있는 실정이다. 모든 사람을 모니터링하기에는 업무 과다 등의 이유로 인적 자원의 한계가 있기 때문이다. (**한상우, 2022)
   
**2021년 산업재해 발생현황 . (2022). https://www.kosha.or.kr/kosha/index.do.*   
***한상우. (2022). 건설현장 안전관리자의 직무수행시 문제점에 관한 연구 : 건축공사를 중심으로(공학석사). 서울과학기술대학교 산업대학원*
   
#### 설명
관리자가 설정한 제한 구역에 작업자가 진입했을 시, 위험 알림을 터미널에 보내주는 코드를 제작했다. 하인리히(Heinrich, 1931)는 사소한 것이 큰 사고를 야기한다고 말했다. 그 '사소한 것'이란 '가지 말라는 곳을 굳이 지나가는 것'이라고 생각하는데, 이를 '불안전 행동'으로 본다. 건설 현장은 넓은 공간에서 생산조직이 이동하는 특성이 있다. 따라서 작업팀이 다른 구역으로 이동할 때 지름길로 가려는 경향을 보인다. 그러나 이동 동선에 잠재 위험(낙하물 발생 위험 구간, 중장비 작업 반경 등)이 있을 수 있기에 관리자가 위험 구역을 지정하여 작업팀이 접근하는 것을 예방한다. 이는 아침 교육(aka. TBM - '전날 몇 명이 제한 구역을 지나갔습니다. 주의 바랍니다.') 등에 활용할 수 있다.
   
이 코드를 오픈 소스로 공유합니다. MIT라이선스에 따라 누구나 제한 없이 본 코드의 취급이 가능합니다.   
Copyright (c) 2022 YUNJUNGCHAN
   

   
![Result2](https://user-images.githubusercontent.com/101917321/166079890-9b882dfb-f2d9-4d1f-a11e-bb0547bfcdac.gif)
   
#### 동작 순서   
1. 사전에 사용자가 제한 구역을 설정(Polygon 좌표 지정)   
2. 사람 객체(Person)가 제한 구역 안에 진입했을 시 밝은 초록색(0, 255, 0) 박스로 강조   
3. 터미널에 '작업자가 제한 구역 안에 들어와 있습니다' 알림   
   
#### 환경 (*는 필수, **는 자동으로 설치됨)   
1. *Linux 우분투 20.04 LTS (Linux Ubuntu 20.04 LTS)   
2. **Python 3.8.6
3. *CMake 2.23.1   
4. *OpenCV 4.5.5   
5. *Git
6. Nvidia graphic driver 470.103.01   
7. Nvidia CUDA toolkit 11.3   
8. Nvidia CUDA Deep Neural Network library(cuDNN) 8.4.0    
9. *AlexeyAB Darknet(YOLOv3) https://github.com/AlexeyAB/darknet
10. Visual Studio Code, Vim   
   
#### 라이브러리
1. OpenCV
2. Numpy, Pandas
3. Shapely
   
#### 실행하기 전에   
1. Line 27 : a) 'yolov3.cfg', b) 'yolov3.weights'를 코드에 연결해야 합니다. a)는 AlexeyAB의 Darknet를 컴파일(make)하면 생성될 것이고, b)는 https://pjreddie.com/media/files/yolov3.weights 에서 받으실 수 있습니다.   
2. 주석으로 코드 설명과 정성을 담았습니다.   
   
#### 실행    
에디터(eg. VS Code) 또는, 기본 터미널에서 다음 명령어로 실행하실 수 있습니다.   

    $ python3 ./Restricted_Area.py
   
#### 사용    
건설현장 Sample 파일로 altoy bokoy님의 유튜브 영상(https://youtu.be/3U6n5oHqLOY)을 사용합니다.   
사전에 정의한 Restricted Area 에 Person 객체가 진입하면 밝은 초록색(0, 255, 0) 박스를 생성하고, 터미널에 다음을 출력합니다.
   
    작업자가 제한 구역 안에 들어와 있습니다
   
#### 종료   
'q'를 누르시면 코드가 Break 되어 종료됩니다.   
   
    q   
   
#### References
   1. https://github.com/kairess/ANPR-with-Yolov4.git   
   2. https://github.com/AlexeyAB/darknet   
   3. https://youtu.be/3U6n5oHqLOY   
   4. https://youtu.be/mmFrZV1iH0c   
   5. 2021년 산업재해 발생현황 . (2022). https://www.kosha.or.kr/kosha/index.do.   
   6. 한상우. (2022). 건설현장 안전관리자의 직무수행시 문제점에 관한 연구 : 건축공사를 중심으로(공학석사). 서울과학기술대학교 산업대학원
    
