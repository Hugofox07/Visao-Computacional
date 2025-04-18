import cv2 as cv 
import numpy as np 

path = 'imagem/apple.jpg'
img = cv.imread(path)

cv.imshow('Original_image', img)
cv.imwrite('Save_Image/apple.png', img)
cv.waitKey(0)
cv.destroyAllWindows()