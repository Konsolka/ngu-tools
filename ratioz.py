from deserialize_dot_net import Deserializer
from handler import Handler
from stats import Stats


class Ratios:
    def __init__(self, stats:Stats):
        self.current_energy_ratio_power = 1
        self.current_energy_ratio_cap = stats.capEnergy / stats.energyBars
        self.current_energy_ratio_bars = stats.energyBars / 1
        self.edit_bar = 1
        self.edit_cap = 37500
        self.edit_power = 1
