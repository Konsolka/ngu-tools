from PySide6.QtCore import QRect

from src.ratioz.window_ratios import WindowRatios
from ui.ngu_helper_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QHBoxLayout
from handler import Handler

from src.stats import Stats


class MainWindow(QMainWindow):
    def __init__(self, handler:Handler):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handler_ref = handler

        self.stats = Stats(handler)
        self.ratios = WindowRatios(self.stats)
        layout = QHBoxLayout()

        layout.addWidget(self.ratios)
        self.ui.centralwidget.setLayout(layout)

    def switch_window(self):
        pass
