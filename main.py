import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)

while True:
    check, frame = video.read()
    cv2.imshow("Webcam Monitor Video", frame)
    #Creates a video stop key "q"
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
