from PySide6.QtCore import Slot, QTimer
from PySide6.QtWidgets import QWidget, QApplication, QToolTip

from src.ratioz.ratioz import Ratios
from src.stats import Stats
from ui.ratios_ui import Ui_Form


def return_c_for_cr(number):
    return '↑' if number > 1.0 else '↓' if number < 1.0 else '~'


def return_color_for_cr(number):
    """Return green if number is 1, red otherwise"""
    return "background-color:green" if number == 1 else "background-color:rgb(234, 153, 153)"


class WindowRatios(QWidget):
    def __init__(self, stats: Stats):
        super(WindowRatios, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.stats = stats
        self.ratios = Ratios(self.stats)
        # ENERGY
        self.draw_type_ratio('energy')
        self.ui_setup_connections('energy')

        # MAGIC
        self.draw_type_ratio('magic')
        self.ui_setup_connections('magic')

        # R3
        self.draw_type_ratio('r3')
        self.ui_setup_connections('r3')

        # ENERGY : MAGIC
        self.draw_em_ratio()
        self.ui_setup_connections('em')

        # MAGIC : ENERGY
        self.draw_me_ratio()
        self.ui_setup_connections('me')

        # ENERGY : R3
        self.draw_er3_ratio()
        self.ui_setup_connections('er3')

    def ui_setup_connections(self, category_):
        # Connect text inputs
        if category_ != 'me':
            if category_ == 'em':
                self.ui.em_edit_goal_ratio_energy.returnPressed.connect(self.update_em_goal_edit)
                self.ui.em_edit_goal_ratio_magic.returnPressed.connect(self.update_em_goal_edit)
            elif category_ == 'er3':
                self.ui.er3_edit_goal_ratio_energy.returnPressed.connect(self.update_er3_goal_edit)
                self.ui.er3_edit_goal_ratio_r3.returnPressed.connect(self.update_er3_goal_edit)
            else:
                getattr(self.ui, f"{category_}_goal_edit_power").returnPressed.connect(
                    lambda: self.update_goal_edit(category_))
                getattr(self.ui, f"{category_}_goal_edit_cap").returnPressed.connect(
                    lambda: self.update_goal_edit(category_))
                getattr(self.ui, f"{category_}_goal_edit_bar").returnPressed.connect(
                    lambda: self.update_goal_edit(category_))

        # Connect buttons
        getattr(self.ui, f"{category_}_amount_left_to_buy_power").clicked.connect(
            self.copy_to_clipboard_amount_left_to_buy)
        getattr(self.ui, f"{category_}_amount_left_to_buy_cap").clicked.connect(
            self.copy_to_clipboard_amount_left_to_buy)
        getattr(self.ui, f"{category_}_amount_left_to_buy_bar").clicked.connect(
            self.copy_to_clipboard_amount_left_to_buy)

    def draw_type_ratio(self, type_):
        # BASE
        getattr(self.ui, f"{type_}_base_power").setText(str(getattr(self.ratios, f"stats_{type_}_base_power")))
        getattr(self.ui, f"{type_}_base_cap").setText(str(getattr(self.ratios, f"stats_{type_}_base_cap")))
        getattr(self.ui, f"{type_}_base_bar").setText(str(getattr(self.ratios, f"stats_{type_}_base_bar")))
        # CURRENT RATIO
        getattr(self.ui, f"{type_}_cr_power").setText(str(getattr(self.ratios, f"{type_}_current_ratio_power")))
        getattr(self.ui, f"{type_}_cr_cap").setText(str(getattr(self.ratios, f"{type_}_current_ratio_cap")))
        getattr(self.ui, f"{type_}_cr_bar").setText(str(getattr(self.ratios, f"{type_}_current_ratio_bar")))
        # BASE GOAL
        getattr(self.ui, f"{type_}_base_goal_power").setText(str(getattr(self.ratios, f"{type_}_base_goal_power")))
        getattr(self.ui, f"{type_}_base_goal_cap").setText(str(getattr(self.ratios, f"{type_}_base_goal_cap")))
        getattr(self.ui, f"{type_}_base_goal_bar").setText(str(getattr(self.ratios, f"{type_}_base_goal_bar")))
        # AMOUNT LEFT TO BUY
        #       IN GAME VALUES
        getattr(self.ui, f"{type_}_amount_left_to_buy_power").setText(
            str(getattr(self.ratios, f"{type_}_amount_left_to_buy_power")))
        getattr(self.ui, f"{type_}_amount_left_to_buy_cap").setText(
            str(getattr(self.ratios, f"{type_}_amount_left_to_buy_cap")))
        getattr(self.ui, f"{type_}_amount_left_to_buy_bar").setText(
            str(getattr(self.ratios, f"{type_}_amount_left_to_buy_bar")))
        #       PRICE FOR THAT
        getattr(self.ui, f"{type_}_exp_cost_power").setText(str(getattr(self.ratios, f"{type_}_exp_cost_power")))
        getattr(self.ui, f"{type_}_exp_cost_cap").setText(str(getattr(self.ratios, f"{type_}_exp_cost_cap")))
        getattr(self.ui, f"{type_}_exp_cost_bar").setText(str(getattr(self.ratios, f"{type_}_exp_cost_bar")))
        getattr(self.ui, f"{type_}_amount_left_to_buy_name").setText(
            "Amount Left To Buy Until Your {} Goal\n(Total Cost: {} EXP)".format(
                type_,
                int(getattr(self.ratios, f"{type_}_amount_left_to_buy_sum"))
            )
        )
        #       COLOR CHECKER
        getattr(self.ui, f"{type_}_cr_power_checker").setText('~')
        getattr(self.ui, f"{type_}_cr_power_checker").setStyleSheet(return_color_for_cr(1))
        getattr(self.ui, f"{type_}_cr_cap_checker").setText(
            return_c_for_cr(getattr(self.ratios, f"{type_}_current_ratio_cap")))
        getattr(self.ui, f"{type_}_cr_cap_checker").setStyleSheet(
            return_color_for_cr(getattr(self.ratios, f"{type_}_current_ratio_cap")))
        getattr(self.ui, f"{type_}_cr_bar_checker").setText(
            return_c_for_cr(getattr(self.ratios, f"{type_}_current_ratio_bar")))
        getattr(self.ui, f"{type_}_cr_bar_checker").setStyleSheet(
            return_color_for_cr(getattr(self.ratios, f"{type_}_current_ratio_bar")))

    def draw_em_ratio(self):
        #   GOAL E:M
        self.ui.em_goal_em_ratio.setText(str(self.ratios.em_goal_em))
        #   CURRENT E:M RATIO
        self.ui.em_cr_power.setText('{} : 1'.format(round(self.ratios.em_cr_power, 2)))
        self.ui.em_cr_cap.setText('{} : 1'.format(round(self.ratios.em_cr_cap, 2)))
        self.ui.em_cr_bar.setText('{} : 1'.format(round(self.ratios.em_cr_bar, 2)))
        #   OPTIMAL ENERGY FOR MAGIC AT RATIO
        self.ui.em_optimal_energy_for_magic_power.setText(str(self.ratios.em_optimal_for_current_power))
        self.ui.em_optimal_energy_for_magic_cap.setText(str(self.ratios.em_optimal_for_current_cap))
        self.ui.em_optimal_energy_for_magic_bar.setText(str(self.ratios.em_optimal_for_current_bar))
        #   AMOUNT LEFT TO BUY
        self.ui.em_amount_left_to_buy_power.setText(str(self.ratios.em_amount_left_to_buy_power))
        self.ui.em_amount_left_to_buy_cap.setText(str(self.ratios.em_amount_left_to_buy_cap))
        self.ui.em_amount_left_to_buy_bar.setText(str(self.ratios.em_amount_left_to_buy_bar))
        self.ui.name_em_amount_left_to_buy.setText(
            "Amount Left To Buy Until Your Energy:Magic Goal\n(Total Cost: {} EXP)".format(
                int(self.ratios.em_amount_left_to_buy_sum)))
        #       EXP COST
        self.ui.em_exp_cost_power.setText('{} EXP'.format(self.ratios.em_exp_cost_power))
        self.ui.em_exp_cost_cap.setText('{} EXP'.format(self.ratios.em_exp_cost_cap))
        self.ui.em_exp_cost_bar.setText('{} EXP'.format(self.ratios.em_exp_cost_bar))
        #       COLORS CHECKER
        self.ui.em_cr_power_checker.setText(return_c_for_cr(self.ratios.em_cr_power))
        self.ui.em_cr_power_checker.setStyleSheet(return_color_for_cr(self.ratios.em_cr_power))
        self.ui.em_cr_cap_checker.setText(return_c_for_cr(self.ratios.em_cr_cap))
        self.ui.em_cr_cap_checker.setStyleSheet(return_color_for_cr(self.ratios.em_cr_cap))
        self.ui.em_cr_bar_checker.setText(return_c_for_cr(self.ratios.em_cr_bar))
        self.ui.em_cr_bar_checker.setStyleSheet(return_color_for_cr(self.ratios.em_cr_bar))

    def draw_me_ratio(self):
        #   GOAL M : E
        self.ui.em_goal_em_ratio.setText(str(self.ratios.em_goal_em))
        #   OPTIMAL MAGIC TO ENERGY AT RATIO
        self.ui.me_optimal_energy_for_magic_power.setText(str(self.ratios.me_optimal_for_current_power))
        self.ui.me_optimal_energy_for_magic_cap.setText(str(self.ratios.me_optimal_for_current_cap))
        self.ui.me_optimal_energy_for_magic_bar.setText(str(self.ratios.me_optimal_for_current_bar))
        #   AMOUNT LEFT TO BUY
        self.ui.me_amount_left_to_buy_power.setText('{}'.format(self.ratios.me_amount_left_to_buy_power))
        self.ui.me_amount_left_to_buy_cap.setText(str(self.ratios.me_amount_left_to_buy_cap))
        self.ui.me_amount_left_to_buy_bar.setText('{}'.format(int(self.ratios.me_amount_left_to_buy_bar)))
        self.ui.name_me_amount_left_to_buy.setText(
            "Amount Left To Buy Until Your MAGIC:ENERGY Goal\n(Total Cost: {} EXP)".format(
                int(self.ratios.me_amount_left_to_buy_sum)))
        #       EXP COST
        self.ui.me_exp_cost_power.setText('{} EXP'.format(self.ratios.me_exp_cost_power))
        self.ui.me_exp_cost_cap.setText('{} EXP'.format(self.ratios.me_exp_cost_cap))
        self.ui.me_exp_cost_bar.setText('{} EXP'.format(self.ratios.me_exp_cost_bar))

    def draw_er3_ratio(self):
        #   GOAL ENERGY : R3
        self.ui.er3_goal_er3_ratio.setText(str(self.ratios.er3_goal_er3))
        #   CURRENT E:M RATIO
        self.ui.er3_cr_power.setText('{} : 1'.format(round(self.ratios.er3_cr_power, 2)))
        self.ui.er3_cr_cap.setText('{} : 1'.format(round(self.ratios.er3_cr_cap, 2)))
        self.ui.er3_cr_bar.setText('{} : 1'.format(round(self.ratios.er3_cr_bar, 2)))
        #   OPTIMAL MAGIC TO ENERGY AT RATIO
        self.ui.er3_optimal_r3_for_energy_power.setText(str(self.ratios.er3_optimal_for_current_power))
        self.ui.er3_optimal_r3_for_energy_cap.setText(str(self.ratios.er3_optimal_for_current_cap))
        self.ui.er3_optimal_r3_for_energy_bar.setText(str(self.ratios.er3_optimal_for_current_bar))
        #   AMOUNT LEFT TO BUY
        self.ui.er3_amount_left_to_buy_power.setText('{}'.format(self.ratios.er3_amount_left_to_buy_power))
        self.ui.er3_amount_left_to_buy_cap.setText(str(self.ratios.er3_amount_left_to_buy_cap))
        self.ui.er3_amount_left_to_buy_bar.setText('{}'.format(int(self.ratios.er3_amount_left_to_buy_bar)))
        self.ui.name_er3_amount_left_to_buy.setText(
            "Amount Left To Buy Until Your ENERGY:R3 Goal\n(Total Cost: {} EXP)".format(
                int(self.ratios.er3_amount_left_to_buy_sum)))
        #       EXP COST
        self.ui.er3_exp_cost_power.setText('{} EXP'.format(self.ratios.er3_exp_cost_power))
        self.ui.er3_exp_cost_cap.setText('{} EXP'.format(self.ratios.er3_exp_cost_cap))
        self.ui.er3_exp_cost_bar.setText('{} EXP'.format(self.ratios.er3_exp_cost_bar))

    @Slot()
    def copy_to_clipboard_amount_left_to_buy(self):
        sender = self.sender()
        text = str(int(float(sender.text())))
        QApplication.clipboard().setText(text)
        QToolTip.showText(sender.mapToGlobal(sender.rect().center()), "Copied!")
        QTimer.singleShot(1500, QToolTip.hideText)

    def update_goal_edit(self, type_):
        power = float(getattr(self.ui, f"{type_}_goal_edit_power").text())
        cap = float(getattr(self.ui, f"{type_}_goal_edit_cap").text())
        bar = float(getattr(self.ui, f"{type_}_goal_edit_bar").text())

        update_method = getattr(self.ratios, f"update_{type_}")

        update_method(power, cap, bar)
        self.draw_type_ratio(type_)

    def update_em_goal_edit(self):
        energy = float(self.ui.em_edit_goal_ratio_energy.text())
        magic = float(self.ui.em_edit_goal_ratio_magic.text())
        self.ratios.update_em(energy, magic)
        self.ratios.update_me(energy, magic)
        self.draw_em_ratio()
        self.draw_me_ratio()

    def update_er3_goal_edit(self):
        energy = float(self.ui.er3_edit_goal_ratio_energy.text())
        r3 = float(self.ui.er3_edit_goal_ratio_r3.text())
        self.ratios.update_er3(energy, r3)
        self.ratios.update_me(energy, r3)
        self.draw_er3_ratio()
