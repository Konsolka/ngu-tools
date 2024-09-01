import math

from src.logger import logger
from src.stats import Stats

def ceiling_precise(number, significance=1.0):
    if significance == 0:
        raise ValueError("Significance cannot be zero.")

    # Significance must be positive
    significance = abs(significance)

    return math.ceil(number / significance) * significance

class Ratios:
    def __init__(self, stats:Stats):
        self.stats_energy_power = stats.energy_base_power
        self.stats_energy_cap = stats.energy_base_cap
        self.stats_energy_bar = stats.energy_base_bars

        self.stats_magic_power = stats.magicPower
        self.stats_magic_cap = stats.magicCap
        self.stats_magic_bar = stats.magicBar

        self.stats_r3_base_power = stats.r3_base_power
        self.stats_r3_base_cap = stats.r3_base_cap
        self.stats_r3_base_bar = stats.r3_base_bar

        self.update_all()

    def update_all(self):
        self.update_energy()
        self.update_magic()
        self.update_r3()
        self.update_em()
        self.update_me()

    def update_energy(self, energy_edit_power = 1, energy_edit_cap = 37500, energy_edit_bar = 1):
        #   CURRENT RATIO
        self.current_energy_ratio_power = 1.0
        self.current_energy_ratio_cap = int(self.stats_energy_cap / self.stats_energy_power)
        self.current_energy_ratio_bars = round(self.stats_energy_bar / self.stats_energy_power, 2)
        #   GOAL RATIO / TEXT INPUT
        self.edit_power = energy_edit_power
        self.edit_cap = energy_edit_cap
        self.edit_bar = energy_edit_bar
        current_goal_energy_ratio_power = 1
        self.current_goal_energy_ratio_cap = self.stats_energy_cap / self.edit_cap / self.stats_energy_power * self.edit_power
        self.current_goal_energy_ratio_bar = self.stats_energy_bar / self.edit_bar / self.stats_energy_power * self.edit_power
        self.max_of_current_goal_energy_ratio = max(current_goal_energy_ratio_power, self.current_goal_energy_ratio_cap,
                                                    self.current_goal_energy_ratio_bar)
        #   BASE GOAL
        self.energy_base_goal_power = ceiling_precise(self.stats_energy_power * self.max_of_current_goal_energy_ratio,
                                                      0.1)
        self.energy_base_goal_cap = ceiling_precise(self.energy_base_goal_power / self.edit_power * self.edit_cap, 250)
        self.energy_base_goal_bars = math.ceil(self.energy_base_goal_power / self.edit_power * self.edit_bar)
        #   AMOUNT LEFT TO BUY
        self.amount_left_to_buy_power = self.energy_base_goal_power - self.stats_energy_power
        self.amount_left_to_buy_cap = self.energy_base_goal_cap - self.stats_energy_cap
        self.amount_left_to_buy_bars = self.energy_base_goal_bars - self.stats_energy_bar
        #   EXP COST
        self.energy_exp_cost_power = self.amount_left_to_buy_power * 150
        self.energy_exp_cost_cap = self.amount_left_to_buy_cap * 0.004
        self.energy_exp_cost_bar = self.amount_left_to_buy_bars * 80
        #   TOTAL EXP COST
        self.amount_left_to_buy_sum = self.energy_exp_cost_bar + self.energy_exp_cost_power + self.energy_exp_cost_cap

    def update_magic(self, magic_edit_power = 1, magic_edit_cap = 40000, magic_edit_bar = 1):
        #   CURRENT RATIO
        self.current_magic_ratio_power = 1.0
        self.current_magic_ratio_cap = int(self.stats_magic_cap / self.stats_magic_power)
        self.current_magic_ratio_bars = round(self.stats_magic_bar / self.stats_magic_power, 2)
        #   GOAL RATIO
        self.magic_edit_power = magic_edit_power
        self.magic_edit_cap = magic_edit_cap
        self.magic_edit_bar = magic_edit_bar
        current_goal_magic_ratio_power = 1
        self.current_goal_magic_ratio_cap = self.stats_magic_cap / self.magic_edit_cap / self.stats_magic_power * self.magic_edit_power
        self.current_goal_magic_ratio_bar = self.stats_magic_bar / self.magic_edit_bar / self.stats_magic_power * self.magic_edit_power
        max_of_current_goal_magic_ratio = max(current_goal_magic_ratio_power, self.current_goal_magic_ratio_cap,
                                              self.current_goal_magic_ratio_bar)
        #   BASE GOAL
        self.magic_base_goal_power = ceiling_precise(self.stats_magic_power * max_of_current_goal_magic_ratio, 0.1)
        self.magic_base_goal_cap = ceiling_precise(
            self.magic_base_goal_power / self.magic_edit_power * self.magic_edit_cap, 250)
        self.magic_base_goal_bars = math.ceil(self.magic_base_goal_power / self.magic_edit_power * self.magic_edit_bar)
        #   AMOUNT LEFT TO BUY
        self.magic_amount_left_to_buy_power = self.magic_base_goal_power - self.stats_magic_power
        self.magic_amount_left_to_buy_cap = self.magic_base_goal_cap - self.stats_magic_cap
        self.magic_amount_left_to_buy_bars = self.magic_base_goal_bars - self.stats_magic_bar
        #   EXP COST
        self.magic_exp_cost_power = self.magic_amount_left_to_buy_power * 450
        self.magic_exp_cost_cap = self.magic_amount_left_to_buy_cap * 0.012
        self.magic_exp_cost_bar = self.magic_amount_left_to_buy_bars * 240
        #   TOTAL EXP COST
        self.magic_amount_left_to_buy_sum = self.magic_exp_cost_bar + self.magic_exp_cost_power + self.magic_exp_cost_cap

    def update_r3(self, r3_edit_power = 1, r3_edit_cap = 40000, r3_edit_bar = 1):
        #   CURRENT RATIO
        self.r3_current_ratio_power = 1.0
        self.r3_current_ratio_cap = int(self.stats_r3_base_cap / self.stats_r3_base_power)
        self.r3_current_ratio_bars = round(self.stats_r3_base_bar / self.stats_r3_base_power, 2)
        #   GOAL RATIO / TEXT INPUT
        self.r3_edit_power = r3_edit_power
        self.r3_edit_cap = r3_edit_cap
        self.r3_edit_bar = r3_edit_bar
        r3_current_goal_ratio_power = 1
        self.r3_current_goal_ratio_cap = self.stats_r3_base_cap / self.r3_edit_cap / self.stats_r3_base_power * self.r3_edit_power
        self.r3_current_goal_ratio_bar = self.stats_r3_base_bar / self.r3_edit_bar / self.stats_r3_base_power * self.r3_edit_power
        self.r3_max_of_current_goal_ratio = max(r3_current_goal_ratio_power, self.r3_current_goal_ratio_cap,
                                                    self.r3_current_goal_ratio_bar)
        #   BASE GOAL
        self.r3_base_goal_power = ceiling_precise(self.stats_r3_base_power * self.r3_max_of_current_goal_ratio,
                                                      0.1)
        self.r3_base_goal_cap = ceiling_precise(self.r3_base_goal_power / self.r3_edit_power * self.r3_edit_cap, 250)
        self.r3_base_goal_bars = math.ceil(self.r3_base_goal_power / self.r3_edit_power * self.r3_edit_bar)
        #   AMOUNT LEFT TO BUY
        self.r3_amount_left_to_buy_power = self.r3_base_goal_power - self.stats_r3_base_power
        self.r3_amount_left_to_buy_cap = self.r3_base_goal_cap - self.stats_r3_base_cap
        self.r3_amount_left_to_buy_bars = self.r3_base_goal_bars - self.stats_r3_base_bar
        #   EXP COST
        self.r3_exp_cost_power = self.r3_amount_left_to_buy_power * 15000000
        self.r3_exp_cost_cap = self.r3_amount_left_to_buy_cap * 400
        self.r3_exp_cost_bar = self.r3_amount_left_to_buy_bars * 8000000
        #   TOTAL EXP COST
        self.r3_amount_left_to_buy_sum = self.r3_exp_cost_power + self.r3_exp_cost_cap + self.r3_exp_cost_bar

    def update_em(self, em_energy = 6.0, em_magic = 2.0):
        #   GOAL ENERGY MAGIC
        self.em_goal_em = em_energy / em_magic
        #   CURRENT ENERGY:MAGIC RATIO
        self.em_cr_power = self.stats_energy_power / self.stats_magic_power
        self.em_cr_cap = self.stats_energy_cap / self.stats_magic_cap
        self.em_cr_bar = self.stats_energy_bar / self.stats_magic_bar
        #   OPTIMAL ENERGY FOR MAGIC AT RATIO
        self.em_optimal_for_current_power = self.stats_energy_power * max(1, self.em_goal_em / self.em_cr_power)
        self.em_optimal_for_current_cap = self.stats_energy_cap * max(1, self.em_goal_em / self.em_cr_cap)
        self.em_optimal_for_current_bar = self.stats_energy_bar * max(1, self.em_goal_em / self.em_cr_bar)
        #   AMOUNT LEFT TO BUY
        self.em_amount_left_to_buy_power = self.em_optimal_for_current_power - self.stats_energy_power
        self.em_amount_left_to_buy_cap = self.em_optimal_for_current_cap - self.stats_energy_cap
        self.em_amount_left_to_buy_bar = self.em_optimal_for_current_bar - self.stats_energy_bar
        self.em_amount_left_to_buy_sum = self.em_amount_left_to_buy_power + self.em_amount_left_to_buy_cap + self.em_amount_left_to_buy_bar
        #   EXP COST
        self.em_exp_cost_power = self.em_amount_left_to_buy_power * 150
        self.em_exp_cost_cap = self.em_amount_left_to_buy_cap * 0.004
        self.em_exp_cost_bar = self.em_amount_left_to_buy_bar * 80

    def update_me(self, em_energy = 6.0, em_magic = 2.0):
        #   GOAL MAGIC ENERGY
        self.em_goal_em = em_energy / em_magic
        #   OPTIMAL ENERGY FOR MAGIC AT RATIO
        self.me_optimal_for_current_power = round(ceiling_precise(self.stats_magic_power / min(1, self.em_goal_em / self.em_cr_power), 0.1), 2)
        self.me_optimal_for_current_cap = round(ceiling_precise(self.stats_magic_cap / min(1, self.em_goal_em / self.em_cr_cap), 10000), 2)
        self.me_optimal_for_current_bar = round(ceiling_precise(self.stats_magic_bar / min(1, self.em_goal_em / self.em_cr_bar), 1), 2)
        #   AMOUNT LEFT TO BUY
        self.me_amount_left_to_buy_power = self.me_optimal_for_current_power - self.stats_magic_power
        self.me_amount_left_to_buy_cap = self.me_optimal_for_current_cap - self.stats_magic_cap
        self.me_amount_left_to_buy_bar = self.me_optimal_for_current_bar - self.stats_magic_bar
        self.me_amount_left_to_buy_sum = self.me_amount_left_to_buy_power + self.me_amount_left_to_buy_cap + self.me_amount_left_to_buy_bar
        #   EXP COST
        self.me_exp_cost_power = self.me_amount_left_to_buy_power * 150
        self.me_exp_cost_cap = self.me_amount_left_to_buy_cap * 0.004
        self.me_exp_cost_bar = self.me_amount_left_to_buy_bar * 80