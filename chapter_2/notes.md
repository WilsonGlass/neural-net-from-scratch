Often, neural networks expect to take in many <b>samples</b>
at a time for two reasons. One reason is that it's faster to train in batches
in parallel processing, and the other reason is that
batches help with generalization during training. If you fit
(perform a step of training process) on one
sample at a time, you're highly likely to keep fitting
to that individual sample, rather than slowly producing general
tweaks to weights and biases that fit the entire dataset.
Fitting or training in batches gives you a higher chance of making more meaningful
changes to weights and biases.

E.g. a batch of data could look like:
```python
batch = [[1, 5, 6, 2],
         [3, 2, 1, 3],
         ...
]

# Shape: (8, 4) Matrix
```