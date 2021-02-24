import GetData as d
import numpy as np
import matplotlib.pyplot as plt


# def add_emission(type, value):
#     print(emission)


emission = np.array([float(d.GetItem.get_food('Burger')),
                     float(d.GetItem.get_transport('suv'))])
chartLabels = ['Food', 'Transport']
chartColors = ['green', 'grey']

if __name__ == '__main__':
    plt.pie(emission, labels=chartLabels, colors=chartColors)
    plt.show()
