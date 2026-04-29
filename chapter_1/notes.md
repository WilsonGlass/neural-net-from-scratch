<b>Chapter 1</b>

AI $\subseteq$ ML $\subseteq$ Neural Networks $\subseteq$ Deep Neural Networks

<b>Layer Sizes: 10, 16, 16, 2</b>

$\therefore$ Weights:    +704

$\therefore$ Biases:     +50

$\therefore$ Params:     =754

The end goal for a nn is to adjust their
weights and biases (parameters) s.t. when applied
to a yet-unseen example in the input, they produce
the desired output.

When supervised machine learning algorithms are trained,
we show the algorithm examples of inputs and their associated
desired outputs. One major issue with this concept is
<b>overfitting.</b> When the algorithm only learns
to fit the training data but doesn't actually "understand" anything
about the underlying input-output dependencies. The network basically
just "memorizes" the training data.

$\therefore$ We tend to use "in-sample" data to train
a model and then use "out-of-sample" data to validate
an algorithm (or nn). E.g. 10% "out-of-sample/validation" data -> 90% "in-sample/training" data.

The goal is for the model to not only accurately predict on the training data,
but also be similarly accurate while predicting on the withheld
out-of-sample validation data.

This is called <b>generalization</b>, which means learning
to fit the data instead of memorizing it. The idea is that we "train"
a nn on many examples of data. We then take out-of-sample
data that the nn has never been presented with and hope it can
accurately predict on these data too.

How "wrong" they are -> <b>loss</b>

