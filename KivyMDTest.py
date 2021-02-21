from kivymd.app import MDApp
from kivy.lang import Builder



class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = "500"
        self.screen = Builder.load_file("main.kv")
        return self.screen
        
        
    def press(self):
        #print(self.screen.ids.input.text)
        #self.screen.ids.response.text = "Snorre snorre bruh"

    
    





MainApp().run()


