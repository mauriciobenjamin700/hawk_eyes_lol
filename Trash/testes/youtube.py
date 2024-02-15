"""
Como fazer o Python localizar imagem e clicar em cima (três níveis de dificuldade)
https://www.youtube.com/watch?v=cNwYx-PDlgM&ab_channel=DanteDerette
"""
import pyautogui
import time

procurar = True

while procurar:

    img = pyautogui.locateOnScreen('ai.PNG', confidence=0.5)

    if img == None:
        time.sleep(1)
        print('não encontrei')

    else:
        print('Encontrei')
        #print(img[0])
        #print(type(img))
        pyautogui.moveTo(img[0],img[1])
        time.sleep(1)
      




