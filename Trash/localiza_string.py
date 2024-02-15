import pyautogui
import pytesseract
from PIL import ImageGrab

# Define a string que será procurada na tela
texto_procurado = "Aceitar"

# Faz uma captura de tela da região onde se espera encontrar a string
imagem_tela = ImageGrab.grab()

# Converte a imagem para escala de cinza
imagem_cinza = imagem_tela.convert("L")

# Realiza a OCR na imagem para obter o texto encontrado
texto_encontrado = pytesseract.image_to_string(imagem_cinza)

# Localiza o índice do início da string na OCR realizada
indice_inicio = texto_encontrado.find(texto_procurado)

# Verifica se a string foi encontrada na tela
if indice_inicio != -1:
    # Obtém as coordenadas do centro da região onde a string foi encontrada
    regiao = (indice_inicio, 0, indice_inicio + len(texto_procurado), imagem_tela.height)
    x, y, largura, altura = pyautogui.center(pyautogui.locateOnScreen(imagem_tela.crop(regiao)))
    
    # Move o mouse para as coordenadas encontradas
    pyautogui.moveTo(x, y)
else:
    print("String não encontrada na tela")
