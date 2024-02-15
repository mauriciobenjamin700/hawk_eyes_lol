from Telas.geral import Tela_Geral
from Telas.gravar import Tela_Gravar
from Telas.iniciar import Tela_Iniciar
from func import *
from comparar_opencv import compara_img
from PyQt5.QtWidgets import QApplication

class Gerenciador():
    def __init__(self):
        self.tela_geral = Tela_Geral()
        self.tela_gravar = Tela_Gravar()
        self.tela_iniciar = Tela_Iniciar()

        self.tela_geral.show()

        #interligando os botões com as telas
        self.tela_geral.botao_gravar.clicked.connect(self.geral2gravar)
        self.tela_geral.botao_iniciar.clicked.connect(self.geral2iniciar)

        self.tela_gravar.botao_voltar.clicked.connect(self.gravar2geral)
        self.tela_iniciar.botao_voltar.clicked.connect(self.iniciar2geral)

        self.tela_iniciar.botao_parar.clicked.connect(self.desligar_bot)

    ###########################################################
    def geral2gravar(self):
        self.tela_gravar.show()
        self.tela_geral.close()

        self.tela_gravar.botao_iniciar.clicked.connect(self.iniciando_gravacao)
    
    def geral2iniciar(self):
        self.tela_iniciar.show()
        self.tela_geral.close()

        
        self.ligar_bot(True)

    def gravar2geral(self):
        self.tela_geral.show()
        self.tela_gravar.close()

    
    def iniciar2geral(self):
        self.tela_geral.show()
        self.tela_iniciar.close()

    #################################################

    def iniciando_gravacao(self):
        self.tela_gravar.timer.start(1000)
    def atualizar_timer(self):
        segundos = self.lcd_timer.value() + 1
        minutos = segundos // 60
        segundos = segundos % 60
        text = f"{minutos:02d}:{segundos:02d}"
        self.tela_gravar.lcd_timer.display(text)

    def ligar_bot(self, sinal):
            import time
            time.sleep(1)
            local = local_img('img/full_button.JPG')

            while True:
                if sinal:
                    if local == None:
                        print('Não Achei')
                        local = local_img('img/full_button.JPG')
                    else:
                        print('achei')
                        move_mouse(local[0]+(local[2]/2),local[1]+(local[3]*0.50))
                        click_mouse()
                        break

                else:
                    break

    def desligar_bot(self):
        self.ligar_bot(False)
            



if __name__ == '__main__':
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Gerenciador()
    sys.exit(aplicativo.exec_())