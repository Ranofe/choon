import numpy as np
import pandas as pd

from choon.tools import k


class LinkCalculation:
    """Calculates the link budget from a given Tx, Rx and distances"""

    def __init__(self, Tx, Rx, distances_km):
        # add exception in case of wrong inputs
        self.tx = Tx
        self.rx = Rx
        self.distances_km = distances_km
        try:
            self.free_space_loss()
            self.link_margin()
            self.data_frame_results()
        except:
            error_print = """
            Data structure error!

            Data structure shall be like the next example.
            TX = {
                    'HPA_dBm' : #,
                    'antenna_dB' : #,
                    'losses_dB' : #,
                    'bandwidth_MHz': #,
                    'frequency_MHz': #,
            }

            RX = {
                    'antenna_dB': #,
                    'noise_temp_k': #,
                    'losses_dB' : #,
                    'noise_figure_dB': #,
                    'LNA_gain_dB':#,
            }

            Distances = numpy array
            """
            print(error_print)

    def noise_floor_dbm(self):
        return 10 * np.log10(self.rx['noise_temp_k'] * k) + 30 + 10 * np.log10(self.tx['bandwidth_MHz'] * 1e6)

    def link_margin(self):
        self.link_margin_dB = (
            self.tx['HPA_dBm']
            + self.tx['antenna_dB']
            + self.tx['losses_dB'] * (-1)
            + self.rx['antenna_dB']
            + self.rx['losses_dB'] * (-1)
            + self.rx['noise_figure_dB'] * (-1)
            + self.fsp_dB * (-1)
            + self.noise_floor_dbm() * (-1)
        )
        return self.link_margin_dB

    def free_space_loss(self):
        self.fsp_dB = 20 * np.log10(self.distances_km) + 20 * np.log10(self.tx['frequency_MHz']) + 32.45

    def data_frame_results(self):
        result_dict = {
            'distances_km': self.distances_km,
            'link_margin_dB': self.link_margin_dB,
        }
        self.results = pd.DataFrame(result_dict)
