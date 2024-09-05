from src.icopod.window_icopod import WindowIcopod
from src.ratioz.window_ratios import WindowRatios
from ui.ngu_helper_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QTabWidget
from handler import Handler

from src.stats import Stats

class TabWidget(QTabWidget):
    def __init__(self, icopod:WindowIcopod, ratios:WindowRatios):
        super(TabWidget, self).__init__()

        self.addTab(icopod, "Icopod")
        self.addTab(ratios, "Ratios")

class MainWindow(QMainWindow):
    def __init__(self, handler:Handler):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handler_ref = handler

        self.stats = Stats(handler)
        self.ratios = WindowRatios(self.stats)
        self.icopod = WindowIcopod(self.stats)
        layout = QHBoxLayout()
        tabs = TabWidget(self.icopod, self.ratios)

        layout.addWidget(tabs)

        self.ui.centralwidget.setLayout(layout)

    def switch_window(self):
        pass
