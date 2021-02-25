from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import cloudant

import json

client = Cloudant.iam('5861e444-61ce-4c94-8d14-a94dfa36ede3-bluemix',
                      'R9ePmy_llFF4gTtBPQROafzl4Ee2xALLiMzTWeCCnn13', connect=True)
client.connect()


def sendCo2(amount, type):
    doc = client['user']['userCo2']


doc = client['user']['userCo2']
doc.update_field(action=doc.list_field_append,
                 field='food', value=str(213))

sendCo2(20, 'food')
