import GetData as d
import SendData as s
import Chart
import numpy as np
import matplotlib.pyplot as plt


# def add_emission(type, value):
#     print(emission)


# emission = np.array([float(d.GetItem.get_food('Burger')),
#                      float(d.GetItem.get_transport('liten'))])
# chartLabels = ['Food', 'Transport']
# chartColors = ['green', 'grey']

if __name__ == '__main__':
    s.sendCo2(15, 'food')
