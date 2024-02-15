from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLCDNumber
from PyQt5.QtCore import QTimer

class Tela_Gravar(QMainWindow):

    def __init__(self):
        super().__init__()

        self.esquerda = 500
        self.topo = 100
        self.largura = 800
        self.altura = 600
        self.titulo = 'Tela Geral'

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizar_timer)

        self.lcd_timer = QLCDNumber(self)
        self.lcd_timer.setDigitCount(5)
        self.lcd_timer.display("00:00")
        self.lcd_timer.resize(600, 100)
        self.lcd_timer.move(100, 100)
        self.lcd_timer.setStyleSheet('QLCDNumber {font: 60px}')

        self.botao_iniciar = QPushButton('Iniciar', self)
        self.botao_iniciar.resize(600, 100)
        self.botao_iniciar.move(100, 250)
        self.botao_iniciar.setStyleSheet('QPushButton {font:80px; background-color: green}')
        self.botao_iniciar.clicked.connect(self.iniciar_timer)

        self.botao_voltar = QPushButton('Voltar', self)
        self.botao_voltar.resize(600, 100)
        self.botao_voltar.move(100, 400)
        self.botao_voltar.setStyleSheet('QPushButton {font:60px}')

        self.Criar_Tela()

    def Criar_Tela(self):

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)

    def iniciar_timer(self):
        self.timer.start(1000)

    def atualizar_timer(self):
        segundos = self.lcd_timer.value() + 1
        minutos = segundos // 60
        segundos = segundos % 60
        text = f"{minutos:02d}:{segundos:02d}"
        self.lcd_timer.display(text)

if __name__ == '__main__':
    import sys
    aplicativo = QApplication(sys.argv)
    tela = Tela_Gravar()
    tela.show()
    sys.exit(aplicativo.exec_())
