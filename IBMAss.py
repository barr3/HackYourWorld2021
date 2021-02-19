"""
Kivy application test

"""
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '900')
Config.set('graphics', 'resizable', False)
from kivy.uix.textinput import TextInput


class ButtonApp(App):
    def build(self):
        return Button()
        
    
    def on_press_button(self):
        print('You pressed the button!')
#Experimental                   
def on_enter(instance, value):
    print('User pressed enter in', instance)

    textinput = TextInput(text='Hello world', multiline=False)
    textinput.bind(on_text_validate=on_enter)

if __name__ == '__main__':
    app = ButtonApp()
    app.run()