from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

import json

client = Cloudant.iam('5861e444-61ce-4c94-8d14-a94dfa36ede3-bluemix',
                      'R9ePmy_llFF4gTtBPQROafzl4Ee2xALLiMzTWeCCnn13', connect=True)
client.connect()


class GetItem():
    dataBase = client['items']
    # returns foods data

    def get_food(name):
        dataBase = client['items']
        foodId = '487eede4ba4d1bc440dda6bf9a9e49c5'
        for doc in dataBase:
            if doc['_id'] == foodId:
                for item in doc['food']:
                    if item['name'] == name:
                        return item['co2']

    def get_transport(name):
        dataBase = client['items']
        transportId = 'transport'
        for doc in dataBase:
            if doc['_id'] == transportId:
                for item in doc['car']:
                    if item['type'] == name:
                        return item['co2']

# print(dataBase)
# result = Result(dataBase, include_docs=True)

# print(format(result[0]))

# GetItem.get_food('BigMac')
