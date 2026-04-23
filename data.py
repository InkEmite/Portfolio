import numpy as np

def generate_data(n=100):
    np.random.seed(0)
    X = 2 * np.random.rand(n, 1)
    Y = 4 + 3 * X + np.random.randn(n, 1) # True w=3, b=4
    return X, Y
