import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MeuApp(App):
    def build(self):
        layout = GridLayout(cols=1, rows=2)

        botao_ligar = Button(text="Ligar", background_color="green")
        botao_ligar.bind(on_press=self.on_button_ligar_click)
        layout.add_widget(botao_ligar)

        botao_desligar = Button(text="Desligar",background_color="red")
        botao_desligar.bind(on_press=self.on_button_desligar_click)
        layout.add_widget(botao_desligar)

        return layout

    def on_button_ligar_click(self, instance):
        print("Imagine que o programa ligou")

    def on_button_desligar_click(self, instance):
        print("Imagine que o programa desligou")

if __name__ == '__main__':
    MeuApp().run()
