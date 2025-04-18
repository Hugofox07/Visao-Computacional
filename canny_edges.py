import cv2 as cv 
import numpy as np

path = 'visao_computacional.png'
image = cv.imread(path)
cv.imshow('Original',image)

# Detectar bordas com Canny
gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow('Gray_Image', gray_image)

 # Detectar bordas com Canny alternar a imagem como blur, grayscale.
canny_image = cv.Canny(gray_image, 125,125)
cv.imshow('Canny_bordas', canny_image)

cv.waitKey(0)
cv.destroyAllWindows()