from PySide6.QtCore import Slot, QTimer

from ngu_helper_ui import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
from handler import Handler
from ratioz import Ratios
from stats import Stats


def return_c_for_cr(number):
    return '↑' if number > 1.0 else '↓' if number < 1.0 else '~'

def return_color_for_cr(number):
    red = 'background-color:rgb(234, 153, 153);'
    green = 'background-color:green'
    return red if number > 1.0 else red if number < 1.0 else green

class MainWindow(QMainWindow):
    def __init__(self, handler:Handler):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.handler_ref = handler
        self.stats = Stats(handler)
        self.ratios = Ratios(self.stats)
        #ENERGY
        self.draw_energy_ratio()
        #   TEXT INPUT
        self.ui.energy_goal_edit_power.returnPressed.connect(self.update_energy_goal_edit)
        self.ui.energy_goal_edit_cap.returnPressed.connect(self.update_energy_goal_edit)
        self.ui.energy_goal_edit_bar.returnPressed.connect(self.update_energy_goal_edit)
        #   BUTTONS
        self.ui.energy_amount_left_to_buy_power.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)
        self.ui.energy_amount_left_to_buy_cap.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)
        self.ui.energy_amount_left_to_buy_bar.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)

        #MAGIC
        self.draw_magic_ratio()
        #   TEXT INPUT
        self.ui.magic_goal_edit_power.returnPressed.connect(self.update_magic_goal_edit)
        self.ui.magic_goal_edit_cap.returnPressed.connect(self.update_magic_goal_edit)
        self.ui.magic_goal_edit_bar.returnPressed.connect(self.update_magic_goal_edit)

        #   BUTTONS
        self.ui.magic_amount_left_to_buy_power.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)
        self.ui.magic_amount_left_to_buy_cap.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)
        self.ui.magic_amount_left_to_buy_bar.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)
        #R3
        self.draw_r3_ratio()
        #   TEXT INPUT
        self.ui.r3_goal_edit_power.returnPressed.connect(self.update_r3_goal_edit)
        self.ui.r3_goal_edit_cap.returnPressed.connect(self.update_r3_goal_edit)
        self.ui.r3_goal_edit_bar.returnPressed.connect(self.update_r3_goal_edit)

        #   BUTTONS
        self.ui.r3_amount_left_to_buy_power.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)
        self.ui.r3_amount_left_to_buy_cap.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)
        self.ui.r3_amount_left_to_buy_bar.clicked.connect(self.copy_to_clipboard_amount_left_to_buy)

    def draw_energy_ratio(self):
        #   BASE
        self.ui.base_e_pow.setText(str(self.stats.energy_base_power))
        self.ui.base_e_cap.setText(str(self.stats.energy_base_cap))
        self.ui.base_e_bar.setText(str(self.stats.energy_base_bars))
        #   CURRENT RATIO
        self.ui.CER_power.setText(str(self.ratios.current_energy_ratio_power))
        self.ui.CER_cap.setText(str(self.ratios.current_energy_ratio_cap))
        self.ui.CER_bars.setText(str(self.ratios.current_energy_ratio_bars))
        #   BASE GOAL
        self.ui.energy_base_goal_power.setText(str(self.ratios.energy_base_goal_power))
        self.ui.energy_base_goal_cap.setText(str(self.ratios.energy_base_goal_cap))
        self.ui.energy_base_goal_bar.setText(str(self.ratios.energy_base_goal_bars))
        #   AMOUNT LEFT TO BUY
        #       IN GAME VALUES
        self.ui.energy_amount_left_to_buy_power.setText(str(self.ratios.amount_left_to_buy_power))
        self.ui.energy_amount_left_to_buy_cap.setText(str(self.ratios.amount_left_to_buy_cap))
        self.ui.energy_amount_left_to_buy_bar.setText(str(self.ratios.amount_left_to_buy_bars))

        #       PRICE FOR THAT
        self.ui.energy_exp_cost_power.setText("{} EXP".format(int(self.ratios.energy_exp_cost_power)))
        self.ui.energy_exp_cost_cap.setText("{} EXP".format(int(self.ratios.energy_exp_cost_cap)))
        self.ui.energy_exp_cost_bars.setText("{} EXP".format(int(self.ratios.energy_exp_cost_bar)))
        self.ui.amount_left_to_buy_energy.setText(
            "Amount Left To Buy Until Your Energy Goal\n(Total Cost: {} EXP)".format(
                int(self.ratios.amount_left_to_buy_sum)))
        #   COLORS CHECKER
        self.ui.energy_CR_power_checker.setText('~')
        self.ui.energy_CR_power_checker.setStyleSheet(return_color_for_cr(1))
        self.ui.energy_CR_cap_checker.setText(return_c_for_cr(self.ratios.current_goal_energy_ratio_cap))
        self.ui.energy_CR_cap_checker.setStyleSheet(return_color_for_cr(self.ratios.current_goal_energy_ratio_cap))
        self.ui.energy_CR_bar_checker.setText(return_c_for_cr(self.ratios.current_goal_energy_ratio_bar))
        self.ui.energy_CR_bar_checker.setStyleSheet(return_color_for_cr(self.ratios.current_goal_energy_ratio_bar))


    def draw_magic_ratio(self):
        #   BASE STAT
        self.ui.base_m_pow.setText(str(self.stats.magicPower))
        self.ui.base_m_cap.setText(str(self.stats.magicCap))
        self.ui.base_m_bar.setText(str(self.stats.magicBar))
        #   CURRENT RATIO
        self.ui.CMR_power.setText(str(self.ratios.current_magic_ratio_power))
        self.ui.CMR_cap.setText(str(self.ratios.current_magic_ratio_cap))
        self.ui.CMR_bars.setText(str(self.ratios.current_magic_ratio_bars))
        #   BASE GOAL
        self.ui.magic_base_goal_power.setText(str(self.ratios.magic_base_goal_power))
        self.ui.magic_base_goal_cap.setText(str(self.ratios.magic_base_goal_cap))
        self.ui.magic_base_goal_bar.setText(str(self.ratios.magic_base_goal_bars))
        #   AMOUNT LEFT TO BUY
        #       IN GAME VALUES
        self.ui.magic_amount_left_to_buy_power.setText(str(self.ratios.magic_amount_left_to_buy_power))
        self.ui.magic_amount_left_to_buy_cap.setText(str(self.ratios.magic_amount_left_to_buy_cap))
        self.ui.magic_amount_left_to_buy_bar.setText(str(self.ratios.magic_amount_left_to_buy_bars))
        #       PRICE FOR THAT
        self.ui.magic_exp_cost_power.setText("{} EXP".format(int(self.ratios.magic_exp_cost_power)))
        self.ui.magic_exp_cost_cap.setText("{} EXP".format(int(self.ratios.magic_exp_cost_cap)))
        self.ui.magic_exp_cost_bars.setText("{} EXP".format(int(self.ratios.magic_exp_cost_bar)))
        self.ui.name_magic_amount_left_to_buy.setText(
            "Amount Left To Buy Until Your Magic Goal\n(Total Cost: {} EXP)".format(
                int(self.ratios.magic_amount_left_to_buy_sum)))
        #   COLORS CHECKER
        self.ui.magic_CR_power_checker.setText('~')
        self.ui.magic_CR_power_checker.setStyleSheet(return_color_for_cr(1))
        self.ui.magic_CR_cap_checker.setText(return_c_for_cr(self.ratios.current_goal_magic_ratio_cap))
        self.ui.magic_CR_cap_checker.setStyleSheet(return_color_for_cr(self.ratios.current_goal_magic_ratio_cap))
        self.ui.magic_CR_bar_checker.setText(return_c_for_cr(self.ratios.current_goal_magic_ratio_bar))
        self.ui.magic_CR_bar_checker.setStyleSheet(return_color_for_cr(self.ratios.current_goal_magic_ratio_bar))

    def draw_r3_ratio(self):
        #   BASE
        self.ui.r3_base_power.setText(str(self.stats.r3_base_power))
        self.ui.r3_base_cap.setText(str(self.stats.r3_base_cap))
        self.ui.r3_base_bar.setText(str(self.stats.r3_base_bar))
        #   CURRENT RATIO
        self.ui.r3_cr_power.setText(str(self.ratios.r3_current_ratio_power))
        self.ui.r3_cr_cap.setText(str(self.ratios.r3_current_ratio_cap))
        self.ui.r3_cr_bars.setText(str(self.ratios.r3_current_ratio_bars))
        #   BASE GOAL
        self.ui.r3_base_goal_power.setText(str(self.ratios.r3_base_goal_power))
        self.ui.r3_base_goal_cap.setText(str(self.ratios.r3_base_goal_cap))
        self.ui.r3_base_goal_bar.setText(str(self.ratios.r3_base_goal_bars))
        #   AMOUNT LEFT TO BUY
        #       IN GAME VALUES
        self.ui.r3_amount_left_to_buy_power.setText(str(self.ratios.r3_amount_left_to_buy_power))
        self.ui.r3_amount_left_to_buy_cap.setText(str(self.ratios.r3_amount_left_to_buy_cap))
        self.ui.r3_amount_left_to_buy_bar.setText(str(self.ratios.r3_amount_left_to_buy_bars))

        #       PRICE FOR THAT
        self.ui.r3_exp_cost_power.setText("{} EXP".format(int(self.ratios.r3_exp_cost_power)))
        self.ui.r3_exp_cost_cap.setText("{} EXP".format(int(self.ratios.r3_exp_cost_cap)))
        self.ui.r3_exp_cost_bars.setText("{} EXP".format(int(self.ratios.r3_exp_cost_bar)))
        self.ui.name_r3_amount_left_to_buy.setText(
            "Amount Left To Buy Until Your R3 Goal\n(Total Cost: {} EXP)".format(
                int(self.ratios.r3_amount_left_to_buy_sum)))
        #   COLORS CHECKER
        self.ui.r3_cr_power_checker.setText('~')
        self.ui.r3_cr_power_checker.setStyleSheet(return_color_for_cr(1))
        self.ui.r3_cr_cap_checker.setText(return_c_for_cr(self.ratios.r3_current_goal_ratio_cap))
        self.ui.r3_cr_cap_checker.setStyleSheet(return_color_for_cr(self.ratios.r3_current_goal_ratio_cap))
        self.ui.r3_cr_bar_checker.setText(return_c_for_cr(self.ratios.r3_current_goal_ratio_bar))
        self.ui.r3_cr_bar_checker.setStyleSheet(return_color_for_cr(self.ratios.r3_current_goal_ratio_bar))

    def init_ratios(self):
        self.draw_energy_ratio()
        self.draw_magic_ratio()
        self.draw_r3_ratio()

    @Slot()
    def copy_to_clipboard_amount_left_to_buy(self):
        sender = self.sender()
        text = str(int(float(sender.text())))
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QToolTip.showText(sender.mapToGlobal(sender.rect().center()), "Copied!")
        QTimer.singleShot(1500, QToolTip.hideText)

    def update_energy_goal_edit(self):
        energy_power = float(self.ui.energy_goal_edit_power.text())
        energy_cap = float(self.ui.energy_goal_edit_cap.text())
        energy_bar = float(self.ui.energy_goal_edit_bar.text())
        self.ratios.update_energy(energy_power, energy_cap, energy_bar)
        self.draw_energy_ratio()

    def update_magic_goal_edit(self):
        magic_power = float(self.ui.magic_goal_edit_power.text())
        magic_cap = float(self.ui.magic_goal_edit_cap.text())
        magic_bar = float(self.ui.magic_goal_edit_bar.text())
        self.ratios.update_magic(magic_power, magic_cap, magic_bar)
        self.draw_magic_ratio()

    def update_r3_goal_edit(self):
        r3_power = float(self.ui.r3_goal_edit_power.text())
        r3_cap = float(self.ui.r3_goal_edit_cap.text())
        r3_bar = float(self.ui.r3_goal_edit_bar.text())
        self.ratios.update_r3(r3_power, r3_cap, r3_bar)
        self.draw_r3_ratio()