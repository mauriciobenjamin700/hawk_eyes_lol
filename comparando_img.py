from PIL import Image, ImageChops

def compara_img(img1,img2):
    # Captura uma imagem da tela
    im1 = Image.open(img1)

    # Carrega outra imagem
    im2 = Image.open(img2)

    # Compara as imagens
    diff = ImageChops.difference(im1, im2)

    # Se as imagens forem iguais, diff.getbbox() retorna None
    if diff.getbbox():
        return True
    else:
        return False
    
if __name__ == '__main__':
    if compara_img('img/c1.PNG','img/c2.PNG'):
        print('parece')
    else:
        print('não parece')