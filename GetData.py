from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

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
    def get_total(self):
        dataBase = client['user']
        userId = 'userCo2'
        food = ""
        electricity = ""
        transport = ""
        for doc in dataBase:
            if doc['_id'] == userId:
                for item in doc['food']:
                    food += item
                for item in doc['electricity']:
                    electricity += item
                for item in doc['transport']:
                    transport += item
                total = float(food) + float(electricity) + float(transport)
            return total

# print(dataBase)
# result = Result(dataBase, include_docs=True)
# print(format(result[0]))
# GetItem.get_food('BigMac')
