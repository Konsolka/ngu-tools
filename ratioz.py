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
        stats_energy_power = stats.energyPower
        stats_energy_cap = stats.capEnergy
        stats_energy_bar = stats.energyBars

        stats_magic_power = stats.magicPower
        stats_magic_cap = stats.magicCap
        stats_magic_bar = stats.magicBar
        # ENERGY
        #   CURRENT RATIO
        self.current_energy_ratio_power = 1.0
        self.current_energy_ratio_cap = int(stats_energy_cap / stats_energy_power)
        self.current_energy_ratio_bars = round(stats_energy_bar / stats_energy_power, 2)
        #   GOAL RATIO / TEXT INPUT
        self.edit_power = 1
        self.edit_cap = 37500
        self.edit_bar = 1
        current_goal_energy_ratio_power = 1
        self.current_goal_energy_ratio_cap = stats_energy_cap / self.edit_cap / stats_energy_power * self.edit_power
        self.current_goal_energy_ratio_bar = stats_energy_bar / self.edit_bar / stats_energy_power * self.edit_power
        max_of_current_goal_energy_ratio = max(current_goal_energy_ratio_power, self.current_goal_energy_ratio_cap,
                                               self.current_goal_energy_ratio_bar)
        #   BASE GOAL
        self.energy_base_goal_power = ceiling_precise(stats_energy_power * max_of_current_goal_energy_ratio, 0.1)
        self.energy_base_goal_cap = ceiling_precise(self.energy_base_goal_power / self.edit_power * self.edit_cap, 250)
        self.energy_base_goal_bars = math.ceil(self.energy_base_goal_power / self.edit_power * self.edit_bar)
        #   AMOUNT LEFT TO BUY
        self.amount_left_to_buy_power = self.energy_base_goal_power - stats_energy_power
        self.amount_left_to_buy_cap = self.energy_base_goal_cap - stats_energy_cap
        self.amount_left_to_buy_bars = self.energy_base_goal_bars - stats_energy_bar
        #   EXP COST
        self.energy_exp_cost_power = self.amount_left_to_buy_power * 150
        self.energy_exp_cost_cap = self.amount_left_to_buy_cap * 0.004
        self.energy_exp_cost_bar = self.amount_left_to_buy_bars * 80
        #   TOTAL EXP COST
        self.amount_left_to_buy_sum = self.energy_exp_cost_bar + self.energy_exp_cost_power + self.energy_exp_cost_cap

        #MAGIC
        #   CURRENT RATIO
        self.current_magic_ratio_power = 1.0
        self.current_magic_ratio_cap = int(stats_magic_cap / stats_magic_cap)
        self.current_magic_ratio_bars = round(stats_magic_bar / stats_magic_cap, 2)
        #   GOAL RATIO
        self.magic_edit_power = 1
        self.magic_edit_cap = 40000
        self.magic_edit_bar = 1
        current_goal_magic_ratio_power = 1
        self.current_goal_magic_ratio_cap = stats_magic_cap / self.magic_edit_cap / stats_magic_cap * self.magic_edit_power
        self.current_goal_magic_ratio_bar = stats_magic_bar / self.magic_edit_bar / stats_magic_cap * self.magic_edit_power
        max_of_current_goal_magic_ratio = max(current_goal_magic_ratio_power, self.current_goal_magic_ratio_cap,
                                              self.current_goal_magic_ratio_bar)
        #   BASE GOAL
        self.magic_base_goal_power = ceiling_precise(stats_magic_cap * max_of_current_goal_magic_ratio, 0.1)
        self.magic_base_goal_cap = ceiling_precise(
            self.magic_base_goal_power / self.magic_edit_power * self.magic_edit_cap, 250)
        self.magic_base_goal_bars = math.ceil(self.magic_base_goal_power / self.magic_edit_power * self.magic_edit_bar)
        #   AMOUNT LEFT TO BUY
        self.magic_amount_left_to_buy_power = self.magic_base_goal_power - stats_magic_cap
        self.magic_amount_left_to_buy_cap = self.magic_base_goal_cap - stats_magic_cap
        self.magic_amount_left_to_buy_bars = self.magic_base_goal_bars - stats_magic_bar
        #   EXP COST
        self.magic_exp_cost_power = self.magic_amount_left_to_buy_power * 450
        self.magic_exp_cost_cap = self.magic_amount_left_to_buy_cap * 0.012
        self.magic_exp_cost_bar = self.magic_amount_left_to_buy_bars * 240
        #   TOTAL EXP COST
        self.magic_amount_left_to_buy_sum = self.magic_exp_cost_bar + self.magic_exp_cost_power + self.magic_exp_cost_cap


    def update_magic(self):
        pass

    def update_energy(self):
        pass
