from pyautogui import locateOnScreen,moveTo,click,position,screenshot
from comparar_opencv import compara_img


def local_img(name_img='img/i.PNG'):
    img = locateOnScreen(name_img, confidence=0.5)
    
    return img

def local_tela(delay=2):
    if delay < 0 or delay > 10:
        return 'Va se tratar!', 'https://www.youtube.com/watch?v=mTqMxlBLAHM'
    else:

        import time
        time.sleep(delay)

        x,y = position()

        return x,y


def move_mouse(x,y):
    moveTo(x,y)

def click_mouse():
    click()

def save_axis(x,y):
    try:
        # Abrir o arquivo em modo de escrita
        arquivo = open('arquivo.txt', 'w')

        # Escrever a string no arquivo
        texto = f'{x},{y}'
        arquivo.write(texto)

        # Fechar o arquivo
        arquivo.close()

        return True
    
    except:
        return False

def load_axis(arquivo='arquivo.txt'):

    # Abrir o arquivo em modo de leitura
    arquivo = open(arquivo, 'r')

    # Ler o conteúdo do arquivo
    conteudo = arquivo.read()

    conteudo = conteudo.split(',')

    x = conteudo[0]
    y = conteudo[1]

    # Fechar o arquivo
    arquivo.close()

    return x,y

def see():
    import time

    while True:

        time.sleep(5)
        im1 = screenshot()
        im1.save('see/img1.png')

        time.sleep(5)
        im1 = screenshot()
        im1.save('see/img2.png')

        retorno = compara_img('see/img1.png','see/img2.png')

        if retorno:
            pass
        else:
            break

def localiza_img_tela(path):
    import time
    from PIL import Image

    # Carrega a imagem
    imagem = Image.open(path)

    # Obtém as dimensões da imagem
    largura, altura = imagem.size

    # Encontra a posição da imagem na tela
    posicao = None
    while posicao is None:
        posicao = locateOnScreen(path)
        time.sleep(1)

    # Obtém as coordenadas x e y do canto superior esquerdo da imagem
    x, y = posicao.left, posicao.top

    # Exibe as dimensões e a posição da imagem na tela
    return x,y,largura,altura




def msg_user():
    """
    Quando aceitar a fila, providenciar uma forma de notificar o usuário que a fila foi aceita e o mesmo deve voltar para o pc o mais rapido possivel
    sugestões:
        E-Mail
        Whatzapp
    """
    pass


if __name__ == '__main__':
    import time
    while True:
        localiza_img_tela('img/LC.PNG')
        time.sleep(1)
        #if 0xFF == ord('esc'):
        #    break


    """q=

    localizando botão na tela de forma eficiente


    local = local_img('img/full_button.JPG')
    print(local)
    move_mouse(local[0]+(local[2]/2),local[1]+(local[3]*0.50))
    """
    """
    Para localizar o botão de aceitar pelo layout geral o código abaixo é adequado.
    
    local = local_img('img/1.JPG')
    print(local)
    move_mouse(local[0]+(local[2]/2),local[1]+(local[3]*0.82))
    """