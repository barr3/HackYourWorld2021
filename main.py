import GetData as d
import SendData as s
import User as u
import Chart
import numpy as np
import matplotlib.pyplot as plt

from kivymd.app import MDApp
from kivy.lang import Builder


from kivy.config import Config
Config.set('graphics', 'width', '370')
Config.set('graphics', 'height', '600')
Config.write()


#This class runs the GUI, main.kv is where all the widgets are added
#MainApp
class MainApp(MDApp):

    clickable = True
    trans = False
    #This function gets called when the user presses one of the mat/transport-buttons
    def change_mode(self, press):
        #This variable is used to decide which database to get data from
        mode = press
        self.mode = mode
        if self.mode == "transport":
            self.screen.ids.input.hint_text = "Jag har åkt bil, buss, flyg et.c"

        else:
            self.screen.ids.input.hint_text = "Jag har ätit:"

        self.screen.ids.translabel.text = ""


    def update(self):
        Chart.piechart()
        self.screen.ids.img.source = ""
        self.screen.ids.img.reload()
        self.screen.ids.img.source = "piechart.png"
        self.screen.ids.img.reload()
        print(self.screen.ids.img)

        print("reload")

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "500"
        self.screen = Builder.load_file("hack.kv")
        self.mat_press()
        return self.screen


    def mat_press(self):
        if self.clickable == True:

            self.change_mode("mat")
        #self.screen.ids.mat.md_bg_color
            self.screen.ids.matknapp.md_bg_color = [.4,.4,.4,1]
            self.screen.ids.transknapp.md_bg_color = [1,1,1,1]
            self.screen.ids.input.hint_text = "Jag har ätit:"

    def trans_press(self):
        if self.clickable == True:


            self.change_mode("transport")
            self.screen.ids.transknapp.md_bg_color = [.4,.4,.4,1]
            self.screen.ids.matknapp.md_bg_color = [1,1,1,1]
            self.screen.ids.input.hint_text = "Jag har åkt bil, buss, flyg et.c"

        #This function takes the value of what is put in the textfield in the gui
        #and sends it to the assistan using run_conversation

    def trans_sträcka(self):


        self.clickable = False
        self.screen.ids.translabel.text = "Hur många kilometer har du åkt?"
        self.screen.ids.input.hint_text = "Hur många kilometer?"
        #text = self.screen.ids.input.text
        if self.trans == True:
            text = self.screen.ids.input.text




            try:
                text = int(text)
                return self.screen.ids.input.text
            except ValueError:
                is_int = False
                self.screen.ids.input.hint_text = "Vänligen skriv en siffra"



        else:
            pass


        self.trans = True



    def send_transport(self, intent, data):

        intent = get_intent(intent)

        print("intenten är:" ,intent)
        print("sträckan är:", data)


    def send_food(self, intent):

        intent = get_intent(intent)

        temp_val = d.GetItem.get_food(intent)

        #print(intent)
        #print(temp_val)
        #s.sendCo2(temp_val, "food")

    def reset(self):
        self.change_mode(self.mode)

    input = True
    transport = None
    def press(self):
        #input = self.screen.ids.input.text
        #self.screen.ids.response.text = run_conversation(input)

        if self.mode == "transport":

            if self.screen.ids.input.text != "" :

                if self.input == True:

                    self.transport = self.screen.ids.input.text
                    self.input = False


                sträcka = self.trans_sträcka()
                if sträcka == None:
                    sträcka = self.trans_sträcka()
                else:
                    self.clickable = True
                    self.input = True
                    self.send_transport(self.transport, sträcka)
                    self.reset()

        if self.mode == "mat":
            mat = self.screen.ids.input.text
            self.send_food(mat)


        #Clears the
        self.screen.ids.input.text = ""



def get_intent(input):
    response = u.run_conversation(input)
    return response




MainApp().run()
