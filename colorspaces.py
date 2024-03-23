import cv2
import os

img = cv2.imread(os.path.join('.','images\cat.webp'))

# cv2.imshow('img',img)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window', img_rgb)
cv2.resizeWindow('custom window', 500, 500)
cv2.waitKey(0)

