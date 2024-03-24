import random

import matplotlib.pyplot as plt
import numpy as np


def sign(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1


def cumulative_dist(x):
    return 0.5 + ((sign(x) / 2) * (1 - (np.exp(-(2 * (x ** 2)) / np.pi))) ** 0.5)


def inverse_phi(x):
    x = ((-np.pi * np.log(1 - ((2 * x - 1) ** 2))) / 2)**0.5
    return -x, x


def sampler(iterations_list):
    for p in iterations_list:
        vals = []
        for i in range(p):
            vals.extend(inverse_phi(random.random()))
        plt.hist(vals, bins=50, range=[-5, 5])
        plt.show()


if __name__ == '__main__':
    print(sampler([1000]))
