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

    # def update_stats(self):
