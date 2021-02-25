import os
import GetData as d
import Chart
import numpy as np
import matplotlib.pyplot as plt

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import cloudant

client = Cloudant.iam('5861e444-61ce-4c94-8d14-a94dfa36ede3-bluemix',
                      'R9ePmy_llFF4gTtBPQROafzl4Ee2xALLiMzTWeCCnn13', connect=True)
client.connect()


def piechart():
    doc = client['user']['userCo2']
    food = 0
    transport = 0
    electricity = 0

    food += float(doc['food'])
    transport += float(doc['transport'])
    electricity += float(doc['electricity'])

    data = [food, transport, electricity]
    chartLabels = ['food', 'transport', 'electricity']
    chartColors = ['green', 'grey', 'yellow']
    plt.clf()
    plt.pie(data, labels=chartLabels, colors=chartColors)
    plt.savefig('piechart.png', transparent=True)
