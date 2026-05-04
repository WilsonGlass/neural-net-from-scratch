<b>Activation Functions</b>

Examples:
* Linear activation function (y = x)
* Sigmoid (1 / (1 + e^-x))
* ReLU (x, x > 0, y, y <= 0)

Why use activation functions?

Many interesting problems are non-linear,
which is why we would want to use a neural network
to begin with.

E.g.

A neural network with linear activation functions in
hidden layers attempting to fit sin(x) would draw a straight line.
ReLU activation functions in hidden layers attempting to fit
y = sin(x) actually fits the function.

E.g.

When we use linear activation, no matter
what we do, however many layers we have,
this network can only depict linear relationships
if we use linear activation functions. 

<b>ReLU Activation in a pair of neurons</b>

With a negative weight and a single neuron, the function
has become a question of when this neuron _deactivates_.

