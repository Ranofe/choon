import numpy as np

from choon.tools import k


class LinkCalculation:
    """Calculates the link budget from a given Tx, Rx and distances"""

    def __init__(self, Tx, Rx, distances_km):
        #add exception in case of wrong inputs
        self.tx = Tx
        self.rx = Rx
        self.distances_km = distances_km
        self.free_space_loss()

    def noise_floor_dbm(self):
        return 10 * np.log10(self.rx['noise_temp_k'] * k) + 30 + 10*np.log10(self.tx['bandwidth_MHz']*1e6)

    def link_margin(self):
        self.link_margin_dB = self.tx['HPA_dBm'] + \
                              self.tx['antenna_dB'] + \
                              self.tx['losses']*(-1) + \
                              self.rx['antenna_dB'] + \
                              self.rx['losses']*(-1) + \
                              self.rx['noise_figure_dB']*(-1) +\
                              self.fsp_dB*(-1) +\
                              self.noise_floor_dbm()*(-1)
        return self.link_margin_dB

    def free_space_loss(self):
        self.fsp_dB = 20*np.log10(self.distances_km) + 20*np.log10(self.tx['frequency_MHz']) + 32.45
