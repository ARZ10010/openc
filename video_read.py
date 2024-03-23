import cv2
import os

file_name = ''

video_path = os.path.join('.','video',f'{file_name}')
video = cv2.VideoCapture(video_path)
ret  = True

while ret:
    ret,frame = video.read()

    if ret:
        cv2.imshow('frames',frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()