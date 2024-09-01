# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ngu_helper.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_qt_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1601, 1177)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color:rgb(202, 224, 228);\n"
"}\n"
"\n"
"QPushButton{\n"
"font-size: 12px;\n"
"background-color: rgb(255, 229, 198);\n"
"font-family: \"Nunito\", sans-serif;\n"
"color:rgb(0, 0, 0);\n"
"border: none; /* \u0411\u0435\u0437 \u0433\u0440\u0430\u043d\u0438\u0446 */\n"
"border-radius: 0; /* \u0411\u0435\u0437 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0439 */\n"
"cursor: pointer;\n"
"}\n"
"\n"
"QWidget#em{\n"
"background-color:rgb(101,175,187);\n"
"}\n"
"QWidget#magic{\n"
"	background-color: rgb(116, 143, 246);\n"
"}\n"
"\n"
"QWidget#r3{\n"
"background-color:rgb(153, 0, 233);\n"
"}\n"
"QWidget#energy{\n"
"background-color:rgb(86, 206, 127);\n"
"}\n"
"\n"
"QLabel {\n"
"font-size: 12px;\n"
"color:rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel[type_of_header=\"misc\"] {\n"
"font-size: 24px;\n"
"color:rgb(0,0,0);\n"
"font-family: \"Orbitron\", sans-serif;\n"
"}\n"
"QLabel[type_of_header=\"0\"] {\n"
"background-color: rgb(164, 124, 190);\n"
"font-size: 48px;\n"
"color:rgb(0,0,0);\n"
""
                        "font-family: \"Orbitron\", sans-serif;\n"
