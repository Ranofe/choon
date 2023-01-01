import numpy as np

from choon.tools import k


def noise_floor_dbm(temparature_k):
    return 10 * np.log10(temparature_k * k) + 30
