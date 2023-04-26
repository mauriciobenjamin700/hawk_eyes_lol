import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from func import *
import pyautogui



class MeuApp(App):
    def build(self):
        layout = GridLayout(cols=1, rows=4)
        
        botao_ligar = Button(text="Ligar", background_color="green")
        botao_ligar.bind(on_press=self.on_button_ligar_click)
        layout.add_widget(botao_ligar)

        botao_desligar = Button(text="Desligar",background_color="red")
        botao_desligar.bind(on_press=self.on_button_desligar_click)
        layout.add_widget(botao_desligar)

        botao_gravar = Button(text="Gravar",background_color="grey")
        botao_gravar.bind(on_press=self.on_button_gravar_click)
        layout.add_widget(botao_gravar)

        botao_modificar = Button(text="Modificar",background_color="grey")
        botao_modificar.bind(on_press=self.on_button_modificar_click)
        layout.add_widget(botao_modificar)
        return layout
    
    

    def on_button_ligar_click(self, instance):
        see()
        move_mouse(load_axis())
        click_mouse()

    def on_button_desligar_click(self, instance):
        print("Imagine que o programa desligou")
    
    def on_button_gravar_click(self, instance):
        print("Imagine que o programa")
    
    def on_button_modificar_click(self, instance):
        print("Imagine que o programa modificar")
    
    

if __name__ == '__main__':
    MeuApp().run()
