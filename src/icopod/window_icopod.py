from src.ratioz.ratioz import Ratios
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
        self.ratios = Ratios(self.stats)
        self.update_stats()

    def update_stats(self):
        self.ui.power.setText(str(self.stats.power))
        self.ui.toughness.setText(str(self.stats.toughness))
        self.ui.hp.setText(str(self.stats.hp))
        self.ui.hp_regen.setText(str(self.stats.regen))