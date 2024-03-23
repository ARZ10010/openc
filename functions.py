import os
import cv2

img = cv2.imread(os.path.join('.','images\cat2.jpg'))
cv2.imshow('img',img)
print(img.shape)
cv2.namedWindow('custom window', cv2.WINDOW_KEEPRATIO)
cv2.imshow('custom window', img)
cv2.resizeWindow('custom window', 500, 500)
#resize
# resized_img = cv2.resize(img,(1280,350))
# print(resized_img.shape)
# cv2.imshow('img',resized_img)

#crop
# cropped_img = img[360:730,1300:1800] #[height:width]
# cv2.imshow('img',cropped_img)

#
cv2.waitKey(0)