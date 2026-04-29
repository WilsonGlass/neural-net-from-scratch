from nnfs.datasets import spiral_data
import numpy as np
import matplotlib.pyplot as plt

"""
Next, rather than hand-typing random data, we'll use a function that can create
non-linear data.
"""

X, y = spiral_data(samples=100, classes=3)
plt.scatter(X[:, 0], X[:,1])
plt.show()

# TODO: add this in a notebook instead of raw python