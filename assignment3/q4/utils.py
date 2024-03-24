import numpy as np


def wrapped_angle_diff(a1, a2):
    diff = a1 - a2
    if diff > np.pi:
        diff -= 2 * np.pi
    if diff < -np.pi:
        diff += 2 * np.pi
    return diff


def state_dist(p1, p2):
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((wrapped_angle_diff(p1[2], p2[2])) ** 2)) ** 0.5
