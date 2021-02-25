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
    data = []
    chartLabels = []
    chartColors = []
    print('nice')
    if float(doc['food']) != 0:
        data.append(float(doc['food']))
        chartLabels.append('Food')
        chartColors.append('green')
    if float(doc['transport']) != 0:
        data.append(float(doc['food']))
        chartLabels.append('Transport')
        chartColors.append('grey')
    if float(doc['electricity']) != 0:
        data.append(float(doc['electricity']))
        chartLabels.append('Electricity')
        chartColors.append('yellow')
    plt.clf()
    plt.pie(data, labels=chartLabels, colors=chartColors)
    plt.savefig('piechart.png', transparent=True)
