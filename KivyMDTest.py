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

    output = response['output']
    generic = output['generic']
    generic_list = generic[0]
    bot_output = generic_list['text']
    #print(bot_output) 
    return bot_output



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
        input = self.screen.ids.input.text
        self.screen.ids.response.text = run_conversation(input)
        self.screen.ids.input.text = ""


    
    





MainApp().run()

