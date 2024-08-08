import cv2
import numpy as np

image=cv2.imread('image.jpg')

if image is None:
    print("could not read the image")
    exit()

cv2.imshow('orginal image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


grey_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grey image',grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()