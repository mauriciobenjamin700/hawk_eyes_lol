import pyautogui
from PIL import Image, ImageChops

# Captura uma imagem da tela
im1 = pyautogui.screenshot()

# Carrega outra imagem
im2 = Image.open('imagem2.png')

# Compara as imagens
diff = ImageChops.difference(im1, im2)

# Se as imagens forem iguais, diff.getbbox() retorna None
if diff.getbbox():
    print('As imagens são diferentes')
else:
    print('As imagens são iguais')
