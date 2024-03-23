import cv2
import os

file_name_in = "hunting rifle_28.jpeg"
image_path = os.path.join('.','images',f'{file_name_in}')

img = cv2.imread(image_path)

# file_name_out = ''
# cv2.imwrite(os.path.join('.','images',f'{file_name_out}'),img)

#visualize image

cv2.imshow("Output",img)
cv2.waitKey(0)