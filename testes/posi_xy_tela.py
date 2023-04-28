import cv2
import numpy as np
import pyautogui

# Carrega a imagem que deseja procurar
template = cv2.imread('chrome.jpg', cv2.IMREAD_GRAYSCALE)

# Tira uma captura de tela da área desejada
screenshot = pyautogui.screenshot()

# Converte a captura de tela para uma matriz NumPy
screenshot = np.array(screenshot)

# Certifique-se de que ambos os tipos de dados estejam corretos
print('Tipo de dados da screenshot:', screenshot.dtype)
print('Tipo de dados do template:', template.dtype)

# Procura a imagem na captura de tela usando o método TM_SQDIFF_NORMED
result = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF_NORMED)

# Obtém a posição da imagem na captura de tela
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
x, y = min_loc

# Imprime a posição da imagem na tela
print('Posição da imagem: ({}, {})'.format(x, y))
