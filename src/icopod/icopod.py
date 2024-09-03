import math
from math import floor

from src.stats import Stats
from src.utils.ceiling_presice import ceiling_precise


class ICOPOD:
    def __init__(self, stats: Stats):
        self.stats = stats
        self.power = 1
        self.toughness = 1
        self.regen = 1
        self.hp = 1
        self.oneshot = 0
        self.final_pp_mod = 1   # 100%
        self.little_blue_pill_stack = 0
        self.kills_after_time_spent = 0     # TODO: calculate
        self.time_spent = 30                # In minutes
        self.time_to_respawn = 4.0

        self.ngu_level_magic_exp = stats.ngu_magic_exp
        self.ngu_level_energy_pp = stats.ngu_energy_pp
        self.update_floor_oneshot()
        self.update_max_floor()
        self.process_gains()


    def update_floor_oneshot(self):
        divisor = 637.5 / (1.25 if self.stats.spooky_set_bonus else 1)
        log_value = math.floor(math.log(self.power / divisor, 1.05))
        self.oneshot = max(0, math.floor(log_value))
        self.icopod_tier = 1 + floor(self.oneshot / 50)
        self.kills_per_ap_exp = max(20,40 - self.icopod_tier)

    def update_max_floor(self):
        divisor = 1.5 if self.stats.spooky_set_bonus else 1.2
        pow_floor = round(max(0.0, math.log((self.power * divisor / 10), 1.05) - 5))
        toughness_floor = round(max(0.0, math.log(self.toughness/10,1.05)))
        hp_floor = round(max(0.0, math.log(self.hp / 600, 1.05)))
        regen_floor = round(max(0.0, math.log(self.regen/10, 1.05)))
        avg_4 = round((pow_floor + toughness_floor + pow_floor + toughness_floor + hp_floor + regen_floor) / 6)
        self.max_floor = max(0, avg_4, self.oneshot)

    def process_gains(self):
        time_to_kill = (
            ceiling_precise(self.time_to_respawn, 0.02)
            + (0.8 if self.stats.maxed_sets['red_liquid'] else 1.0)
        )

        self.kills_after_time_spent = math.floor((self.time_spent * 60) / time_to_kill)
        gpp_per_kill_ = (
            ((700 if self.stats.is_evil else 200) + self.oneshot)
            * (12 if self.stats.maxed_sets['green_heart'] else 10 / 10)
            * (11 if self.stats.maxed_sets['pissed_off_key'] else 10 / 10)
            * (11 if self.stats.maxed_sets['ppp'] else 10 / 10)
            * self.final_pp_mod
                        )
        gpp_per_kill = math.floor(gpp_per_kill_)
        bonus_gpp_per_kill = math.floor(gpp_per_kill_ * 2.2 if self.stats.maxed_sets['blue_heart'] else 2) - gpp_per_kill
        self.max_kills_per_pp = math.ceil(1000000 / (gpp_per_kill + bonus_gpp_per_kill if self.little_blue_pill_stack >= self.kills_after_time_spent else  gpp_per_kill))
        self.time_to_get_one_pp = self.max_kills_per_pp * time_to_kill / 60
        self.time_to_get_one_ap_exp = self.kills_per_ap_exp * time_to_kill
        self.time_to_get_one_poop = 9000 * time_to_kill / 60
        kills_per_mcguf = (5000
                * (0.8 if self.stats.ictpod_perk_dict['Improved MacGuffin ITOPOD Drops I'] == 1 else 1)
                * (0.75 if self.stats.ictpod_perk_dict['Improved MacGuffin ITOPOD Drops II'] == 1 else 1)
                * (0.75 if self.stats.ictpod_perk_dict['Improved MacGuffin ITOPOD Drops III'] == 1 else 1)
                * (0.9 if self.stats.maxed_sets['purple_heart'] else 1)
        )
        print(kills_per_mcguf)
        self.time_to_get_one_mcguf = time_to_kill * kills_per_mcguf / 60
        self.time_to_get_one_boost = time_to_kill / 0.16


