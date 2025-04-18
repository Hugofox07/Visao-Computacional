# Objetivo: Carregar uma imagem e exibi-la em uma janela.
import cv2 as cv
import numpy as np

path = ('visao_computacional.png')
img = cv.imread(path)

cv.imshow('Exercicios1', img)
cv.waitKey(0)
cv.destroyAllWindows()