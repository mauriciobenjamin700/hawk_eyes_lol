import cv2

# Carrega as imagens
img1 = cv2.imread('imagem1.png')
img2 = cv2.imread('imagem2.png')

# Converte as imagens para escala de cinza
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Encontra a correspondência entre as imagens usando a função matchTemplate
result = cv2.matchTemplate(gray1, gray2, cv2.TM_CCOEFF_NORMED)

# Determina a similaridade entre as imagens a partir do valor máximo do mapa de correspondência
max_similarity = cv2.minMaxLoc(result)[1]

# Verifica se as imagens são semelhantes o suficiente
if max_similarity > 0.95:
    print('As imagens são semelhantes')
else:
    print('As imagens são diferentes')
