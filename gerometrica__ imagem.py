import cv2 as cv 
import numpy as np

# Color
green = (0, 255, 0)
blue = (255, 0, 0)
red = (0, 0, 255)
yellow = (0, 255, 255)
white = (255, 255, 255)
# height,width
width = 800
height = 800
#blank image numpy
blank_image = np.zeros([height,width, 3], dtype=np.uint8)

circle = cv.circle(blank_image, (447,63), 63, blue, 3)#-1
rectangle_image = cv.rectangle(blank_image,(0,0),(110,120),red,3)#-1
line_image = cv.line(blank_image,(0,0),(310,210,),green,3)
arrowedLine = cv.arrowedLine(blank_image, (0, 255), (255, 255), yellow, 3)#-1

cv.imshow('Blank', blank_image)
cv.waitKey(0)
cv.destroyAllWindows()