import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('Paa0LICW2gszbzgDQX_83y5td9ggmRiv0H2RvA88uG0w')

#2021-02-11
assistant = AssistantV2(
    version='2020-09-24',
    authenticator=authenticator
)

assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')

sesh_id = assistant.create_session(
    assistant_id='6bc3d805-70f6-4f71-9ee0-def44227ed12'
).get_result()

#print(sesh_id)
#print(sesh_id['session_id'])

py_sesh_id = sesh_id['session_id']

#py_sesh_id = json.loads(sesh_id)
#print(py_sesh_id)
#print(json.dumps(sesh_id, indent=2))

user_input = input("What do you want to ask the bot?")


#ass id: 6bc3d805-70f6-4f71-9ee0-def44227ed12

#sends user_input to the bot and stores the response in response
response = assistant.message(
    assistant_id='6bc3d805-70f6-4f71-9ee0-def44227ed12',
    session_id=py_sesh_id,
    input={
        'message_type': 'text',
        'text': user_input
    }
).get_result()

#extremly messy code, will fix later
output = response['output']
generic = output['generic']
generic_list = generic[0]
bot_output = generic_list['text'] 

print(bot_output)


#print(json.dumps(response, indent=2))