"}\n"
"\n"
"QLabel[type_of_header=\"1\"] {\n"
"background-color: rgb(153, 153, 151);\n"
"font-family: \"Comfortaa\", sans-serif;\n"
"color:rgb(255,255,255);\n"
"}\n"
"\n"
"QLabel[type_of_header=\"2\"] {\n"
"background-color: rgb(255, 229, 198);\n"
"font-family: \"Nunito\", sans-serif;\n"
"}\n"
"\n"
"QLabel[type_of_header=\"3\"]{\n"
"background-color:rgb(253, 242, 199);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Title_Of_The_Tab = QLabel(self.centralwidget)
        self.Title_Of_The_Tab.setObjectName(u"Title_Of_The_Tab")
        self.Title_Of_The_Tab.setGeometry(QRect(290, 30, 891, 77))
        self.Title_Of_The_Tab.setMinimumSize(QSize(661, 77))
        font = QFont()
        font.setFamilies([u"Orbitron"])
        self.Title_Of_The_Tab.setFont(font)
        self.Title_Of_The_Tab.setStyleSheet(u"")
        self.Title_Of_The_Tab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 120, 1413, 1041))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.energy = QWidget(self.gridLayoutWidget)
        self.energy.setObjectName(u"energy")
        self.energy.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.energy)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Title = QLabel(self.energy)
        self.Title.setObjectName(u"Title")

        self.verticalLayout_3.addWidget(self.Title)

        self.energy_base_stat = QVBoxLayout()
        self.energy_base_stat.setSpacing(0)
        self.energy_base_stat.setObjectName(u"energy_base_stat")
        self.header_3 = QLabel(self.energy)
        self.header_3.setObjectName(u"header_3")
        self.header_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.energy_base_stat.addWidget(self.header_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.base_e_cap = QLabel(self.energy)
        self.base_e_cap.setObjectName(u"base_e_cap")
        self.base_e_cap.setMinimumSize(QSize(130, 21))
        self.base_e_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.base_e_cap, 1, 1, 1, 1)

        self.label_14 = QLabel(self.energy)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(130, 21))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.energy)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(130, 21))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1)

        self.base_e_pow = QLabel(self.energy)
        self.base_e_pow.setObjectName(u"base_e_pow")
        self.base_e_pow.setMinimumSize(QSize(130, 21))
        self.base_e_pow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.base_e_pow, 1, 0, 1, 1)

        self.base_e_bar = QLabel(self.energy)
        self.base_e_bar.setObjectName(u"base_e_bar")
        self.base_e_bar.setMinimumSize(QSize(130, 21))
        self.base_e_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.base_e_bar, 1, 2, 1, 1)

        self.label_16 = QLabel(self.energy)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(130, 21))
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_16, 0, 2, 1, 1)


        self.energy_base_stat.addLayout(self.gridLayout_3)


        self.verticalLayout_3.addLayout(self.energy_base_stat)

        self.energy_current_raio = QVBoxLayout()
        self.energy_current_raio.setSpacing(0)
        self.energy_current_raio.setObjectName(u"energy_current_raio")
        self.header_2 = QLabel(self.energy)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setMinimumSize(QSize(395, 21))
        self.header_2.setMaximumSize(QSize(16777215, 21))
        self.header_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.energy_current_raio.addWidget(self.header_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.energy)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(130, 21))
        self.label_6.setMaximumSize(QSize(130, 21))
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.energy)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(130, 21))
        self.label_7.setMaximumSize(QSize(130, 21))
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_8 = QLabel(self.energy)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(130, 21))
        self.label_8.setMaximumSize(QSize(130, 21))
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.CER_power = QLabel(self.energy)
        self.CER_power.setObjectName(u"CER_power")
        self.CER_power.setMinimumSize(QSize(130, 21))
        self.CER_power.setMaximumSize(QSize(130, 21))
        self.CER_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.CER_power)

        self.energy_CR_power_checker = QLabel(self.energy)
        self.energy_CR_power_checker.setObjectName(u"energy_CR_power_checker")
        self.energy_CR_power_checker.setMinimumSize(QSize(25, 21))
        self.energy_CR_power_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.energy_CR_power_checker)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.CER_cap = QLabel(self.energy)
        self.CER_cap.setObjectName(u"CER_cap")
        self.CER_cap.setMinimumSize(QSize(130, 21))
        self.CER_cap.setMaximumSize(QSize(130, 21))
        self.CER_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.CER_cap)

        self.energy_CR_cap_checker = QLabel(self.energy)
        self.energy_CR_cap_checker.setObjectName(u"energy_CR_cap_checker")
        self.energy_CR_cap_checker.setMinimumSize(QSize(25, 21))
        self.energy_CR_cap_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.energy_CR_cap_checker)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.CER_bars = QLabel(self.energy)
        self.CER_bars.setObjectName(u"CER_bars")
        self.CER_bars.setMinimumSize(QSize(130, 21))
        self.CER_bars.setMaximumSize(QSize(130, 21))
        self.CER_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.CER_bars)

        self.energy_CR_bar_checker = QLabel(self.energy)
        self.energy_CR_bar_checker.setObjectName(u"energy_CR_bar_checker")
        self.energy_CR_bar_checker.setMinimumSize(QSize(25, 21))
        self.energy_CR_bar_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.energy_CR_bar_checker)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 1, 2, 1, 1)


        self.energy_current_raio.addLayout(self.gridLayout_2)


        self.verticalLayout_3.addLayout(self.energy_current_raio)

        self.verticalSpacer_3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.energy_goal_ratio = QVBoxLayout()
        self.energy_goal_ratio.setSpacing(0)
        self.energy_goal_ratio.setObjectName(u"energy_goal_ratio")
        self.header_1 = QLabel(self.energy)
        self.header_1.setObjectName(u"header_1")
        self.header_1.setMinimumSize(QSize(395, 21))
        self.header_1.setMaximumSize(QSize(16777215, 21))
        self.header_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.energy_goal_ratio.addWidget(self.header_1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.energy_goal_edit_power = QLineEdit(self.energy)
        self.energy_goal_edit_power.setObjectName(u"energy_goal_edit_power")

        self.gridLayout.addWidget(self.energy_goal_edit_power, 1, 0, 1, 1)

        self.energy_goal_edit_cap = QLineEdit(self.energy)
        self.energy_goal_edit_cap.setObjectName(u"energy_goal_edit_cap")

        self.gridLayout.addWidget(self.energy_goal_edit_cap, 1, 1, 1, 1)

        self.label_3 = QLabel(self.energy)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(130, 21))
        self.label_3.setMaximumSize(QSize(130, 21))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet(u"")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_4 = QLabel(self.energy)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(130, 21))
        self.label_4.setMaximumSize(QSize(130, 21))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.energy_goal_edit_bar = QLineEdit(self.energy)
        self.energy_goal_edit_bar.setObjectName(u"energy_goal_edit_bar")

        self.gridLayout.addWidget(self.energy_goal_edit_bar, 1, 2, 1, 1)

        self.label_5 = QLabel(self.energy)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(130, 21))
        self.label_5.setMaximumSize(QSize(130, 21))
        font1 = QFont()
        font1.setFamilies([u"Nunito"])
        font1.setBold(False)
        self.label_5.setFont(font1)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet(u"")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)


        self.energy_goal_ratio.addLayout(self.gridLayout)


        self.verticalLayout_3.addLayout(self.energy_goal_ratio)

        self.verticalSpacer = QSpacerItem(20, 92, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.energy_base_goals = QVBoxLayout()
        self.energy_base_goals.setSpacing(0)
        self.energy_base_goals.setObjectName(u"energy_base_goals")
        self.header_4 = QLabel(self.energy)
        self.header_4.setObjectName(u"header_4")
        self.header_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.energy_base_goals.addWidget(self.header_4)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.energy_base_goal_power = QLabel(self.energy)
        self.energy_base_goal_power.setObjectName(u"energy_base_goal_power")
        self.energy_base_goal_power.setMinimumSize(QSize(130, 21))
        self.energy_base_goal_power.setMaximumSize(QSize(130, 21))
        self.energy_base_goal_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.energy_base_goal_power, 1, 0, 1, 1)

        self.energy_base_goal_bar = QLabel(self.energy)
        self.energy_base_goal_bar.setObjectName(u"energy_base_goal_bar")
        self.energy_base_goal_bar.setMinimumSize(QSize(130, 21))
        self.energy_base_goal_bar.setMaximumSize(QSize(130, 21))
        self.energy_base_goal_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.energy_base_goal_bar, 1, 2, 1, 1)

        self.energy_base_goal_cap = QLabel(self.energy)
        self.energy_base_goal_cap.setObjectName(u"energy_base_goal_cap")
        self.energy_base_goal_cap.setMinimumSize(QSize(130, 21))
        self.energy_base_goal_cap.setMaximumSize(QSize(130, 21))
        self.energy_base_goal_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.energy_base_goal_cap, 1, 1, 1, 1)

        self.label_23 = QLabel(self.energy)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(130, 21))
        self.label_23.setMaximumSize(QSize(130, 21))
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_23, 0, 2, 1, 1)

        self.label_21 = QLabel(self.energy)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(130, 21))
        self.label_21.setMaximumSize(QSize(130, 21))
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_21, 0, 0, 1, 1)

        self.label_22 = QLabel(self.energy)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(130, 21))
        self.label_22.setMaximumSize(QSize(130, 21))
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.label_22, 0, 1, 1, 1)


        self.energy_base_goals.addLayout(self.gridLayout_7)


        self.verticalLayout_3.addLayout(self.energy_base_goals)

        self.energy_amount_left_to_buy = QVBoxLayout()
        self.energy_amount_left_to_buy.setSpacing(0)
        self.energy_amount_left_to_buy.setObjectName(u"energy_amount_left_to_buy")
        self.amount_left_to_buy_energy = QLabel(self.energy)
        self.amount_left_to_buy_energy.setObjectName(u"amount_left_to_buy_energy")
        self.amount_left_to_buy_energy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.energy_amount_left_to_buy.addWidget(self.amount_left_to_buy_energy)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_36 = QLabel(self.energy)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(130, 21))
        self.label_36.setMaximumSize(QSize(130, 21))
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_36, 2, 0, 1, 1)

        self.energy_exp_cost_cap = QLabel(self.energy)
        self.energy_exp_cost_cap.setObjectName(u"energy_exp_cost_cap")
        self.energy_exp_cost_cap.setMinimumSize(QSize(130, 21))
        self.energy_exp_cost_cap.setMaximumSize(QSize(130, 21))
        self.energy_exp_cost_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.energy_exp_cost_cap, 3, 1, 1, 1)

        self.energy_exp_cost_power = QLabel(self.energy)
        self.energy_exp_cost_power.setObjectName(u"energy_exp_cost_power")
        self.energy_exp_cost_power.setMinimumSize(QSize(130, 21))
        self.energy_exp_cost_power.setMaximumSize(QSize(130, 21))
        self.energy_exp_cost_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.energy_exp_cost_power, 3, 0, 1, 1)

        self.label_30 = QLabel(self.energy)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(130, 21))
        self.label_30.setMaximumSize(QSize(130, 21))
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_35 = QLabel(self.energy)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(130, 21))
        self.label_35.setMaximumSize(QSize(130, 21))
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_35, 2, 1, 1, 1)

        self.label_29 = QLabel(self.energy)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(130, 21))
        self.label_29.setMaximumSize(QSize(130, 21))
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_29, 0, 1, 1, 1)

        self.label_28 = QLabel(self.energy)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(130, 21))
        self.label_28.setMaximumSize(QSize(130, 21))
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_28, 0, 2, 1, 1)

        self.label_34 = QLabel(self.energy)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(130, 21))
        self.label_34.setMaximumSize(QSize(130, 21))
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.label_34, 2, 2, 1, 1)

        self.energy_exp_cost_bars = QLabel(self.energy)
        self.energy_exp_cost_bars.setObjectName(u"energy_exp_cost_bars")
        self.energy_exp_cost_bars.setMinimumSize(QSize(130, 21))
        self.energy_exp_cost_bars.setMaximumSize(QSize(130, 21))
        self.energy_exp_cost_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.energy_exp_cost_bars, 3, 2, 1, 1)

        self.energy_amount_left_to_buy_power = QPushButton(self.energy)
        self.energy_amount_left_to_buy_power.setObjectName(u"energy_amount_left_to_buy_power")
        self.energy_amount_left_to_buy_power.setMinimumSize(QSize(21, 21))
        self.energy_amount_left_to_buy_power.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon = QIcon()
        icon.addFile(u":/icons/resources/icons/copy_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.energy_amount_left_to_buy_power.setIcon(icon)

        self.gridLayout_8.addWidget(self.energy_amount_left_to_buy_power, 1, 0, 1, 1)

        self.energy_amount_left_to_buy_cap = QPushButton(self.energy)
        self.energy_amount_left_to_buy_cap.setObjectName(u"energy_amount_left_to_buy_cap")
        self.energy_amount_left_to_buy_cap.setMinimumSize(QSize(21, 21))
        self.energy_amount_left_to_buy_cap.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.energy_amount_left_to_buy_cap.setIcon(icon)

        self.gridLayout_8.addWidget(self.energy_amount_left_to_buy_cap, 1, 1, 1, 1)

        self.energy_amount_left_to_buy_bar = QPushButton(self.energy)
        self.energy_amount_left_to_buy_bar.setObjectName(u"energy_amount_left_to_buy_bar")
        self.energy_amount_left_to_buy_bar.setMinimumSize(QSize(21, 21))
        self.energy_amount_left_to_buy_bar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.energy_amount_left_to_buy_bar.setIcon(icon)

        self.gridLayout_8.addWidget(self.energy_amount_left_to_buy_bar, 1, 2, 1, 1)


        self.energy_amount_left_to_buy.addLayout(self.gridLayout_8)


        self.verticalLayout_3.addLayout(self.energy_amount_left_to_buy)


        self.gridLayout_12.addWidget(self.energy, 0, 0, 1, 1)

        self.r3 = QWidget(self.gridLayoutWidget)
        self.r3.setObjectName(u"r3")
        self.verticalLayout_10 = QVBoxLayout(self.r3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Title_4 = QLabel(self.r3)
        self.Title_4.setObjectName(u"Title_4")

        self.verticalLayout_10.addWidget(self.Title_4)

        self.layout_r3_base_stats = QVBoxLayout()
        self.layout_r3_base_stats.setSpacing(0)
        self.layout_r3_base_stats.setObjectName(u"layout_r3_base_stats")
        self.header_13 = QLabel(self.r3)
        self.header_13.setObjectName(u"header_13")
        self.header_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_r3_base_stats.addWidget(self.header_13)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_31 = QLabel(self.r3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(130, 21))
        self.label_31.setMaximumSize(QSize(130, 21))
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_31, 0, 0, 1, 1)

        self.r3_base_bar = QLabel(self.r3)
        self.r3_base_bar.setObjectName(u"r3_base_bar")
        self.r3_base_bar.setMinimumSize(QSize(130, 21))
        self.r3_base_bar.setMaximumSize(QSize(130, 21))
        self.r3_base_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.r3_base_bar, 1, 2, 1, 1)

        self.label_32 = QLabel(self.r3)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(130, 21))
        self.label_32.setMaximumSize(QSize(130, 21))
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_32, 0, 1, 1, 1)

        self.r3_base_cap = QLabel(self.r3)
        self.r3_base_cap.setObjectName(u"r3_base_cap")
        self.r3_base_cap.setMinimumSize(QSize(130, 21))
        self.r3_base_cap.setMaximumSize(QSize(130, 21))
        self.r3_base_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.r3_base_cap, 1, 1, 1, 1)

        self.label_33 = QLabel(self.r3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(130, 21))
        self.label_33.setMaximumSize(QSize(130, 21))
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.label_33, 0, 2, 1, 1)

        self.r3_base_power = QLabel(self.r3)
        self.r3_base_power.setObjectName(u"r3_base_power")
        self.r3_base_power.setMinimumSize(QSize(130, 21))
        self.r3_base_power.setMaximumSize(QSize(130, 21))
        self.r3_base_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.r3_base_power, 1, 0, 1, 1)


        self.layout_r3_base_stats.addLayout(self.gridLayout_16)


        self.verticalLayout_10.addLayout(self.layout_r3_base_stats)

        self.layout_r3_current_ratio = QVBoxLayout()
        self.layout_r3_current_ratio.setSpacing(0)
        self.layout_r3_current_ratio.setObjectName(u"layout_r3_current_ratio")
        self.header_14 = QLabel(self.r3)
        self.header_14.setObjectName(u"header_14")
        self.header_14.setMinimumSize(QSize(395, 21))
        self.header_14.setMaximumSize(QSize(16777215, 21))
        self.header_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_r3_current_ratio.addWidget(self.header_14)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_63 = QLabel(self.r3)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(130, 21))
        self.label_63.setMaximumSize(QSize(130, 21))
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_63, 0, 1, 1, 1)

        self.label_64 = QLabel(self.r3)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(130, 21))
        self.label_64.setMaximumSize(QSize(130, 21))
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_64, 0, 0, 1, 1)

        self.label_65 = QLabel(self.r3)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(130, 21))
        self.label_65.setMaximumSize(QSize(130, 21))
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.label_65, 0, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.r3_cr_power = QLabel(self.r3)
        self.r3_cr_power.setObjectName(u"r3_cr_power")
        self.r3_cr_power.setMinimumSize(QSize(105, 21))
        self.r3_cr_power.setMaximumSize(QSize(130, 21))
        self.r3_cr_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.r3_cr_power)

        self.r3_cr_power_checker = QLabel(self.r3)
        self.r3_cr_power_checker.setObjectName(u"r3_cr_power_checker")
        self.r3_cr_power_checker.setMinimumSize(QSize(25, 21))
        self.r3_cr_power_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.r3_cr_power_checker)


        self.gridLayout_17.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.r3_cr_cap = QLabel(self.r3)
        self.r3_cr_cap.setObjectName(u"r3_cr_cap")
        self.r3_cr_cap.setMinimumSize(QSize(105, 21))
        self.r3_cr_cap.setMaximumSize(QSize(130, 21))
        self.r3_cr_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.r3_cr_cap)

        self.r3_cr_cap_checker = QLabel(self.r3)
        self.r3_cr_cap_checker.setObjectName(u"r3_cr_cap_checker")
        self.r3_cr_cap_checker.setMinimumSize(QSize(25, 21))
        self.r3_cr_cap_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.r3_cr_cap_checker)


        self.gridLayout_17.addLayout(self.horizontalLayout_9, 1, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.r3_cr_bars = QLabel(self.r3)
        self.r3_cr_bars.setObjectName(u"r3_cr_bars")
        self.r3_cr_bars.setMinimumSize(QSize(105, 21))
        self.r3_cr_bars.setMaximumSize(QSize(130, 21))
        self.r3_cr_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.r3_cr_bars)

        self.r3_cr_bar_checker = QLabel(self.r3)
        self.r3_cr_bar_checker.setObjectName(u"r3_cr_bar_checker")
        self.r3_cr_bar_checker.setMinimumSize(QSize(25, 21))
        self.r3_cr_bar_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.r3_cr_bar_checker)


        self.gridLayout_17.addLayout(self.horizontalLayout_10, 1, 2, 1, 1)


        self.layout_r3_current_ratio.addLayout(self.gridLayout_17)


        self.verticalLayout_10.addLayout(self.layout_r3_current_ratio)

        self.verticalSpacer_7 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_10.addItem(self.verticalSpacer_7)

        self.layout_r3_goal_ratio_3 = QVBoxLayout()
        self.layout_r3_goal_ratio_3.setSpacing(0)
        self.layout_r3_goal_ratio_3.setObjectName(u"layout_r3_goal_ratio_3")
        self.header_15 = QLabel(self.r3)
        self.header_15.setObjectName(u"header_15")
        self.header_15.setMinimumSize(QSize(395, 21))
        self.header_15.setMaximumSize(QSize(16777215, 21))
        self.header_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_r3_goal_ratio_3.addWidget(self.header_15)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.r3_goal_edit_power = QLineEdit(self.r3)
        self.r3_goal_edit_power.setObjectName(u"r3_goal_edit_power")
        self.r3_goal_edit_power.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.r3_goal_edit_power.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.gridLayout_18.addWidget(self.r3_goal_edit_power, 1, 0, 1, 1)

        self.label_66 = QLabel(self.r3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(130, 21))
        self.label_66.setMaximumSize(QSize(130, 21))
        self.label_66.setAutoFillBackground(False)
        self.label_66.setStyleSheet(u"")
        self.label_66.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.label_66, 0, 0, 1, 1)

        self.label_67 = QLabel(self.r3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(130, 21))
        self.label_67.setMaximumSize(QSize(130, 21))
        self.label_67.setFont(font1)
        self.label_67.setAutoFillBackground(False)
        self.label_67.setStyleSheet(u"")
        self.label_67.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.label_67, 0, 1, 1, 1)

        self.r3_goal_edit_cap = QLineEdit(self.r3)
        self.r3_goal_edit_cap.setObjectName(u"r3_goal_edit_cap")

        self.gridLayout_18.addWidget(self.r3_goal_edit_cap, 1, 1, 1, 1)

        self.label_68 = QLabel(self.r3)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(130, 21))
        self.label_68.setMaximumSize(QSize(130, 21))
        self.label_68.setAutoFillBackground(False)
        self.label_68.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.label_68, 0, 2, 1, 1)

        self.r3_goal_edit_bar = QLineEdit(self.r3)
        self.r3_goal_edit_bar.setObjectName(u"r3_goal_edit_bar")

        self.gridLayout_18.addWidget(self.r3_goal_edit_bar, 1, 2, 1, 1)


        self.layout_r3_goal_ratio_3.addLayout(self.gridLayout_18)


        self.verticalLayout_10.addLayout(self.layout_r3_goal_ratio_3)

        self.verticalSpacer_8 = QSpacerItem(420, 89, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)

        self.layout_r3_base_goals = QVBoxLayout()
        self.layout_r3_base_goals.setSpacing(0)
        self.layout_r3_base_goals.setObjectName(u"layout_r3_base_goals")
        self.header_16 = QLabel(self.r3)
        self.header_16.setObjectName(u"header_16")
        self.header_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_r3_base_goals.addWidget(self.header_16)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.r3_base_goal_power = QLabel(self.r3)
        self.r3_base_goal_power.setObjectName(u"r3_base_goal_power")
        self.r3_base_goal_power.setMinimumSize(QSize(130, 21))
        self.r3_base_goal_power.setMaximumSize(QSize(130, 21))
        self.r3_base_goal_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.r3_base_goal_power, 1, 0, 1, 1)

        self.r3_base_goal_bar = QLabel(self.r3)
        self.r3_base_goal_bar.setObjectName(u"r3_base_goal_bar")
        self.r3_base_goal_bar.setMinimumSize(QSize(130, 21))
        self.r3_base_goal_bar.setMaximumSize(QSize(130, 21))
        self.r3_base_goal_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.r3_base_goal_bar, 1, 2, 1, 1)

        self.r3_base_goal_cap = QLabel(self.r3)
        self.r3_base_goal_cap.setObjectName(u"r3_base_goal_cap")
        self.r3_base_goal_cap.setMinimumSize(QSize(130, 21))
        self.r3_base_goal_cap.setMaximumSize(QSize(130, 21))
        self.r3_base_goal_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.r3_base_goal_cap, 1, 1, 1, 1)

        self.label_69 = QLabel(self.r3)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(130, 21))
        self.label_69.setMaximumSize(QSize(130, 21))
        self.label_69.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.label_69, 0, 2, 1, 1)

        self.label_70 = QLabel(self.r3)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(130, 21))
        self.label_70.setMaximumSize(QSize(130, 21))
        self.label_70.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.label_70, 0, 0, 1, 1)

        self.label_71 = QLabel(self.r3)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(130, 21))
        self.label_71.setMaximumSize(QSize(130, 21))
        self.label_71.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.label_71, 0, 1, 1, 1)


        self.layout_r3_base_goals.addLayout(self.gridLayout_19)


        self.verticalLayout_10.addLayout(self.layout_r3_base_goals)

        self.layout_r3_amount_left_to_buy = QVBoxLayout()
        self.layout_r3_amount_left_to_buy.setSpacing(0)
        self.layout_r3_amount_left_to_buy.setObjectName(u"layout_r3_amount_left_to_buy")
        self.name_r3_amount_left_to_buy = QLabel(self.r3)
        self.name_r3_amount_left_to_buy.setObjectName(u"name_r3_amount_left_to_buy")
        self.name_r3_amount_left_to_buy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_r3_amount_left_to_buy.addWidget(self.name_r3_amount_left_to_buy)

        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_72 = QLabel(self.r3)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(130, 21))
        self.label_72.setMaximumSize(QSize(130, 21))
        self.label_72.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_72, 2, 0, 1, 1)

        self.r3_exp_cost_cap = QLabel(self.r3)
        self.r3_exp_cost_cap.setObjectName(u"r3_exp_cost_cap")
        self.r3_exp_cost_cap.setMinimumSize(QSize(130, 21))
        self.r3_exp_cost_cap.setMaximumSize(QSize(130, 21))
        self.r3_exp_cost_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.r3_exp_cost_cap, 3, 1, 1, 1)

        self.r3_exp_cost_power = QLabel(self.r3)
        self.r3_exp_cost_power.setObjectName(u"r3_exp_cost_power")
        self.r3_exp_cost_power.setMinimumSize(QSize(130, 21))
        self.r3_exp_cost_power.setMaximumSize(QSize(130, 21))
        self.r3_exp_cost_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.r3_exp_cost_power, 3, 0, 1, 1)

        self.label_73 = QLabel(self.r3)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(130, 21))
        self.label_73.setMaximumSize(QSize(130, 21))
        self.label_73.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_73, 0, 0, 1, 1)

        self.label_74 = QLabel(self.r3)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(130, 21))
        self.label_74.setMaximumSize(QSize(130, 21))
        self.label_74.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_74, 2, 1, 1, 1)

        self.label_75 = QLabel(self.r3)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(130, 21))
        self.label_75.setMaximumSize(QSize(130, 21))
        self.label_75.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_75, 0, 1, 1, 1)

        self.label_76 = QLabel(self.r3)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(130, 21))
        self.label_76.setMaximumSize(QSize(130, 21))
        self.label_76.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_76, 0, 2, 1, 1)

        self.label_77 = QLabel(self.r3)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(130, 21))
        self.label_77.setMaximumSize(QSize(130, 21))
        self.label_77.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.label_77, 2, 2, 1, 1)

        self.r3_exp_cost_bars = QLabel(self.r3)
        self.r3_exp_cost_bars.setObjectName(u"r3_exp_cost_bars")
        self.r3_exp_cost_bars.setMinimumSize(QSize(130, 21))
        self.r3_exp_cost_bars.setMaximumSize(QSize(130, 21))
        self.r3_exp_cost_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.r3_exp_cost_bars, 3, 2, 1, 1)

        self.r3_amount_left_to_buy_bar = QPushButton(self.r3)
        self.r3_amount_left_to_buy_bar.setObjectName(u"r3_amount_left_to_buy_bar")
        self.r3_amount_left_to_buy_bar.setMinimumSize(QSize(21, 21))
        self.r3_amount_left_to_buy_bar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.r3_amount_left_to_buy_bar.setIcon(icon)

        self.gridLayout_20.addWidget(self.r3_amount_left_to_buy_bar, 1, 2, 1, 1)

        self.r3_amount_left_to_buy_cap = QPushButton(self.r3)
        self.r3_amount_left_to_buy_cap.setObjectName(u"r3_amount_left_to_buy_cap")
        self.r3_amount_left_to_buy_cap.setMinimumSize(QSize(21, 21))
        self.r3_amount_left_to_buy_cap.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.r3_amount_left_to_buy_cap.setIcon(icon)

        self.gridLayout_20.addWidget(self.r3_amount_left_to_buy_cap, 1, 1, 1, 1)

        self.r3_amount_left_to_buy_power = QPushButton(self.r3)
        self.r3_amount_left_to_buy_power.setObjectName(u"r3_amount_left_to_buy_power")
        self.r3_amount_left_to_buy_power.setMinimumSize(QSize(21, 21))
        self.r3_amount_left_to_buy_power.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.r3_amount_left_to_buy_power.setIcon(icon)

        self.gridLayout_20.addWidget(self.r3_amount_left_to_buy_power, 1, 0, 1, 1)


        self.layout_r3_amount_left_to_buy.addLayout(self.gridLayout_20)


        self.verticalLayout_10.addLayout(self.layout_r3_amount_left_to_buy)


        self.gridLayout_12.addWidget(self.r3, 0, 2, 1, 1)

        self.magic = QWidget(self.gridLayoutWidget)
        self.magic.setObjectName(u"magic")
        self.verticalLayout_8 = QVBoxLayout(self.magic)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.Title_2 = QLabel(self.magic)
        self.Title_2.setObjectName(u"Title_2")

        self.verticalLayout_8.addWidget(self.Title_2)

        self.magic_base_stats = QVBoxLayout()
        self.magic_base_stats.setSpacing(0)
        self.magic_base_stats.setObjectName(u"magic_base_stats")
        self.header_5 = QLabel(self.magic)
        self.header_5.setObjectName(u"header_5")
        self.header_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.magic_base_stats.addWidget(self.header_5)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_17 = QLabel(self.magic)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(130, 21))
        self.label_17.setMaximumSize(QSize(130, 21))
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_17, 0, 0, 1, 1)

        self.base_m_bar = QLabel(self.magic)
        self.base_m_bar.setObjectName(u"base_m_bar")
        self.base_m_bar.setMinimumSize(QSize(130, 21))
        self.base_m_bar.setMaximumSize(QSize(130, 21))
        self.base_m_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.base_m_bar, 1, 2, 1, 1)

        self.label_18 = QLabel(self.magic)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(130, 21))
        self.label_18.setMaximumSize(QSize(130, 21))
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_18, 0, 1, 1, 1)

        self.base_m_cap = QLabel(self.magic)
        self.base_m_cap.setObjectName(u"base_m_cap")
        self.base_m_cap.setMinimumSize(QSize(130, 21))
        self.base_m_cap.setMaximumSize(QSize(130, 21))
        self.base_m_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.base_m_cap, 1, 1, 1, 1)

        self.label_19 = QLabel(self.magic)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(130, 21))
        self.label_19.setMaximumSize(QSize(130, 21))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_19, 0, 2, 1, 1)

        self.base_m_pow = QLabel(self.magic)
        self.base_m_pow.setObjectName(u"base_m_pow")
        self.base_m_pow.setMinimumSize(QSize(130, 21))
        self.base_m_pow.setMaximumSize(QSize(130, 21))
        self.base_m_pow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.base_m_pow, 1, 0, 1, 1)


        self.magic_base_stats.addLayout(self.gridLayout_4)


        self.verticalLayout_8.addLayout(self.magic_base_stats)

        self.magic_current_ratio = QVBoxLayout()
        self.magic_current_ratio.setSpacing(0)
        self.magic_current_ratio.setObjectName(u"magic_current_ratio")
        self.header_6 = QLabel(self.magic)
        self.header_6.setObjectName(u"header_6")
        self.header_6.setMinimumSize(QSize(395, 21))
        self.header_6.setMaximumSize(QSize(16777215, 21))
        self.header_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.magic_current_ratio.addWidget(self.header_6)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_9 = QLabel(self.magic)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(130, 21))
        self.label_9.setMaximumSize(QSize(130, 21))
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)

        self.label_10 = QLabel(self.magic)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(130, 21))
        self.label_10.setMaximumSize(QSize(130, 21))
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_11 = QLabel(self.magic)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(130, 21))
        self.label_11.setMaximumSize(QSize(130, 21))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_11, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CMR_power = QLabel(self.magic)
        self.CMR_power.setObjectName(u"CMR_power")
        self.CMR_power.setMinimumSize(QSize(105, 21))
        self.CMR_power.setMaximumSize(QSize(130, 21))
        self.CMR_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.CMR_power)

        self.magic_CR_power_checker = QLabel(self.magic)
        self.magic_CR_power_checker.setObjectName(u"magic_CR_power_checker")
        self.magic_CR_power_checker.setMinimumSize(QSize(25, 21))
        self.magic_CR_power_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.magic_CR_power_checker)


        self.gridLayout_5.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CMR_cap = QLabel(self.magic)
        self.CMR_cap.setObjectName(u"CMR_cap")
        self.CMR_cap.setMinimumSize(QSize(105, 21))
        self.CMR_cap.setMaximumSize(QSize(130, 21))
        self.CMR_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.CMR_cap)

        self.magic_CR_cap_checker = QLabel(self.magic)
        self.magic_CR_cap_checker.setObjectName(u"magic_CR_cap_checker")
        self.magic_CR_cap_checker.setMinimumSize(QSize(25, 21))
        self.magic_CR_cap_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.magic_CR_cap_checker)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CMR_bars = QLabel(self.magic)
        self.CMR_bars.setObjectName(u"CMR_bars")
        self.CMR_bars.setMinimumSize(QSize(105, 21))
        self.CMR_bars.setMaximumSize(QSize(130, 21))
        self.CMR_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.CMR_bars)

        self.magic_CR_bar_checker = QLabel(self.magic)
        self.magic_CR_bar_checker.setObjectName(u"magic_CR_bar_checker")
        self.magic_CR_bar_checker.setMinimumSize(QSize(25, 21))
        self.magic_CR_bar_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.magic_CR_bar_checker)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)


        self.magic_current_ratio.addLayout(self.gridLayout_5)


        self.verticalLayout_8.addLayout(self.magic_current_ratio)

        self.verticalSpacer_4 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_8.addItem(self.verticalSpacer_4)

        self.magic_goal_ratio = QVBoxLayout()
        self.magic_goal_ratio.setSpacing(0)
        self.magic_goal_ratio.setObjectName(u"magic_goal_ratio")
        self.header_7 = QLabel(self.magic)
        self.header_7.setObjectName(u"header_7")
        self.header_7.setMinimumSize(QSize(395, 21))
        self.header_7.setMaximumSize(QSize(16777215, 21))
        self.header_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.magic_goal_ratio.addWidget(self.header_7)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.magic_goal_edit_power = QLineEdit(self.magic)
        self.magic_goal_edit_power.setObjectName(u"magic_goal_edit_power")
        self.magic_goal_edit_power.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.magic_goal_edit_power.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.gridLayout_6.addWidget(self.magic_goal_edit_power, 1, 0, 1, 1)

        self.label_13 = QLabel(self.magic)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(130, 21))
        self.label_13.setMaximumSize(QSize(130, 21))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet(u"")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_27 = QLabel(self.magic)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(130, 21))
        self.label_27.setMaximumSize(QSize(130, 21))
        self.label_27.setFont(font1)
        self.label_27.setAutoFillBackground(False)
        self.label_27.setStyleSheet(u"")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_27, 0, 1, 1, 1)

        self.magic_goal_edit_cap = QLineEdit(self.magic)
        self.magic_goal_edit_cap.setObjectName(u"magic_goal_edit_cap")

        self.gridLayout_6.addWidget(self.magic_goal_edit_cap, 1, 1, 1, 1)

        self.label_20 = QLabel(self.magic)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(130, 21))
        self.label_20.setMaximumSize(QSize(130, 21))
        self.label_20.setAutoFillBackground(False)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_20, 0, 2, 1, 1)

        self.magic_goal_edit_bar = QLineEdit(self.magic)
        self.magic_goal_edit_bar.setObjectName(u"magic_goal_edit_bar")

        self.gridLayout_6.addWidget(self.magic_goal_edit_bar, 1, 2, 1, 1)


        self.magic_goal_ratio.addLayout(self.gridLayout_6)


        self.verticalLayout_8.addLayout(self.magic_goal_ratio)

        self.verticalSpacer_2 = QSpacerItem(420, 89, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.magic_base_goals = QVBoxLayout()
        self.magic_base_goals.setSpacing(0)
        self.magic_base_goals.setObjectName(u"magic_base_goals")
        self.header_8 = QLabel(self.magic)
        self.header_8.setObjectName(u"header_8")
        self.header_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.magic_base_goals.addWidget(self.header_8)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.magic_base_goal_power = QLabel(self.magic)
        self.magic_base_goal_power.setObjectName(u"magic_base_goal_power")
        self.magic_base_goal_power.setMinimumSize(QSize(130, 21))
        self.magic_base_goal_power.setMaximumSize(QSize(130, 21))
        self.magic_base_goal_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.magic_base_goal_power, 1, 0, 1, 1)

        self.magic_base_goal_bar = QLabel(self.magic)
        self.magic_base_goal_bar.setObjectName(u"magic_base_goal_bar")
        self.magic_base_goal_bar.setMinimumSize(QSize(130, 21))
        self.magic_base_goal_bar.setMaximumSize(QSize(130, 21))
        self.magic_base_goal_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.magic_base_goal_bar, 1, 2, 1, 1)

        self.magic_base_goal_cap = QLabel(self.magic)
        self.magic_base_goal_cap.setObjectName(u"magic_base_goal_cap")
        self.magic_base_goal_cap.setMinimumSize(QSize(130, 21))
        self.magic_base_goal_cap.setMaximumSize(QSize(130, 21))
        self.magic_base_goal_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.magic_base_goal_cap, 1, 1, 1, 1)

        self.label_37 = QLabel(self.magic)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(130, 21))
        self.label_37.setMaximumSize(QSize(130, 21))
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_37, 0, 2, 1, 1)

        self.label_38 = QLabel(self.magic)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(130, 21))
        self.label_38.setMaximumSize(QSize(130, 21))
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_38, 0, 0, 1, 1)

        self.label_39 = QLabel(self.magic)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(130, 21))
        self.label_39.setMaximumSize(QSize(130, 21))
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.label_39, 0, 1, 1, 1)


        self.magic_base_goals.addLayout(self.gridLayout_9)


        self.verticalLayout_8.addLayout(self.magic_base_goals)

        self.layout_magic_amount_left_to_buy = QVBoxLayout()
        self.layout_magic_amount_left_to_buy.setSpacing(0)
        self.layout_magic_amount_left_to_buy.setObjectName(u"layout_magic_amount_left_to_buy")
        self.name_magic_amount_left_to_buy = QLabel(self.magic)
        self.name_magic_amount_left_to_buy.setObjectName(u"name_magic_amount_left_to_buy")
        self.name_magic_amount_left_to_buy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_magic_amount_left_to_buy.addWidget(self.name_magic_amount_left_to_buy)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_40 = QLabel(self.magic)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(130, 21))
        self.label_40.setMaximumSize(QSize(130, 21))
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_40, 2, 0, 1, 1)

        self.magic_exp_cost_cap = QLabel(self.magic)
        self.magic_exp_cost_cap.setObjectName(u"magic_exp_cost_cap")
        self.magic_exp_cost_cap.setMinimumSize(QSize(130, 21))
        self.magic_exp_cost_cap.setMaximumSize(QSize(130, 21))
        self.magic_exp_cost_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.magic_exp_cost_cap, 3, 1, 1, 1)

        self.magic_exp_cost_power = QLabel(self.magic)
        self.magic_exp_cost_power.setObjectName(u"magic_exp_cost_power")
        self.magic_exp_cost_power.setMinimumSize(QSize(130, 21))
        self.magic_exp_cost_power.setMaximumSize(QSize(130, 21))
        self.magic_exp_cost_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.magic_exp_cost_power, 3, 0, 1, 1)

        self.label_41 = QLabel(self.magic)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(130, 21))
        self.label_41.setMaximumSize(QSize(130, 21))
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_42 = QLabel(self.magic)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(130, 21))
        self.label_42.setMaximumSize(QSize(130, 21))
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_42, 2, 1, 1, 1)

        self.label_43 = QLabel(self.magic)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(130, 21))
        self.label_43.setMaximumSize(QSize(130, 21))
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_43, 0, 1, 1, 1)

        self.label_44 = QLabel(self.magic)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(130, 21))
        self.label_44.setMaximumSize(QSize(130, 21))
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_44, 0, 2, 1, 1)

        self.label_45 = QLabel(self.magic)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(130, 21))
        self.label_45.setMaximumSize(QSize(130, 21))
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.label_45, 2, 2, 1, 1)

        self.magic_exp_cost_bars = QLabel(self.magic)
        self.magic_exp_cost_bars.setObjectName(u"magic_exp_cost_bars")
        self.magic_exp_cost_bars.setMinimumSize(QSize(130, 21))
        self.magic_exp_cost_bars.setMaximumSize(QSize(130, 21))
        self.magic_exp_cost_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.magic_exp_cost_bars, 3, 2, 1, 1)

        self.magic_amount_left_to_buy_bar = QPushButton(self.magic)
        self.magic_amount_left_to_buy_bar.setObjectName(u"magic_amount_left_to_buy_bar")
        self.magic_amount_left_to_buy_bar.setMinimumSize(QSize(21, 21))
        self.magic_amount_left_to_buy_bar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.magic_amount_left_to_buy_bar.setIcon(icon)

        self.gridLayout_10.addWidget(self.magic_amount_left_to_buy_bar, 1, 2, 1, 1)

        self.magic_amount_left_to_buy_cap = QPushButton(self.magic)
        self.magic_amount_left_to_buy_cap.setObjectName(u"magic_amount_left_to_buy_cap")
        self.magic_amount_left_to_buy_cap.setMinimumSize(QSize(21, 21))
        self.magic_amount_left_to_buy_cap.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.magic_amount_left_to_buy_cap.setIcon(icon)

        self.gridLayout_10.addWidget(self.magic_amount_left_to_buy_cap, 1, 1, 1, 1)

        self.magic_amount_left_to_buy_power = QPushButton(self.magic)
        self.magic_amount_left_to_buy_power.setObjectName(u"magic_amount_left_to_buy_power")
        self.magic_amount_left_to_buy_power.setMinimumSize(QSize(21, 21))
        self.magic_amount_left_to_buy_power.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.magic_amount_left_to_buy_power.setIcon(icon)

        self.gridLayout_10.addWidget(self.magic_amount_left_to_buy_power, 1, 0, 1, 1)


        self.layout_magic_amount_left_to_buy.addLayout(self.gridLayout_10)


        self.verticalLayout_8.addLayout(self.layout_magic_amount_left_to_buy)


        self.gridLayout_12.addWidget(self.magic, 0, 1, 1, 1)

        self.em = QWidget(self.gridLayoutWidget)
        self.em.setObjectName(u"em")
        self.verticalLayout = QVBoxLayout(self.em)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Title_3 = QLabel(self.em)
        self.Title_3.setObjectName(u"Title_3")

        self.verticalLayout.addWidget(self.Title_3)

        self.layout_em_goal_ratio = QVBoxLayout()
        self.layout_em_goal_ratio.setSpacing(0)
        self.layout_em_goal_ratio.setObjectName(u"layout_em_goal_ratio")
        self.header_17 = QLabel(self.em)
        self.header_17.setObjectName(u"header_17")
        self.header_17.setMinimumSize(QSize(395, 21))
        self.header_17.setMaximumSize(QSize(16777215, 21))
        self.header_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_em_goal_ratio.addWidget(self.header_17)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.em_edit_goal_ratio_energy = QLineEdit(self.em)
        self.em_edit_goal_ratio_energy.setObjectName(u"em_edit_goal_ratio_energy")
        self.em_edit_goal_ratio_energy.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.em_edit_goal_ratio_energy.setInputMethodHints(Qt.InputMethodHint.ImhNone)

        self.gridLayout_21.addWidget(self.em_edit_goal_ratio_energy, 1, 0, 1, 1)

        self.label_78 = QLabel(self.em)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(130, 21))
        self.label_78.setAutoFillBackground(False)
        self.label_78.setStyleSheet(u"")
        self.label_78.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.label_78, 0, 0, 1, 1)

        self.label_79 = QLabel(self.em)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(130, 21))
        self.label_79.setFont(font1)
        self.label_79.setAutoFillBackground(False)
        self.label_79.setStyleSheet(u"")
        self.label_79.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.label_79, 0, 1, 1, 1)

        self.em_edit_goal_ratio_magic = QLineEdit(self.em)
        self.em_edit_goal_ratio_magic.setObjectName(u"em_edit_goal_ratio_magic")

        self.gridLayout_21.addWidget(self.em_edit_goal_ratio_magic, 1, 1, 1, 1)

        self.label_80 = QLabel(self.em)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(130, 21))
        self.label_80.setAutoFillBackground(False)
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.label_80, 0, 2, 1, 1)

        self.em_edit_goal_em_ratio = QLabel(self.em)
        self.em_edit_goal_em_ratio.setObjectName(u"em_edit_goal_em_ratio")
        self.em_edit_goal_em_ratio.setMinimumSize(QSize(130, 21))
        self.em_edit_goal_em_ratio.setAutoFillBackground(False)
        self.em_edit_goal_em_ratio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.em_edit_goal_em_ratio, 1, 2, 1, 1)


        self.layout_em_goal_ratio.addLayout(self.gridLayout_21)


        self.verticalLayout.addLayout(self.layout_em_goal_ratio)

        self.layout_em_current_ratio = QVBoxLayout()
        self.layout_em_current_ratio.setSpacing(0)
        self.layout_em_current_ratio.setObjectName(u"layout_em_current_ratio")
        self.header_19 = QLabel(self.em)
        self.header_19.setObjectName(u"header_19")
        self.header_19.setMinimumSize(QSize(395, 21))
        self.header_19.setMaximumSize(QSize(16777215, 21))
        self.header_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_em_current_ratio.addWidget(self.header_19)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_84 = QLabel(self.em)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(130, 21))
        self.label_84.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.label_84, 0, 1, 1, 1)

        self.label_85 = QLabel(self.em)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(130, 21))
        self.label_85.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.label_85, 0, 0, 1, 1)

        self.label_86 = QLabel(self.em)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(130, 21))
        self.label_86.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.label_86, 0, 2, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.em_cr_power = QLabel(self.em)
        self.em_cr_power.setObjectName(u"em_cr_power")
        self.em_cr_power.setMinimumSize(QSize(105, 21))
        self.em_cr_power.setMaximumSize(QSize(130, 21))
        self.em_cr_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.em_cr_power)

        self.em_cr_power_checker = QLabel(self.em)
        self.em_cr_power_checker.setObjectName(u"em_cr_power_checker")
        self.em_cr_power_checker.setMinimumSize(QSize(25, 21))
        self.em_cr_power_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.em_cr_power_checker)


        self.gridLayout_23.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.em_cr_cap = QLabel(self.em)
        self.em_cr_cap.setObjectName(u"em_cr_cap")
        self.em_cr_cap.setMinimumSize(QSize(105, 21))
        self.em_cr_cap.setMaximumSize(QSize(130, 21))
        self.em_cr_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.em_cr_cap)

        self.em_cr_cap_checker = QLabel(self.em)
        self.em_cr_cap_checker.setObjectName(u"em_cr_cap_checker")
        self.em_cr_cap_checker.setMinimumSize(QSize(25, 21))
        self.em_cr_cap_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.em_cr_cap_checker)


        self.gridLayout_23.addLayout(self.horizontalLayout_12, 1, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.em_cr_bars = QLabel(self.em)
        self.em_cr_bars.setObjectName(u"em_cr_bars")
        self.em_cr_bars.setMinimumSize(QSize(105, 21))
        self.em_cr_bars.setMaximumSize(QSize(130, 21))
        self.em_cr_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.em_cr_bars)

        self.em_cr_bar_checker = QLabel(self.em)
        self.em_cr_bar_checker.setObjectName(u"em_cr_bar_checker")
        self.em_cr_bar_checker.setMinimumSize(QSize(25, 21))
        self.em_cr_bar_checker.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.em_cr_bar_checker)


        self.gridLayout_23.addLayout(self.horizontalLayout_13, 1, 2, 1, 1)


        self.layout_em_current_ratio.addLayout(self.gridLayout_23)


        self.verticalLayout.addLayout(self.layout_em_current_ratio)

        self.em_optimal_energy_at_that_ratio = QVBoxLayout()
        self.em_optimal_energy_at_that_ratio.setSpacing(0)
        self.em_optimal_energy_at_that_ratio.setObjectName(u"em_optimal_energy_at_that_ratio")
        self.header_9 = QLabel(self.em)
        self.header_9.setObjectName(u"header_9")
        self.header_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.em_optimal_energy_at_that_ratio.addWidget(self.header_9)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.em_optimal_energy_for_magic_power = QLabel(self.em)
        self.em_optimal_energy_for_magic_power.setObjectName(u"em_optimal_energy_for_magic_power")
        self.em_optimal_energy_for_magic_power.setMinimumSize(QSize(130, 21))
        self.em_optimal_energy_for_magic_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.em_optimal_energy_for_magic_power, 1, 0, 1, 1)

        self.em_optimal_energy_for_magic_bar = QLabel(self.em)
        self.em_optimal_energy_for_magic_bar.setObjectName(u"em_optimal_energy_for_magic_bar")
        self.em_optimal_energy_for_magic_bar.setMinimumSize(QSize(130, 21))
        self.em_optimal_energy_for_magic_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.em_optimal_energy_for_magic_bar, 1, 2, 1, 1)

        self.em_optimal_energy_for_magic_cap = QLabel(self.em)
        self.em_optimal_energy_for_magic_cap.setObjectName(u"em_optimal_energy_for_magic_cap")
        self.em_optimal_energy_for_magic_cap.setMinimumSize(QSize(130, 21))
        self.em_optimal_energy_for_magic_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.em_optimal_energy_for_magic_cap, 1, 1, 1, 1)

        self.label_24 = QLabel(self.em)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(130, 21))
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_24, 0, 2, 1, 1)

        self.label_25 = QLabel(self.em)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(130, 21))
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_26 = QLabel(self.em)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(130, 21))
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.label_26, 0, 1, 1, 1)


        self.em_optimal_energy_at_that_ratio.addLayout(self.gridLayout_11)


        self.verticalLayout.addLayout(self.em_optimal_energy_at_that_ratio)

        self.layout_em_amount_left_to_buy = QVBoxLayout()
        self.layout_em_amount_left_to_buy.setSpacing(0)
        self.layout_em_amount_left_to_buy.setObjectName(u"layout_em_amount_left_to_buy")
        self.name_em_amount_left_to_buy = QLabel(self.em)
        self.name_em_amount_left_to_buy.setObjectName(u"name_em_amount_left_to_buy")
        self.name_em_amount_left_to_buy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_em_amount_left_to_buy.addWidget(self.name_em_amount_left_to_buy)

        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.label_93 = QLabel(self.em)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(130, 21))
        self.label_93.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.label_93, 2, 0, 1, 1)

        self.em_exp_cost_cap = QLabel(self.em)
        self.em_exp_cost_cap.setObjectName(u"em_exp_cost_cap")
        self.em_exp_cost_cap.setMinimumSize(QSize(130, 21))
        self.em_exp_cost_cap.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.em_exp_cost_cap, 3, 1, 1, 1)

        self.em_exp_cost_power = QLabel(self.em)
        self.em_exp_cost_power.setObjectName(u"em_exp_cost_power")
        self.em_exp_cost_power.setMinimumSize(QSize(130, 21))
        self.em_exp_cost_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.em_exp_cost_power, 3, 0, 1, 1)

        self.label_94 = QLabel(self.em)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(130, 21))
        self.label_94.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.label_94, 0, 0, 1, 1)

        self.label_95 = QLabel(self.em)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(130, 21))
        self.label_95.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.label_95, 2, 1, 1, 1)

        self.label_96 = QLabel(self.em)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(130, 21))
        self.label_96.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.label_96, 0, 1, 1, 1)

        self.label_97 = QLabel(self.em)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(130, 21))
        self.label_97.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.label_97, 0, 2, 1, 1)

        self.label_98 = QLabel(self.em)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(130, 21))
        self.label_98.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.label_98, 2, 2, 1, 1)

        self.em_exp_cost_bars = QLabel(self.em)
        self.em_exp_cost_bars.setObjectName(u"em_exp_cost_bars")
        self.em_exp_cost_bars.setMinimumSize(QSize(130, 21))
        self.em_exp_cost_bars.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.em_exp_cost_bars, 3, 2, 1, 1)

        self.em_amount_left_to_buy_bar = QPushButton(self.em)
        self.em_amount_left_to_buy_bar.setObjectName(u"em_amount_left_to_buy_bar")
        self.em_amount_left_to_buy_bar.setMinimumSize(QSize(21, 21))
        self.em_amount_left_to_buy_bar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.em_amount_left_to_buy_bar.setIcon(icon)

        self.gridLayout_26.addWidget(self.em_amount_left_to_buy_bar, 1, 2, 1, 1)

        self.em_amount_left_to_buy_cap = QPushButton(self.em)
        self.em_amount_left_to_buy_cap.setObjectName(u"em_amount_left_to_buy_cap")
        self.em_amount_left_to_buy_cap.setMinimumSize(QSize(21, 21))
        self.em_amount_left_to_buy_cap.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.em_amount_left_to_buy_cap.setIcon(icon)

        self.gridLayout_26.addWidget(self.em_amount_left_to_buy_cap, 1, 1, 1, 1)

        self.em_amount_left_to_buy_power = QPushButton(self.em)
        self.em_amount_left_to_buy_power.setObjectName(u"em_amount_left_to_buy_power")
        self.em_amount_left_to_buy_power.setMinimumSize(QSize(21, 21))
        self.em_amount_left_to_buy_power.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.em_amount_left_to_buy_power.setIcon(icon)

        self.gridLayout_26.addWidget(self.em_amount_left_to_buy_power, 1, 0, 1, 1)


        self.layout_em_amount_left_to_buy.addLayout(self.gridLayout_26)


        self.verticalLayout.addLayout(self.layout_em_amount_left_to_buy)


        self.gridLayout_12.addWidget(self.em, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ngu-helper", None))
        self.Title_Of_The_Tab.setText(QCoreApplication.translate("MainWindow", u"R : A : T : I : Oz", None))
        self.Title_Of_The_Tab.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"0", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"ENERGY", None))
        self.Title.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"misc", None))
        self.header_3.setText(QCoreApplication.translate("MainWindow", u"Your Base Energy Stats", None))
        self.header_3.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.base_e_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.base_e_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_14.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_15.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.base_e_pow.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.base_e_pow.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.base_e_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.base_e_bar.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_16.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.header_2.setText(QCoreApplication.translate("MainWindow", u"Your Current Energy Ratio", None))
        self.header_2.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_6.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_7.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_8.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.CER_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CER_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.energy_CR_power_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CER_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CER_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.energy_CR_cap_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CER_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CER_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.energy_CR_bar_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.header_1.setText(QCoreApplication.translate("MainWindow", u"Your Goal Energy Ratio", None))
        self.header_1.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.energy_goal_edit_power.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.energy_goal_edit_cap.setText(QCoreApplication.translate("MainWindow", u"37500", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_3.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_4.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.energy_goal_edit_bar.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_5.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.header_4.setText(QCoreApplication.translate("MainWindow", u"Your Base Energy Goals", None))
        self.header_4.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.energy_base_goal_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_base_goal_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.energy_base_goal_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_base_goal_bar.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.energy_base_goal_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_base_goal_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_23.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_21.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_22.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.amount_left_to_buy_energy.setText(QCoreApplication.translate("MainWindow", u"Amount Left To Buy Until Your Energy Goal\n"
"(Total Cost: 0 EXP)", None))
        self.amount_left_to_buy_energy.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Power EXP Cost", None))
        self.label_36.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.energy_exp_cost_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_exp_cost_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.energy_exp_cost_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_exp_cost_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_30.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Cap EXP Cost", None))
        self.label_35.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_29.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_28.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Bars EXP Cost", None))
        self.label_34.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.energy_exp_cost_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_exp_cost_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.energy_amount_left_to_buy_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_amount_left_to_buy_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.energy_amount_left_to_buy_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Title_4.setText(QCoreApplication.translate("MainWindow", u"R3", None))
        self.Title_4.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"misc", None))
        self.header_13.setText(QCoreApplication.translate("MainWindow", u"Your Base R3 Stats", None))
        self.header_13.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_31.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_base_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_base_bar.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_32.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_base_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_base_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_33.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_base_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_base_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.header_14.setText(QCoreApplication.translate("MainWindow", u"Your Current R3 Ratio", None))
        self.header_14.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_63.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_64.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_65.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_cr_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_cr_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.r3_cr_power_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_cr_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_cr_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.r3_cr_cap_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_cr_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_cr_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.r3_cr_bar_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.header_15.setText(QCoreApplication.translate("MainWindow", u"Your Goal R3 Ratio", None))
        self.header_15.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.r3_goal_edit_power.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_66.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_67.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_goal_edit_cap.setText(QCoreApplication.translate("MainWindow", u"40000", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_68.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_goal_edit_bar.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.header_16.setText(QCoreApplication.translate("MainWindow", u"Your Base R3 Goals", None))
        self.header_16.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.r3_base_goal_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_base_goal_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.r3_base_goal_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_base_goal_bar.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.r3_base_goal_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_base_goal_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_69.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_70.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_71.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.name_r3_amount_left_to_buy.setText(QCoreApplication.translate("MainWindow", u"Amount Left To Buy Until Your R3 Goal\n"
"(Total Cost: 0 EXP)", None))
        self.name_r3_amount_left_to_buy.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Power EXP Cost", None))
        self.label_72.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_exp_cost_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_exp_cost_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.r3_exp_cost_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_exp_cost_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_73.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Cap EXP Cost", None))
        self.label_74.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_75.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_76.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Bars EXP Cost", None))
        self.label_77.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.r3_exp_cost_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_exp_cost_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.r3_amount_left_to_buy_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_amount_left_to_buy_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r3_amount_left_to_buy_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Title_2.setText(QCoreApplication.translate("MainWindow", u"MAGIC", None))
        self.Title_2.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"misc", None))
        self.header_5.setText(QCoreApplication.translate("MainWindow", u"Your Base Magic Stats", None))
        self.header_5.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_17.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.base_m_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.base_m_bar.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_18.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.base_m_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.base_m_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_19.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.base_m_pow.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.base_m_pow.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.header_6.setText(QCoreApplication.translate("MainWindow", u"Your Current Magic Ratio", None))
        self.header_6.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_9.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_10.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_11.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.CMR_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CMR_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.magic_CR_power_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CMR_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CMR_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.magic_CR_cap_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CMR_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.CMR_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.magic_CR_bar_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.header_7.setText(QCoreApplication.translate("MainWindow", u"Your Goal Magic Ratio", None))
        self.header_7.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.magic_goal_edit_power.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_13.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_27.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.magic_goal_edit_cap.setText(QCoreApplication.translate("MainWindow", u"40000", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_20.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.magic_goal_edit_bar.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.header_8.setText(QCoreApplication.translate("MainWindow", u"Your Base Magic Goals", None))
        self.header_8.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.magic_base_goal_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_base_goal_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.magic_base_goal_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_base_goal_bar.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.magic_base_goal_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_base_goal_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_37.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_38.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_39.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.name_magic_amount_left_to_buy.setText(QCoreApplication.translate("MainWindow", u"Amount Left To Buy Until Your Magic Goal\n"
"(Total Cost: 0 EXP)", None))
        self.name_magic_amount_left_to_buy.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Power EXP Cost", None))
        self.label_40.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.magic_exp_cost_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_exp_cost_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.magic_exp_cost_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_exp_cost_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_41.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Cap EXP Cost", None))
        self.label_42.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_43.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_44.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Bars EXP Cost", None))
        self.label_45.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.magic_exp_cost_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_exp_cost_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.magic_amount_left_to_buy_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_amount_left_to_buy_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magic_amount_left_to_buy_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Title_3.setText(QCoreApplication.translate("MainWindow", u"ENERGY : MAGIC", None))
        self.Title_3.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"misc", None))
        self.header_17.setText(QCoreApplication.translate("MainWindow", u"Your Goal Energy:Magic Ratio", None))
        self.header_17.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.em_edit_goal_ratio_energy.setText(QCoreApplication.translate("MainWindow", u"6.0", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Energy", None))
        self.label_78.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Magic", None))
        self.label_79.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.em_edit_goal_ratio_magic.setText(QCoreApplication.translate("MainWindow", u"2.0", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Goal Energy:Magic", None))
        self.label_80.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.em_edit_goal_em_ratio.setText(QCoreApplication.translate("MainWindow", u"3.00 : 1", None))
        self.em_edit_goal_em_ratio.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.header_19.setText(QCoreApplication.translate("MainWindow", u"Your Current Energy:Magic Ratio", None))
        self.header_19.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_84.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_85.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_86.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.em_cr_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_cr_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.em_cr_power_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_cr_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_cr_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.em_cr_cap_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_cr_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_cr_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.em_cr_bar_checker.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.header_9.setText(QCoreApplication.translate("MainWindow", u"Optimal Energy for your Magic at that Ratio", None))
        self.header_9.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.em_optimal_energy_for_magic_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_optimal_energy_for_magic_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.em_optimal_energy_for_magic_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_optimal_energy_for_magic_bar.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.em_optimal_energy_for_magic_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_optimal_energy_for_magic_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_24.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_25.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_26.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.name_em_amount_left_to_buy.setText(QCoreApplication.translate("MainWindow", u"Amount Left To Buy Until Your Energy:Magic Goal\n"
"(Total Cost: 0 EXP)", None))
        self.name_em_amount_left_to_buy.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"1", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Power EXP Cost", None))
        self.label_93.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.em_exp_cost_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_exp_cost_cap.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.em_exp_cost_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_exp_cost_power.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_94.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Cap EXP Cost", None))
        self.label_95.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Cap", None))
        self.label_96.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
        self.label_97.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Bars EXP Cost", None))
        self.label_98.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"2", None))
        self.em_exp_cost_bars.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_exp_cost_bars.setProperty("type_of_header", QCoreApplication.translate("MainWindow", u"3", None))
        self.em_amount_left_to_buy_bar.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_amount_left_to_buy_cap.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.em_amount_left_to_buy_power.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

