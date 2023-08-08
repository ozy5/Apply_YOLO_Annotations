import cv2
from ultralytics import YOLO
import torch

#capture video from webcam in gray scale




cap = cv2.VideoCapture(0)

out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 30.0, (640,480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #set frame to (640,480)
    frame = cv2.resize(frame, (640,480))

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    cv2.imshow('webcam', frame)

    out.write(frame)



    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()

