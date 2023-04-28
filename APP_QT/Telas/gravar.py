from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel, QLCDNumber
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
        
        self.label_msg = QLabel(self)
        self.label_msg.setText('Tempo Estimado: ')
        self.label_msg.resize(600,100)
        self.label_msg.move(20,30)
        self.label_msg.setStyleSheet('QLabel {font: 60px}')

        self.lcd_timer = QLCDNumber(self)
        self.lcd_timer.setDigitCount(5)
        self.lcd_timer.display("00:00")
        self.lcd_timer.resize(200, 50)
        self.lcd_timer.move(500, 60)
        self.lcd_timer.setStyleSheet('QLCDNumber {font: 60px}')
        
        """
        self.label_tempo = QLabel(self)
        self.label_tempo.setText('5')
        self.label_tempo.resize(600,100)
        self.label_tempo.move(600,30)
        self.label_tempo.setStyleSheet('QLabel {font: 60px}')
        """

        self.botao_iniciar = QPushButton('Iniciar', self)
        self.botao_iniciar.resize(600,100)
        self.botao_iniciar.move(100,200)
        self.botao_iniciar.setStyleSheet('QPushButton {font:80px; background-color: green}')


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
    tela = Tela_Gravar()
    sys.exit(aplicativo.exec_())
