from PySide6.QtCore import Slot

from src.icopod.icopod import ICOPOD
from src.utils.misc import more_then_60
from ui.icopod_ui import Ui_Form as ICTPOD_ui

from PySide6.QtWidgets import QWidget

import ui.icopod_ui
from src.stats import Stats


class WindowIcopod(QWidget):
    def __init__(self, stats: Stats):
        super(WindowIcopod, self).__init__()
        self.ui = ICTPOD_ui()
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

    def ui_connect(self):
        self.ui.edit_power.returnPressed.connect(lambda: self.update_stats_from_ui('power'))
        self.ui.edit_toughness.returnPressed.connect(lambda: self.update_stats_from_ui('toughness'))
        self.ui.edit_hp_regen.returnPressed.connect(lambda: self.update_stats_from_ui('hp_regen'))
        self.ui.edit_hp.returnPressed.connect(lambda: self.update_stats_from_ui('hp'))
        self.ui.edit_minutes_spent.returnPressed.connect(self.ui_update_time_spent)

    @Slot()
    def update_stats_from_ui(self, stat_type):
        stat_value = int(getattr(self.ui, f"edit_{stat_type}").text())
        setattr(self.icopod, stat_type, stat_value)
        self.update_all()

    def update_gains(self):
        self.ui.max_kills_need.setText(str(self.icopod.max_kills_per_pp))
        self.ui.kills_aftes_time_spent.setText(str(self.icopod.kills_after_time_spent))
        hour_switch = 'h' if self.icopod.time_spent > 60 else 'm'
        self.ui.pp_per_time.setText('PP Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.ap_exp_per_time.setText('AP/EXP Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.poop_per_time.setText('Poop Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.mcguf_per_time.setText('MacGuffins Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.boost_per_time.setText('Boost Per {}{} :O'.format(self.icopod.time_spent, hour_switch))
        self.ui.pp_per.setText('{:.2f}{}'.format(self.icopod.time_to_get_one_pp, 'h' if more_then_60(self.icopod.time_to_get_one_pp) else 'm'))
        self.ui.ap_exp_per.setText('{:.2f}{}'.format(self.icopod.time_to_get_one_ap_exp, 'm' if more_then_60(self.icopod.time_to_get_one_ap_exp) else 's'))
        self.ui.poop_per.setText('{:.2f}{}'.format(self.icopod.time_to_get_one_poop, 'h' if more_then_60(self.icopod.time_to_get_one_poop) else 'm'))
        self.ui.mcguf_per.setText('{:.2f}{}'.format(self.icopod.time_to_get_one_mcguf, 'h' if more_then_60(self.icopod.time_to_get_one_mcguf) else 'm'))
        self.ui.boost_per.setText('{:.2f}{}'.format(self.icopod.time_to_get_one_boost, 'm' if more_then_60(self.icopod.time_to_get_one_boost) else 's'))


    def ui_update_time_spent(self):
        self.icopod.time_spent = int(self.ui.edit_minutes_spent.text())
        self.icopod.process_gains()
        self.update_gains()