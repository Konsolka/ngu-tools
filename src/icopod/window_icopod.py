from PySide6.QtCore import Slot

from src.icopod.icopod import ICOPOD
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
        self.ui.edit_power.returnPressed.connect(lambda: self.ui_upade_stats_type('power'))
        self.ui.edit_toughness.returnPressed.connect(lambda: self.ui_upade_stats_type('toughness'))
        self.ui.edit_hp_regen.returnPressed.connect(lambda: self.ui_upade_stats_type('hp_regen'))
        self.ui.edit_hp.returnPressed.connect(lambda: self.ui_upade_stats_type('hp'))
        self.ui.edit_minutes_spent.returnPressed.connect(self.ui_update_time_spent)

    @Slot()
    def ui_upade_stats_type(self, type_):
        sender = self.sender()
        if type_ == 'power':
            self.icopod.power = int(self.ui.edit_power.text())
        elif type_ == 'toughness':
            self.icopod.toughness = int(self.ui.edit_toughness.text())
        elif type_ == 'hp_regen':
            self.icopod.regen = int(self.ui.edit_hp_regen.text())
        elif type_ == 'hp':
            self.icopod.hp = int(self.ui.edit_hp.text())
        self.update_all()

    def update_gains(self):
        self.ui.max_kills_need.setText(str(self.icopod.max_kills_per_pp))
        self.ui.kills_aftes_time_spent.setText(str(self.icopod.kills_after_time_spent))


    def ui_update_time_spent(self):
        self.icopod.time_spent = int(self.ui.edit_minutes_spent.text())
        self.icopod.process_gains()
        self.update_gains()