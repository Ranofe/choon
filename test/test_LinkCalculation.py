import unittest

import numpy as np

from choon.LinkCalculation import LinkCalculation
from choon.tools import k

test_TX = {
    'HPA_dBm': 30,
    'antenna_dB': 23,
    'losses': 0.4,
    'bandwidth_MHz': 50,
    'frequency_MHz': 8000,
}

test_RX = {
    'antenna_dB': 46.8,
    'noise_temp_k': 290,
    'losses': 2,
    'noise_figure_dB': 1,
    'LNA_gain': 30,
}

distances_km = np.arange(500, 2000, 100)


class TestLinkCalculation(unittest.TestCase):
    def setUp(self):
        self.Link = LinkCalculation(test_TX, test_RX, distances_km)

    def test_noise_floor_dbm(self):
        temp_k = self.Link.rx['noise_temp_k']
        bandwidth_MHz = self.Link.tx['bandwidth_MHz']
        test_noise = 10 * np.log10(temp_k * k) + 30 + 10 * np.log10(bandwidth_MHz * 1e6)
        self.assertEqual(self.Link.noise_floor_dbm(), test_noise, "noise floor calculation error")

    def test_free_space_loss(self):
        fsp_dB = 20 * np.log10(distances_km) + 20 * np.log10(test_TX['frequency_MHz']) + 32.45
        self.assertEqual((self.Link.fsp_dB == fsp_dB).all(), True)

    def test_link_margin(self):
        link_margin = np.array(
            [
                28.89428732,
                27.3106624,
                25.97172661,
                24.81188767,
                23.78883722,
                22.87368741,
                22.04583371,
                21.29006249,
                20.59482036,
                19.9511267,
                19.35186223,
                18.79128776,
                18.26470898,
                17.76823731,
                17.29861539,
            ]
        )
        self.assertEqual((self.Link.link_margin().round(5) == link_margin.round(5)).all(), True)
