import cv2

def compara_img(path_img1,path_img2):
    # Carrega as imagens
    img1 = cv2.imread(path_img1)
    img2 = cv2.imread(path_img2)

    # Redimensiona a imagem modelo para que ela tenha o mesmo tamanho da imagem de referência
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Converte as imagens para escala de cinza
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2_resized, cv2.COLOR_BGR2GRAY)

    # Encontra a correspondência entre as imagens usando a função matchTemplate
    result = cv2.matchTemplate(gray1, gray2, cv2.TM_CCOEFF_NORMED)

    # Determina a similaridade entre as imagens a partir do valor máximo do mapa de correspondência
    max_similarity = cv2.minMaxLoc(result)[1]

    # Verifica se as imagens são semelhantes o suficiente
    if max_similarity > 0.90:
        return True
    else:
        return False
