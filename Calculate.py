import GetData as d
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

client = Cloudant.iam('5861e444-61ce-4c94-8d14-a94dfa36ede3-bluemix',
                      'R9ePmy_llFF4gTtBPQROafzl4Ee2xALLiMzTWeCCnn13', connect=True)
client.connect()


def calc_transport(type, dist):
    data = client['items']['transport']
    if type == 'small' or type == 'medium' or type == 'large':
        return float(data['car'][type]) * dist
    elif type == 'bus':
        return float(data['bus']) * dist
    elif type == 'train':
        return float(data['train']) * dist
    elif type == 'boat':
        return float(data['boat']) * dist
    elif type == 'flight':
        return float(data['flight']) * dist
