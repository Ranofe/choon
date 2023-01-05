import numpy as np

from choon.LinkCalculation import LinkCalculation
from choon.tools import k

test_TX = {
        'HPA_dBm' : 30,
        'antenna_dB' : 23,
        'losses_dB' : 0.4,
        'bandwidth_MHz': 50,
        'frequency_MHz': 8000,
}

test_RX = {
        'antenna_dB': 46.8,
        'noise_temp_k': 290,
        'losses_dB' : 2,
        'noise_figure_dB': 1,
        'LNA_gain_dB':30,
}

distances_km = np.arange(500,2000,100)

Link = LinkCalculation(test_TX, test_RX, distances_km)

from IPython import embed; embed()
