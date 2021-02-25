import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import GetData

# Sets API Key
authenticator = IAMAuthenticator('cHqjiL405gfXgXgfOCzESnez_H3uqQt93LDn7HIYGDsw')

# Inits assistant
assistant = AssistantV2(
    version='2020-09-24',
    authenticator=authenticator
)
assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')

sesh_id = assistant.create_session(
    assistant_id='dc3a8482-d13c-4913-bc48-44785b5d14d5'
).get_result()

# Sets py_sesh_id to the session id
py_sesh_id = sesh_id['session_id']


###################################################################################


# See KivyMDTest.py for code comments.
def run_conversation(input):
    user_input = input

    response = assistant.message(
        assistant_id='dc3a8482-d13c-4913-bc48-44785b5d14d5',
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
    print(bot_output)
    print(GetData.GetItem.get_food(bot_output))
    return bot_output

# Adds values returned from run_conversation() to a list
returned = []
returned.append(run_conversation(input("Please ask me something")))