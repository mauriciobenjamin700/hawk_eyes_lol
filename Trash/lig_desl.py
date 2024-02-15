from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from func import *

class MeuApp(App):
    def build(self):
        layout = GridLayout(cols=1, rows=4)
        
        botao_ligar = Button(text="Ligar", background_color="green")
        botao_ligar.bind(on_press=self.on_button_ligar_click)
        layout.add_widget(botao_ligar)

        botao_desligar = Button(text="Desligar",background_color="red")
        botao_desligar.bind(on_press=self.on_button_desligar_click)
        layout.add_widget(botao_desligar)

        botao_gravar = Button(text="Gravar",background_color="orange")
        botao_gravar.bind(on_press=self.on_button_gravar_click)
        layout.add_widget(botao_gravar)

        botao_modificar = Button(text="Modificar",background_color="purple")
        botao_modificar.bind(on_press=self.on_button_modificar_click)
        layout.add_widget(botao_modificar)
        return layout
    
    def on_button_ligar_click(self):
        """
        desenvolver uma tela com um contador de tempo subindo e um uma mensagem escrita "Estou vigiando a fila por você durante " em baixo disso o tempo que o bot ficou ligado
        quando o mesmo terminar o serviço, os textos mudam para "aceitei a fila por você" "trabalhei por XX tempo'
        """
        see()
        x,y = load_axis()
        move_mouse(x,y)
        click_mouse()

    def on_button_desligar_click(self, instance):
        print("Imagine que o programa desligou")
    
    def on_button_gravar_click(self, instance):
        """
        desenvolver uma tela com uma label contador, que inicia com o tempo do delay (padrão 2 segundos) e vai diminuindo até 0
        quando a label chegar a 0, troca o texto por "Posição do Mouse gravada com sucesso"
        aguarda alguns segunds (tempo exato precisa ser definido) e volta para a tela anterior
        """
        x,y = local_tela(delay=5)
        if save_axis(x,y):
            print('Eixos salvos com sucesso!')
        else:
            print('Falha ao salvar os eixos')
    
    def on_button_modificar_click(self, instance):
        """
        desenvolver uma tela com caixas de texto, onde o usuário pode definir o daley de reação da aplicação
        """
        print("Imagine que o programa modificar")
    
    

if __name__ == '__main__':
    MeuApp().run()
