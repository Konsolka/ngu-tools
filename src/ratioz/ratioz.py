import math

from src.utils.logger import logger
from src.stats import Stats
from src.utils.ceiling_presice import ceiling_precise


class Ratios:
    def __init__(self, stats:Stats):
        self.stats_energy_base_power = stats.energy_base_power
        self.stats_energy_base_cap = stats.energy_base_cap
        self.stats_energy_base_bar = stats.energy_base_bar

        self.stats_magic_base_power = stats.magicPower
        self.stats_magic_base_cap = stats.magicCap
        self.stats_magic_base_bar = stats.magicBar

        self.stats_r3_base_power = stats.r3_base_power
        self.stats_r3_base_cap = stats.r3_base_cap
        self.stats_r3_base_bar = stats.r3_base_bar

        self.update_all()

    def update_all(self):
        self.update_type(1, 37500, 1, 'energy')
        self.update_type(1, 40000, 1, 'magic')
        self.update_type(1, 40000, 1, 'r3')
        self.update_em()
        self.update_me()
        self.update_er3()

    def update_type(self, power, cap, bar, type_):
        #   CURRENT RATIO
        setattr(self, f'{type_}_current_ratio_power', 1.0)
        setattr(self, f'{type_}_current_ratio_cap', int(getattr(self, f'stats_{type_}_base_cap') / getattr(self, f'stats_{type_}_base_power')))
        setattr(self, f'{type_}_current_ratio_bar', round(getattr(self, f'stats_{type_}_base_bar') / getattr(self, f'stats_{type_}_base_power'), 2))
        #   GOAL RATIO / TEXT INPUT
        setattr(self, f'{type_}_edit_power', power)
        setattr(self, f'{type_}_edit_cap', cap)
        setattr(self, f'{type_}_edit_bar', bar)
        current_goal_ratio_power = 1
        current_goal_ratio_cap = getattr(self, f'stats_{type_}_base_cap') / getattr(self, f'{type_}_edit_cap') / getattr(self, f'stats_{type_}_base_power') * getattr(self, f'{type_}_edit_power')
        current_goal_ratio_bar = getattr(self, f'stats_{type_}_base_bar') / getattr(self, f'{type_}_edit_bar') / getattr(self, f'stats_{type_}_base_power') * getattr(self, f'{type_}_edit_power')
        max_of_current_goal_ratio = max(current_goal_ratio_power, current_goal_ratio_cap, current_goal_ratio_bar)
        #   BASE GOAL
        setattr(self, f'{type_}_base_goal_power', ceiling_precise(getattr(self, f'stats_{type_}_base_power') * max_of_current_goal_ratio, 0.01))
        setattr(self, f'{type_}_base_goal_cap', ceiling_precise(getattr(self, f'{type_}_base_goal_power') / getattr(self, f'{type_}_edit_power') * getattr(self, f'{type_}_edit_cap'), 250))
        setattr(self, f'{type_}_base_goal_bar', math.ceil(getattr(self, f'{type_}_base_goal_power') / getattr(self, f'{type_}_edit_power') * getattr(self, f'{type_}_edit_bar')))
        # AMOUNT LEFT TO BUY
        setattr(self, f'{type_}_amount_left_to_buy_power', getattr(self, f'{type_}_base_goal_power') - getattr(self, f'stats_{type_}_base_power'))
        setattr(self, f'{type_}_amount_left_to_buy_cap', getattr(self, f'{type_}_base_goal_cap') - getattr(self, f'stats_{type_}_base_cap'))
        setattr(self, f'{type_}_amount_left_to_buy_bar', getattr(self, f'{type_}_base_goal_bar') - getattr(self, f'stats_{type_}_base_bar'))
        # EXP COST
        exp_cost_value = self.type_exp_cost(type_)
        setattr(self, f'{type_}_exp_cost_power', getattr(self, f'{type_}_amount_left_to_buy_power') * exp_cost_value[0])
        setattr(self, f'{type_}_exp_cost_cap', getattr(self, f'{type_}_amount_left_to_buy_cap') * exp_cost_value[1])
        setattr(self, f'{type_}_exp_cost_bar', getattr(self, f'{type_}_amount_left_to_buy_bar') * exp_cost_value[2])
        #   TOTAL EXP COST
        setattr(self, f'{type_}_amount_left_to_buy_sum', getattr(self, f'{type_}_exp_cost_bar') + getattr(self, f'{type_}_exp_cost_power') + getattr(self, f'{type_}_exp_cost_cap'))

    def type_exp_cost(self, type_):
        if type_ == 'energy':
            return [150, 0.004, 80]
        elif type_ == 'magic':
            return [450, 0.012, 240]
        elif type_ == 'r3':
            return [15000000, 400, 8000000]

    def update_em(self, em_energy = 6.0, em_magic = 2.0):
        #   GOAL ENERGY MAGIC
        self.em_goal_em = em_energy / em_magic
        #   CURRENT ENERGY:MAGIC RATIO
        self.em_cr_power = self.stats_energy_base_power / self.stats_magic_base_power
        self.em_cr_cap = self.stats_energy_base_cap / self.stats_magic_base_cap
        self.em_cr_bar = self.stats_energy_base_bar / self.stats_magic_base_bar
        #   OPTIMAL ENERGY FOR MAGIC AT RATIO
        self.em_optimal_for_current_power = self.stats_energy_base_power * max(1, self.em_goal_em / self.em_cr_power)
        self.em_optimal_for_current_cap = self.stats_energy_base_cap * max(1, self.em_goal_em / self.em_cr_cap)
        self.em_optimal_for_current_bar = self.stats_energy_base_bar * max(1, self.em_goal_em / self.em_cr_bar)
        #   AMOUNT LEFT TO BUY
        self.em_amount_left_to_buy_power = self.em_optimal_for_current_power - self.stats_energy_base_power
        self.em_amount_left_to_buy_cap = self.em_optimal_for_current_cap - self.stats_energy_base_cap
        self.em_amount_left_to_buy_bar = self.em_optimal_for_current_bar - self.stats_energy_base_bar
        self.em_amount_left_to_buy_sum = self.em_amount_left_to_buy_power + self.em_amount_left_to_buy_cap + self.em_amount_left_to_buy_bar
        #   EXP COST
        self.em_exp_cost_power = self.em_amount_left_to_buy_power * 150
        self.em_exp_cost_cap = self.em_amount_left_to_buy_cap * 0.004
        self.em_exp_cost_bar = self.em_amount_left_to_buy_bar * 80

    def update_me(self, em_energy = 6.0, em_magic = 2.0):
        #   GOAL MAGIC ENERGY
        self.em_goal_em = em_energy / em_magic
        #   OPTIMAL ENERGY FOR MAGIC AT RATIO
        self.me_optimal_for_current_power = round(ceiling_precise(self.stats_magic_base_power / min(1, self.em_goal_em / self.em_cr_power), 0.1), 2)
        self.me_optimal_for_current_cap = round(ceiling_precise(self.stats_magic_base_cap / min(1, self.em_goal_em / self.em_cr_cap), 10000), 2)
        self.me_optimal_for_current_bar = round(ceiling_precise(self.stats_magic_base_bar / min(1, self.em_goal_em / self.em_cr_bar), 1), 2)
        #   AMOUNT LEFT TO BUY
        self.me_amount_left_to_buy_power = self.me_optimal_for_current_power - self.stats_magic_base_power
        self.me_amount_left_to_buy_cap = self.me_optimal_for_current_cap - self.stats_magic_base_cap
        self.me_amount_left_to_buy_bar = self.me_optimal_for_current_bar - self.stats_magic_base_bar
        self.me_amount_left_to_buy_sum = self.me_amount_left_to_buy_power + self.me_amount_left_to_buy_cap + self.me_amount_left_to_buy_bar
        #   EXP COST
        self.me_exp_cost_power = self.me_amount_left_to_buy_power * 450
        self.me_exp_cost_cap = self.me_amount_left_to_buy_cap * 0.012
        self.me_exp_cost_bar = self.me_amount_left_to_buy_bar * 240

    def update_er3(self, energy = 100000, r3 = 1):
        #   GOAL ENERGY R3
        self.er3_goal_er3 = energy / r3 if r3 != 0 else float('inf')
        #   CURRENT ENERGY : R3 RATIO
        self.er3_cr_power = (
            self.stats_energy_base_power / self.stats_r3_base_power
            if self.stats_r3_base_power != 0
            else float('inf')
        )
        self.er3_cr_cap = (
            self.stats_energy_base_cap / self.stats_r3_base_cap
            if self.stats_r3_base_cap != 0
            else float('inf')
        )
        self.er3_cr_bar = (
            self.stats_energy_base_bar / self.stats_r3_base_bar
                if self.stats_r3_base_bar != 0
            else float('inf')
        )

        self.er3_edit_energy = energy
        self.er3_edit_r3 = r3
        #   OPTIMAL R3 FOR ENERGY AT RATIO
        self.er3_optimal_for_current_power = round(ceiling_precise(self.stats_r3_base_power / max(1, self.er3_goal_er3 / self.er3_cr_power), 0.1), 2)
        self.er3_optimal_for_current_cap = self.stats_r3_base_cap / max(1, self.er3_goal_er3 / self.er3_cr_cap)
        self.er3_optimal_for_current_bar = self.stats_r3_base_bar / max(1, self.er3_goal_er3 / self.er3_cr_bar)
        #   AMOUNT LEFT TO BUY
        self.er3_amount_left_to_buy_power = 0 if self.er3_optimal_for_current_power - self.stats_r3_base_power < 1.0 else self.er3_optimal_for_current_power - self.stats_r3_base_power
        self.er3_amount_left_to_buy_cap = self.er3_optimal_for_current_cap - self.stats_r3_base_cap
        self.er3_amount_left_to_buy_bar = self.er3_optimal_for_current_bar - self.stats_r3_base_bar
        #   EXP COST
        self.er3_exp_cost_power = self.er3_amount_left_to_buy_power * 15000000
        self.er3_exp_cost_cap = self.er3_amount_left_to_buy_cap * 400
        self.er3_exp_cost_bar = self.er3_amount_left_to_buy_bar * 8000000
        self.er3_amount_left_to_buy_sum = self.er3_exp_cost_power + self.er3_exp_cost_cap + self.er3_exp_cost_bar
