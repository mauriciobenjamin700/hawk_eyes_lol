from pyautogui import locateOnScreen,moveTo,click,screenshot

def local_img(name_img):
    location = locateOnScreen(name_img)
    
    return location

def move_mouse(x,y):
    moveTo(x,y)

def click_mouse():
    click()


if __name__ == '__main__':
    
    im1 = screenshot()
    im1.save('my_screenshot.png')

    
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