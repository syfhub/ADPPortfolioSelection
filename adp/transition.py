import numpy as np

from data import N
from .parameters import theta


def ft(h: np.ndarray, R: np.ndarray, x: np.ndarray, y: np.ndarray):
    """
    Transition function.
    :param h: Pre-decision state at previous time (h_(t-1))
    :param R: Returns at time t
    :param x: Buys
    :param y: Sales
    :return : h_plus, post-decision state variable
    :rtype  : np.ndarray
    """
    h_plus = np.zeros(N + 1, dtype=object)
    h_plus[1:] = R[1:] * h[1:] + x - y
    h_plus[0] = R[0] * h[0] - (1 + theta) * x.sum() + (1 - theta) * y.sum()
    return h_plus
