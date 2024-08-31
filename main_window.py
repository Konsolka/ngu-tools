from ngu_helper_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from handler import Handler
from ratioz import Ratios
from stats import Stats


class MainWindow(QMainWindow):
    def __init__(self, handler:Handler):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handler_ref = handler
        self.stats = Stats(handler)
        self.ratios = Ratios(self.stats)

    def init_ratios(self):
        self.ui.base_e_pow.setText(str(self.stats.energyPower))
        self.ui.base_e_cap.setText(str(self.stats.capEnergy))
        self.ui.base_e_bar.setText(str(self.stats.energyBars))
        self.ui.CER_power.setText(str(self.ratios.current_energy_ratio_power))
        self.ui.CER_cap.setText(str(self.ratios.current_energy_ratio_cap))
        self.ui.CER_bars.setText(str(self.ratios.current_energy_ratio_bars))
        self.ui.energy_base_goal_power.setText(str(self.ratios.energy_base_goal_power))
        self.ui.energy_base_goal_cap.setText(str(self.ratios.energy_base_goal_cap))
        self.ui.energy_base_goal_bar.setText(str(self.ratios.energy_base_goal_bars))
        self.ui.energy_amount_left_to_buy_pow.setText(str(self.ratios.amount_left_to_buy_power))
        self.ui.energy_amount_left_to_buy_cap.setText(str(self.ratios.amount_left_to_buy_cap))
        self.ui.energy_amount_left_to_buy_bars.setText(str(self.ratios.amount_left_to_buy_bars))
        self.ui.energy_exp_cost_power.setText("{} EXP".format(int(self.ratios.energy_exp_cost_power)))
        self.ui.energy_exp_cost_cap.setText("{} EXP".format(int(self.ratios.energy_exp_cost_cap)))
        self.ui.energy_exp_cost_bars.setText("{} EXP".format(int(self.ratios.energy_exp_cost_bar)))
        self.ui.amount_left_to_buy_energy.setText("Amount Left To Buy Until Your Energy Goal\n(Total Cost: {} EXP)".format(int(self.ratios.amount_left_to_buy_sum)))