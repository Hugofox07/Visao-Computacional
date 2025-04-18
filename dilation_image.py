import cv2 as cv 
import numpy as np

#Use the kernel
kernel = np.ones((5,5),np.uint8)
print(kernel)

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)

# Using method Canny Edges
img_canny = cv.Canny(img, 25, 25) # Alternar a imagem como blur, grayscale.
cv.imshow('Canny_Image', img_canny)

# Using method Dilation image
img_dilated = cv.dilate(img_canny,kernel, iterations=1)# Alternar a imagem como blur, grayscale.

cv.imshow('Dilate_Image', img_dilated)
cv.waitKey(0)
cv.destroyAllWindows()