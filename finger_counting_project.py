import cv2
import time
import os
import hand_tracking_module as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0
folderPath = 'finger_images'
myList = os.listdir(folderPath)
overlayList = []
TotalFingers = 0

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)


    # 5 fingers
    if lmList != None:
        fingers = []
        for id in range(0, 5):
            if lmList[tipIds[id]][1] > lmList[tipIds[id]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
        TotalFingers = fingers.count(1)

    h, w, c = overlayList[TotalFingers].shape
    img[0:h, 0:w] = overlayList[TotalFingers]
    cv2.rectangle(img, (25, 390), (120, 455), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, str(TotalFingers), (50, 450), cv2.FONT_HERSHEY_PLAIN,
                5, (0, 0, 255), 10)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
    cv2.imshow('custom window', img)
    key = cv2.waitKey(1)
    if key > 0:
        break
    