from deserialize_dot_net import Deserializer
from handler import Handler
from stats import Stats
import math

def ceiling_precise(number, significance=1.0):
    if significance == 0:
        raise ValueError("Significance cannot be zero.")

    # Significance must be positive
    significance = abs(significance)

    return math.ceil(number / significance) * significance

class Ratios:
    def __init__(self, stats:Stats):
        self.current_energy_ratio_power = 1.0
        self.current_energy_ratio_cap = int(stats.capEnergy / stats.energyPower)
        self.current_energy_ratio_bars = round(stats.energyBars / stats.energyPower, 2)
        self.edit_bar = 1
        self.edit_cap = 37500
        self.edit_power = 1
        current_goal_energy_ratio_power = 1
        current_goal_energy_ratio_cap = stats.capEnergy / self.edit_cap / stats.energyPower * self.edit_power
        current_goal_energy_ratio_bar = stats.energyBars / self.edit_bar / stats.energyPower * self.edit_power
        max_of_current_goal_energy_ratio = max(current_goal_energy_ratio_power, current_goal_energy_ratio_cap, current_goal_energy_ratio_bar)
        self.energy_base_goal_power = ceiling_precise(stats.energyPower * max_of_current_goal_energy_ratio, 0.1)
        self.energy_base_goal_cap = ceiling_precise(self.energy_base_goal_power / self.edit_power * self.edit_cap, 250)
        self.energy_base_goal_bars = math.ceil(self.energy_base_goal_power / self.edit_power * self.edit_bar)
        self.amount_left_to_buy_power = self.energy_base_goal_power - stats.energyPower
        self.amount_left_to_buy_cap = self.energy_base_goal_cap - stats.capEnergy
        self.amount_left_to_buy_bars = self.energy_base_goal_bars - stats.energyBars
        self.energy_exp_cost_power = self.amount_left_to_buy_power * 150
        self.energy_exp_cost_cap = self.amount_left_to_buy_cap * 0.004
        self.energy_exp_cost_bar = self.amount_left_to_buy_bars * 80
        self.amount_left_to_buy_sum = self.energy_exp_cost_bar + self.energy_exp_cost_power + self.energy_exp_cost_cap

