from re import X
import cv2
import numpy as np

CONFIDENCE = 0.5
THRESHOLD = 0.3
LABELS = ['Person','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','Cell Phone','','','','','','','','','','','','','','','','','']

cap = cv2.imread('./data/site.png')
cv2.imshow('result', cap)

cv2.waitKey(1) == ord('q')
