import unittest

import numpy as np

from choon.LinkCalculation import noise_floor_dbm
from choon.tools import k


class TestLinkCalculation(unittest.TestCase):
    def test_noise_floor_dbm(self):
        temp_k = 279
        test_noise = 10 * np.log10(temp_k * k) + 30
        self.assertEqual(noise_floor_dbm(temp_k), test_noise, "noise floor calculation error")
