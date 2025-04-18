import cv2 as cv 
import numpy as np 

width = 302
height = 287
path = 'visao_computacional.png'
img = cv.imread(path)
cv.imshow('Original', img)

resize_img = cv.resize(img,(width,height))
cv.imshow('Resize', resize_img)

cv.waitKey(0)
cv.destroyAllWindows()