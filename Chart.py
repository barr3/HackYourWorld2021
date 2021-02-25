import GetData as d
import Chart
import numpy as np
import matplotlib.pyplot as plt


class MakeChart:

    def piechart(data, chartLabels, chartColors):
        plt.pie(data, labels=chartLabels, colors=chartColors)
        plt.savefig('piechart.png')
