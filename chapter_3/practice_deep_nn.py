"""
For a Neural Network to be considered "deep" we need to have 2 or more
_hidden_layers_
"""

import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2., 5., -1., 2],
          [-1.5, 2.7, 3.3, -.8]]

weights = [[.2, .8, -.5, 1],
           [.5, -.91, .26, -.5],
           [-.26, -.27, .17, .87]]

biases = [2, 3, .5]

weights2 = [[.1, -.14, .5],
            [-.5, .12, -.33],
            [-.44, .73, .13]]

biases2 = [-1, 2, -.5]

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T + biases2)

"""
>>>
array([[ .5031, -1.04185, -2.03875],
       [ .2434, -2.7332,  -5.7633 ],
       [ -.99314, 1.41254, -.35655]])
"""