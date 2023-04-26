from pyautogui import locateOnScreen,moveTo,click,position,screenshot
from comparar_opencv import compara_img

def local_img(name_img):
    location = locateOnScreen(name_img)
    
    return location

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


if __name__ == '__main__':
    see()
    


    """

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