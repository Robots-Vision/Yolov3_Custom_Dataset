from cv2 import cv2


cap = cv2.VideoCapture("rtsp://admin:Sena14232518@192.168.0.105:554/cam/realmonitor?channel=1&subtype=1")

while True: 
    _, frame = cap.read()

    cv2.imshow("image", frame)
    if ord("q") == cv2.waitKey(1):
        break