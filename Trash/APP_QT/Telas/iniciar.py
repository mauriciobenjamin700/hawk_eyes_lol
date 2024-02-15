from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel

class Tela_Iniciar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.esquerda = 500
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Tela Geral'

        
        self.label_msg = QLabel(self)
        self.label_msg.setText('Tempo Ligado: ')
        self.label_msg.resize(600,100)
        self.label_msg.move(100,30)
        self.label_msg.setStyleSheet('QLabel {font: 60px}')
        
        self.label_tempo = QLabel(self)
        self.label_tempo.setText('0s')
        self.label_tempo.resize(600,100)
        self.label_tempo.move(600,30)
        self.label_tempo.setStyleSheet('QLabel {font: 60px}')

        self.botao_parar = QPushButton('Parar', self)
        self.botao_parar.resize(600,100)
        self.botao_parar.move(100,200)
        self.botao_parar.setStyleSheet('QPushButton {font:80px; background-color: red}')


        self.botao_voltar = QPushButton('Voltar', self)
        self.botao_voltar.resize(600,100)
        self.botao_voltar.move(100,370)
        self.botao_voltar.setStyleSheet('QPushButton {font:60px}')


        self.Criar_Tela()

    def Criar_Tela(self):

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        #para visualizar descomente a linha a baixo
        #self.show()


if __name__ == '__main__':
    
    
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_Iniciar()
    sys.exit(aplicativo.exec_())
