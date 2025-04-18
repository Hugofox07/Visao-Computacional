import numpy as np
import cv2

# Criar uma imagem em branco (RGB) com tamanho 500x500 pixels
height, width = 500, 500
blank_image = np.zeros((height, width, 3), dtype=np.uint8)

# Exibir a imagem em uma janela
cv2.imshow("Imagem em Branco", blank_image)

# Aguardar uma tecla e fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
