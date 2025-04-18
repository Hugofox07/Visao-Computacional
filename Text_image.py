import cv2 as cv 
import numpy as np

path = 'Save_Image/apple.png'
white = (255, 255, 255)
frase = 'OpenCV e divertido'
img = cv.imread(path)

# Put text in image
font = cv.FONT_HERSHEY_SIMPLEX
line_type = cv.LINE_AA
text = cv.putText(img,frase, (100,100), font, 1, white, 3, line_type)

cv.imshow('Original', img)
cv.waitKey(0)
cv.destroyAllWindows()