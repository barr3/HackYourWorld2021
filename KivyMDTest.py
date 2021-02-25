from kivymd.app import MDApp
from kivy.lang import Builder

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Sets API Key
authenticator = IAMAuthenticator('Paa0LICW2gszbzgDQX_83y5td9ggmRiv0H2RvA88uG0w')

#Inits assistant
assistant = AssistantV2(
    version='2020-09-24',
    authenticator=authenticator
)
assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')

sesh_id = assistant.create_session(
        assistant_id='6bc3d805-70f6-4f71-9ee0-def44227ed12'
    ).get_result()

#Sets py_sesh_id to the session id
py_sesh_id = sesh_id['session_id']


#######################################

#This function takes the input "input" and sends it to the assistant.
#The function returns the response that the assistant gives. 
def run_conversation(input):
    user_input = input
    
    response = assistant.message(
        assistant_id='6bc3d805-70f6-4f71-9ee0-def44227ed12',
        session_id=py_sesh_id,
        input={
            'message_type': 'text',
            'text': user_input
        }
    ).get_result()

    #Really messy and ugly code. Could probaly be cleaned up but it works
    output = response['output']
    generic = output['generic']
    generic_list = generic[0]
    bot_output = generic_list['text']
    #print(bot_output) 
    return bot_output






#This class runs the GUI, main.kv is where all the widgets are added
#MainApp
class MainApp(MDApp):


    #This function gets called when the user presses one of the mat/transport-buttons
    def change_mode(self, press):
        #This variable is used to decide which database to get data from
        mode = press
        self.mode = mode


    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = "500"
        self.screen = Builder.load_file("hack.kv")
        self.mat_press()
        return self.screen


    def mat_press(self):
        self.change_mode("mat")
        #self.screen.ids.mat.md_bg_color
        self.screen.ids.matknapp.md_bg_color = [.4,.4,.4,1]
        self.screen.ids.transknapp.md_bg_color = [1,1,1,1]

    def trans_press(self):
        self.change_mode("transport")
        self.screen.ids.transknapp.md_bg_color = [.4,.4,.4,1]
        self.screen.ids.matknapp.md_bg_color = [1,1,1,1]


        #This function takes the value of what is put in the textfield in the gui
        #and sends it to the assistan using run_conversation

        

    def press(self):
        input = self.screen.ids.input.text
        #self.screen.ids.response.text = run_conversation(input)

        print("input: ", input)
        print("mode: ", self.mode)
        #Clears the 
        self.screen.ids.input.text = ""



MainApp().run()
