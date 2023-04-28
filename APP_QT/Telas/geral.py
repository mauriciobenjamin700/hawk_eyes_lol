from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton#,QLabel

class Tela_Geral(QMainWindow):

    def __init__(self):
        super().__init__()

        self.esquerda = 500
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Tela Geral'

        """
        self.label_msg = QLabel(self)
        self.label_msg.setText('BEM VINDO(A)  ')
        self.label_msg.resize(600,100)
        self.label_msg.move(480,0)
        self.label_msg.setStyleSheet('QLabel {font: 40px}')
        """


        self.botao_iniciar = QPushButton('Iniciar', self)
        self.botao_iniciar.resize(600,100)
        self.botao_iniciar.move(100,30)
        self.botao_iniciar.setStyleSheet('QPushButton {font:80px}')

        self.botao_gravar = QPushButton('Gravar', self)
        self.botao_gravar.resize(600,100)
        self.botao_gravar.move(100,200)
        self.botao_gravar.setStyleSheet('QPushButton {font:80px}')

        self.botao_modificar = QPushButton('Modificar parâmetros', self)
        self.botao_modificar.resize(600,100)
        self.botao_modificar.move(100,370)
        self.botao_modificar.setStyleSheet('QPushButton {font:60px}')


        self.Criar_Tela()

    def Criar_Tela(self):

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        #para visualizar descomente a linha a baixo
        #self.show()


if __name__ == '__main__':
    
    
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_Geral()
    sys.exit(aplicativo.exec_())
