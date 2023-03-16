import numpy as np
import cv2 as cv

cap = cv.VideoCapture("rtsp://admin:Niepcesnir21@10.171.20.39:554")

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
print(cap.get(cv.CAP_PROP_FPS))

out = cv.VideoWriter('video99.avi', fourcc, 24.0, (int(cap.get(3)), int(cap.get(4))))

print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
while cap.isOpened():

    ret, frame = cap.read()
    if ret == True:

        out.write(frame)
        cv.imshow('cam', frame)
        time = cap.get(cv.CAP_PROP_POS_MSEC) / 1000
        print(time)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
