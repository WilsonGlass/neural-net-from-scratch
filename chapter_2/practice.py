import numpy as np

"""
In this code, we have three sets of weights and three biases, which define
three neurons. Each Neuron is "connected" to the same inputs. The difference
is in the separate weights and bias that each neuron applies to the input.
This is called a _fully_connected_ nn -- every neuron in the current layer
has connections to every neuron from the previous layer.

Note: It is not a requirement that nns have to be fully connected
"""

# V1.0
inputs = [1, 2, 3, 2.5]

weights1 = [.2, .8, -.5, 1]
weights2 = [.5, -.91, .26, -.5]
weights3 = [-.26, -.27, .17, .87]

bias1 = 2
bias2 = 3
bias3 = .5

outputs = [
    # Neuron 1:
    inputs[0] * weights1[0] +
    inputs[1] * weights1[1] +
    inputs[2] * weights1[2] +
    inputs[3] * weights1[3] + bias1,

    # Neuron 2:
    inputs[0] * weights2[0] +
    inputs[1] * weights2[1] +
    inputs[2] * weights2[2] +
    inputs[3] * weights2[3] + bias2,

    # Neuron 3:
    inputs[0] * weights3[0] +
    inputs[1] * weights3[1] +
    inputs[2] * weights3[2] +
    inputs[3] * weights3[3] + bias3
]

"""
>>>
[4.8, 1.21, 2.385]

Obviously this gets very tiring, so we can write something like this
"""
# V2.0

# Output of the current layer
layer_outputs = []
weights = [weights1, weights2, weights3]
biases = [bias1, bias2, bias3]
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    # For each input and weight to the neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply this input by associated weight
        # and add to the neuron's output variable
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)


# V3.0
outputs = np.dot(weights, inputs) + biases


# To get the layer outputs:
inputs = [[1.0, 2.0, 3.0, 2.5]
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -.8]]
outputs = np.dot(inputs, np.array(weights).T) + biases
"""
>>>
array ([ 4.8,   1.21,    2.835],
       [ 8.9,   -1.81,  .2    ],
       [ 1.41,  1.051,  .026  ]]
       )
       
As you can see, our neural network
takes in a group of samples (inputs) and outputs a group
of predictions.
"""


