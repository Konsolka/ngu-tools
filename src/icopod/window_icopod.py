from PySide6.QtCore import Slot

from src.icopod.icopod import ICOPOD
from src.utils.misc import more_then_60
from ui.icopod_ui import Ui_icopod_window

from PySide6.QtWidgets import QWidget

from src.stats import Stats


def get_time_and_format(value, time_switch):
    unit = time_switch[1] if more_then_60(value) else time_switch[0]
    time_value = value / 60 if unit == time_switch[1] else value
    if unit == time_switch[0]:
        return f'{time_value:.1f}{unit}'
    return f'{time_value:.2f}{unit}'


class WindowIcopod(QWidget):
    def __init__(self, stats: Stats):
        super(WindowIcopod, self).__init__()
        self.ui = Ui_icopod_window()
        self.ui.setupUi(self)
        self.stats = stats
        self.icopod = ICOPOD(self.stats)
        self.ui_connect()
        self.update_all()

    def update_all(self):
        self.icopod.update_floor_oneshot()
        self.ui.oneshot_floor.setText(str(self.icopod.oneshot))
        self.ui.tier.setText('Tier ' + str(self.icopod.icopod_tier))
        self.ui.kills_per_ap_exp.setText('{} Kills'.format(self.icopod.kills_per_ap_exp))
        self.icopod.update_max_floor()
        self.ui.max_floor.setText(str(self.icopod.max_floor))
        self.icopod.process_gains()
        self.update_gains()
        self.icopod.update_enemy_stat_checker()
        self.ui_update_enemy_stat_checker()

    def ui_connect(self):
        self.ui.edit_power.returnPressed.connect(lambda: self.update_stats_from_ui('power'))
        self.ui.edit_toughness.returnPressed.connect(lambda: self.update_stats_from_ui('toughness'))
        self.ui.edit_hp_regen.returnPressed.connect(lambda: self.update_stats_from_ui('hp_regen'))
        self.ui.edit_hp.returnPressed.connect(lambda: self.update_stats_from_ui('hp'))
        self.ui.edit_minutes_spent.returnPressed.connect(self.ui_update_time_spent)
        self.ui.edit_floor.returnPressed.connect(self.ui_update_enemy_stat_checker)

    @Slot()
    def update_stats_from_ui(self, stat_type):
        stat_value = int(getattr(self.ui, f"edit_{stat_type}").text())
        setattr(self.icopod, stat_type, stat_value)
        self.update_all()

    def ui_update_enemy_stat_checker(self):
        self.icopod.enemy_stat_level = int(self.ui.edit_floor.text())
        self.icopod.update_enemy_stat_checker()
        self.update_enemy_stat_checker()

    def update_gains(self):
        self.ui.max_kills_need.setText(str(self.icopod.max_kills_per_pp))
        self.ui.kills_aftes_time_spent.setText(str(self.icopod.kills_after_time_spent))
        hour_switch = 'h' if self.icopod.time_spent > 60 else 'm'
        self.ui.pp_per_time.setText('PP Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.ap_per_time.setText('AP Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.exp_per_time.setText('EXP Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.poop_per_time.setText('Poop Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.mcguf_per_time.setText('MacGuffins Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.boost_per_time.setText('Boost Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.time_to_pp.setText(get_time_and_format(self.icopod.time_to_get_one_pp, ['m', 'h']))
        self.ui.time_to_ap_exp.setText(get_time_and_format(self.icopod.time_to_get_one_ap_exp, ['s', 'm']))
        self.ui.time_to_poop.setText(get_time_and_format(self.icopod.time_to_get_one_poop, ['m', 'h']))
        self.ui.time_to_mcguf.setText(get_time_and_format(self.icopod.time_to_get_one_mcguf, ['m', 'h']))
        self.ui.time_to_boost.setText(get_time_and_format(self.icopod.time_to_get_one_boost, ['s', 'm']))
        self.ui.pp_per.setText(f'{self.icopod.pp_per_time} PP')
        self.ui.ap_per.setText(f'{self.icopod.ap_per_time} AP')
        self.ui.exp_per.setText(f'{self.icopod.exp_per_time} EXP')
        self.ui.poop_per.setText(f'{self.icopod.poop_per_time} Poop')
        self.ui.mcguf_per.setText(f'{self.icopod.mcguf_per_time} MacGuffins')
        self.ui.boost_per.setText(f'{self.icopod.boost_per_time :.2f} Boost')

    def update_enemy_stat_checker(self):
        self.ui.enemy_power.setText(str(self.icopod.enemy_stat_power))
        self.ui.enemy_toughness.setText(str(self.icopod.enemy_stat_toughness))
        self.ui.enemy_hp_regen.setText(str(self.icopod.enemy_stat_regen))
        self.ui.enemy_hp.setText(str(self.icopod.enemy_stat_hp))
        self.ui.oneshot_power.setText(str(self.icopod.power_to_oneshot_enemy))

    def ui_update_time_spent(self):
        self.icopod.time_spent = int(self.ui.edit_minutes_spent.text())
        self.icopod.process_gains()
        self.update_gains()
