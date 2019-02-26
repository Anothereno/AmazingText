# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.width = 850
        self.height = 470
        MainWindow.resize(self.width, self.height)
        self.setWindowIcon(QIcon('logo.png'))
        """Main widget."""
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        """Button Start."""
        self.btn_start = QtWidgets.QPushButton(self.centralWidget)
        self.btn_start.setGeometry(QtCore.QRect(625, 400, 100, 40))
        self.btn_start.setObjectName("btn_start")
        self.btn_start.setShortcut('Ctrl+Return')
        """Button Stop."""
        self.btn_stop = QtWidgets.QPushButton(self.centralWidget)
        self.btn_stop.setGeometry(QtCore.QRect(730, 400, 100, 40))
        self.btn_stop.setObjectName("btn_stop")
        MainWindow.setCentralWidget(self.centralWidget)
        """Menu."""
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu('File')
        viewMenu = self.mainMenu.addMenu('View')
        """Menu actions."""
        """Save."""
        self.save_button = QAction(QIcon('save.png'), 'Save', self)
        self.save_button.setShortcut('Ctrl+S')
        fileMenu.addAction(self.save_button)
        """Open."""
        self.open_button = QAction(QIcon('open.png'), 'Open', self)
        self.open_button.setShortcut('Ctrl+O')
        fileMenu.addAction(self.open_button)
        """Exit."""
        exit_button = QAction(QIcon('power.png'), 'Exit', self)
        exit_button.triggered.connect(self.close)
        fileMenu.addAction(exit_button)
        """BG set."""
        self.set_bg_image = QAction(QIcon('eye.png'), 'Set wallpaper', self)
        viewMenu.addAction(self.set_bg_image)

        """Bar_1 Buttons"""
        """Button Bar_1, coord_1."""
        self.btn_bar_1_coord_1 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_bar_1_coord_1.setGeometry(QtCore.QRect(90, 10, 70, 40))
        self.btn_bar_1_coord_1.setObjectName("btn_bar_1_coord_1")
        self.btn_bar_1_coord_1.setToolTip("Top left corner of the rectangle.")
        """Button Bar_1, coord_2."""
        self.btn_bar_1_coord_2 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_bar_1_coord_2.setGeometry(QtCore.QRect(90, 60, 70, 40))
        self.btn_bar_1_coord_2.setObjectName("btn_bar_1_coord_2")
        self.btn_bar_1_coord_2.setToolTip("Bottom right corner of the rectangle.")
        """Button Bar_1, value."""
        self.btn_bar_1_value = QtWidgets.QPushButton(self.centralWidget)
        self.btn_bar_1_value.setGeometry(QtCore.QRect(90, 120, 55, 40))
        self.btn_bar_1_value.setObjectName("btn_bar_1_value")
        self.btn_bar_1_value.setToolTip("Set values.")
        """Bar_1, color"""
        self.btn_bar_1_color = QtWidgets.QPushButton("Color 1", self.centralWidget)
        self.btn_bar_1_color.setGeometry(QtCore.QRect(90, 180, 55, 40))
        self.btn_bar_1_color.setObjectName("btn_bar_1_color")
        self.btn_bar_1_color.setToolTip("Pick a color.")

        """Bar_1 Edits"""
        """Edit Bar_1, coord_1_x"""
        self.ed_bar_1_coord_1_x = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_coord_1_x.setGeometry(QtCore.QRect(50, 10, 35, 18))
        self.ed_bar_1_coord_1_x.setObjectName("ed_bar_1_coord_1_x")
        """Edit Bar_1, coord_1_y"""
        self.ed_bar_1_coord_1_y = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_coord_1_y.setGeometry(QtCore.QRect(50, 30, 35, 18))
        self.ed_bar_1_coord_1_y.setObjectName("ed_bar_1_coord_1_y")
        """Edit Bar_1, coord_2_x"""
        self.ed_bar_1_coord_2_x = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_coord_2_x.setGeometry(QtCore.QRect(50, 60, 35, 18))
        self.ed_bar_1_coord_2_x.setObjectName("ed_bar_1_coord_2_x")
        """Edit Bar_1, coord_2_y"""
        self.ed_bar_1_coord_2_y = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_coord_2_y.setGeometry(QtCore.QRect(50, 80, 35, 18))
        self.ed_bar_1_coord_2_y.setObjectName("ed_bar_1_coord_2_y")
        """Edit Bar_1, value"""
        self.ed_bar_1_value = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_value.setGeometry(QtCore.QRect(50, 110, 35, 18))
        self.ed_bar_1_value.setObjectName("ed_bar_1_value")
        """Edit Bar_1, refresh"""
        self.ed_bar_1_refresh = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_refresh.setGeometry(QtCore.QRect(50, 130, 35, 19))
        self.ed_bar_1_refresh.setObjectName("ed_bar_1_refresh")
        """Edit Bar_1, Action"""
        self.ed_bar_1_Action = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_Action.setGeometry(QtCore.QRect(50, 150, 35, 19))
        self.ed_bar_1_Action.setObjectName("ed_bar_1_Action")
        """Edit Bar_1, color"""
        self.ed_bar_1_color = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_1_color.setGeometry(QtCore.QRect(55, 190, 25, 25))
        self.ed_bar_1_color.setObjectName("ed_bar_1_color")

        """Bar_2 Buttons"""
        """Кнопка Bar_2, coord_1."""
        self.btn_bar_2_coord_1 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_bar_2_coord_1.setGeometry(QtCore.QRect(280, 10, 70, 40))
        self.btn_bar_2_coord_1.setObjectName("Bar_2, coord_1")
        self.btn_bar_2_coord_1.setToolTip("Top left corner of the rectangle.")
        """Кнопка Bar_2, coord_2."""
        self.btn_bar_2_coord_2 = QtWidgets.QPushButton(self.centralWidget)
        self.btn_bar_2_coord_2.setGeometry(QtCore.QRect(280, 60, 70, 40))
        self.btn_bar_2_coord_2.setObjectName("Bar_2, coord_2")
        self.btn_bar_2_coord_2.setToolTip("Bottom right corner of the rectangle.")
        """Кнопка Bar_2, value."""
        self.btn_bar_2_value = QtWidgets.QPushButton(self.centralWidget)
        self.btn_bar_2_value.setGeometry(QtCore.QRect(280, 120, 55, 40))
        self.btn_bar_2_value.setObjectName("Bar_2, value")
        self.btn_bar_2_value.setToolTip("Set values.")
        """Bar_2, color"""
        self.btn_bar_2_color = QtWidgets.QPushButton("Color 2", self.centralWidget)
        self.btn_bar_2_color.setGeometry(QtCore.QRect(280, 180, 55, 40))
        self.btn_bar_2_color.setObjectName("btn_bar_2_color")
        self.btn_bar_2_color.setToolTip("Pick a color.")

        """Bar_2 Edits"""
        """Edit Bar_2, coord_1_x"""
        self.ed_bar_2_coord_1_x = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_coord_1_x.setGeometry(QtCore.QRect(240, 10, 35, 18))
        self.ed_bar_2_coord_1_x.setObjectName("ed_bar_2_coord_1_x")
        """Edit Bar_2, coord_1_y"""
        self.ed_bar_2_coord_1_y = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_coord_1_y.setGeometry(QtCore.QRect(240, 30, 35, 18))
        self.ed_bar_2_coord_1_y.setObjectName("ed_bar_2_coord_1_y")
        """Edit Bar_2, coord_2_x"""
        self.ed_bar_2_coord_2_x = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_coord_2_x.setGeometry(QtCore.QRect(240, 60, 35, 18))
        self.ed_bar_2_coord_2_x.setObjectName("ed_bar_2_coord_2_x")
        """Edit Bar_2, coord_2_y"""
        self.ed_bar_2_coord_2_y = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_coord_2_y.setGeometry(QtCore.QRect(240, 80, 35, 18))
        self.ed_bar_2_coord_2_y.setObjectName("ed_bar_2_coord_2_y")
        """Edit Bar_2, value"""
        self.ed_bar_2_value = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_value.setGeometry(QtCore.QRect(240, 110, 35, 18))
        self.ed_bar_2_value.setObjectName("ed_bar_2_value")
        """Edit Bar_2, refresh"""
        self.ed_bar_2_refresh = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_refresh.setGeometry(QtCore.QRect(240, 130, 35, 18))
        self.ed_bar_2_refresh.setObjectName("ed_bar_2_refresh")
        """Edit Bar_2, Action"""
        self.ed_bar_2_Action = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_Action.setGeometry(QtCore.QRect(240, 150, 35, 18))
        self.ed_bar_2_Action.setObjectName("ed_bar_2_Action")
        """Edit Bar_2, color"""
        self.ed_bar_2_color = QtWidgets.QLineEdit(self.centralWidget)
        self.ed_bar_2_color.setGeometry(QtCore.QRect(245, 190, 25, 25))
        self.ed_bar_2_color.setObjectName("ed_bar_2_color")

        """Statistics."""
        self.bars_statistics = QtWidgets.QTextEdit(self.centralWidget)
        self.bars_statistics.setGeometry(QtCore.QRect(730, 30, 100, 80))
        self.bars_statistics.setObjectName("Bars_statistics")
        self.bars_statistics.setToolTip("What buttons have been pressed.")
        """statistics_label"""
        self.statistics_label = QtWidgets.QLabel("Statistics", self.centralWidget)
        self.statistics_label.setGeometry(QtCore.QRect(730, 10, 100, 20))
        self.statistics_label.setObjectName("statistics_label")
        self.statistics_label.setStyleSheet("color:rgb(0, 0, 0, 255)")
        self.statistics_label.setFont(QtGui.QFont("Times", 12))


        """Cooldown_edits."""
        """Cooldown_edit_1"""
        self.cooldown_edit_1 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_1.setGeometry(QtCore.QRect(100, 300, 50, 20))
        self.cooldown_edit_1.setObjectName("cooldown_edit_1")
        self.cooldown_edit_1.setToolTip("Button")
        self.cooldown_edit_1.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        # self.cooldown_edit_1.setStyleSheet("color:rgb(255, 255, 255, 255)")
        self.cooldown_edit_1.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_2"""
        self.cooldown_edit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_2.setGeometry(QtCore.QRect(250, 300, 50, 20))
        self.cooldown_edit_2.setObjectName("cooldown_edit_2")
        self.cooldown_edit_2.setToolTip("Button")
        self.cooldown_edit_2.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_2.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_3"""
        self.cooldown_edit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_3.setGeometry(QtCore.QRect(400, 300, 50, 20))
        self.cooldown_edit_3.setObjectName("cooldown_edit_3")
        self.cooldown_edit_3.setToolTip("Button")
        self.cooldown_edit_3.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_3.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_4"""
        self.cooldown_edit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_4.setGeometry(QtCore.QRect(550, 300, 50, 20))
        self.cooldown_edit_4.setObjectName("cooldown_edit_4")
        self.cooldown_edit_4.setToolTip("Button")
        self.cooldown_edit_4.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_4.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_5"""
        self.cooldown_edit_5 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_5.setGeometry(QtCore.QRect(700, 300, 50, 20))
        self.cooldown_edit_5.setObjectName("cooldown_edit_5")
        self.cooldown_edit_5.setToolTip("Button")
        self.cooldown_edit_5.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_5.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_6"""
        self.cooldown_edit_6 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_6.setGeometry(QtCore.QRect(100, 350, 50, 20))
        self.cooldown_edit_6.setObjectName("cooldown_edit_6")
        self.cooldown_edit_6.setToolTip("Button")
        self.cooldown_edit_6.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_6.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_7"""
        self.cooldown_edit_7 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_7.setGeometry(QtCore.QRect(250, 350, 50, 20))
        self.cooldown_edit_7.setObjectName("cooldown_edit_7")
        self.cooldown_edit_7.setToolTip("Button")
        self.cooldown_edit_7.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_7.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_8"""
        self.cooldown_edit_8 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_8.setGeometry(QtCore.QRect(400, 350, 50, 20))
        self.cooldown_edit_8.setObjectName("cooldown_edit_8")
        self.cooldown_edit_8.setToolTip("Button")
        self.cooldown_edit_8.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_8.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_9"""
        self.cooldown_edit_9 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_9.setGeometry(QtCore.QRect(550, 350, 50, 20))
        self.cooldown_edit_9.setObjectName("cooldown_edit_9")
        self.cooldown_edit_9.setToolTip("Button")
        self.cooldown_edit_9.setStyleSheet("background-color:rgb(100, 200, 0, 200)")
        self.cooldown_edit_9.setFont(QtGui.QFont("Times", 11))
        """Cooldown_edit_10"""
        self.cooldown_edit_10 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_edit_10.setGeometry(QtCore.QRect(700, 350, 50, 20))
        self.cooldown_edit_10.setObjectName("cooldown_edit_10")
        self.cooldown_edit_10.setToolTip("Button")
        self.cooldown_edit_10.setStyleSheet("background-color:rgba(100, 200, 0, 200)")
        self.cooldown_edit_10.setFont(QtGui.QFont("Times", 11))

        """Cooldown_timers."""
        """Cooldown_timer_1"""
        self.cooldown_timer_1 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_1.setGeometry(QtCore.QRect(60, 300, 25, 20))
        self.cooldown_timer_1.setObjectName("cooldown_timer_1")
        self.cooldown_timer_1.setToolTip("Time")
        self.cooldown_timer_1.setStyleSheet("background-color:rgb(255, 20, 20, 150)")
        self.cooldown_timer_1.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_2"""
        self.cooldown_timer_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_2.setGeometry(QtCore.QRect(210, 300, 25, 20))
        self.cooldown_timer_2.setObjectName("cooldown_timer_2")
        self.cooldown_timer_2.setToolTip("Time")
        self.cooldown_timer_2.setStyleSheet("background-color:rgb(255, 20, 20, 150)")
        self.cooldown_timer_2.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_3"""
        self.cooldown_timer_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_3.setGeometry(QtCore.QRect(360, 300, 25, 20))
        self.cooldown_timer_3.setObjectName("cooldown_timer_3")
        self.cooldown_timer_3.setToolTip("Time")
        self.cooldown_timer_3.setStyleSheet("background-color:rgb(255, 20, 20, 150)")
        self.cooldown_timer_3.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_4"""
        self.cooldown_timer_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_4.setGeometry(QtCore.QRect(510, 300, 25, 20))
        self.cooldown_timer_4.setObjectName("cooldown_timer_4")
        self.cooldown_timer_4.setToolTip("Time")
        self.cooldown_timer_4.setStyleSheet("background-color:rgb(255, 20, 20, 150)")
        self.cooldown_timer_4.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_5"""
        self.cooldown_timer_5 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_5.setGeometry(QtCore.QRect(660, 300, 25, 20))
        self.cooldown_timer_5.setObjectName("cooldown_timer_5")
        self.cooldown_timer_5.setToolTip("Time")
        self.cooldown_timer_5.setStyleSheet("background-color:rgb(255, 20, 20, 150)")
        self.cooldown_timer_5.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_6"""
        self.cooldown_timer_6 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_6.setGeometry(QtCore.QRect(60, 350, 25, 20))
        self.cooldown_timer_6.setObjectName("cooldown_timer_6")
        self.cooldown_timer_6.setToolTip("Time")
        self.cooldown_timer_6.setStyleSheet("background-color:rgb(55, 20, 200, 150)")
        self.cooldown_timer_6.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_7"""
        self.cooldown_timer_7 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_7.setGeometry(QtCore.QRect(210, 350, 25, 20))
        self.cooldown_timer_7.setObjectName("cooldown_timer_7")
        self.cooldown_timer_7.setToolTip("Time")
        self.cooldown_timer_7.setStyleSheet("background-color:rgb(55, 20, 200, 150)")
        self.cooldown_timer_7.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_8"""
        self.cooldown_timer_8 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_8.setGeometry(QtCore.QRect(360, 350, 25, 20))
        self.cooldown_timer_8.setObjectName("cooldown_timer_8")
        self.cooldown_timer_8.setToolTip("Time")
        self.cooldown_timer_8.setStyleSheet("background-color:rgb(55, 20, 200, 150)")
        self.cooldown_timer_8.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_9"""
        self.cooldown_timer_9 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_9.setGeometry(QtCore.QRect(510, 350, 25, 20))
        self.cooldown_timer_9.setObjectName("cooldown_timer_9")
        self.cooldown_timer_9.setToolTip("Time")
        self.cooldown_timer_9.setStyleSheet("background-color:rgb(55, 20, 200, 150)")
        self.cooldown_timer_9.setFont(QtGui.QFont("Times", 11))
        """Cooldown_timer_10"""
        self.cooldown_timer_10 = QtWidgets.QLineEdit(self.centralWidget)
        self.cooldown_timer_10.setGeometry(QtCore.QRect(660, 350, 25, 20))
        self.cooldown_timer_10.setObjectName("cooldown_timer_10")
        self.cooldown_timer_10.setToolTip("Time")
        self.cooldown_timer_10.setStyleSheet("background-color:rgb(55, 20, 200, 150)")
        self.cooldown_timer_10.setFont(QtGui.QFont("Times", 10))

        """Labels_bar_1."""
        """Label_1"""
        self.bar_1_label_1 = QtWidgets.QLabel("x", self.centralWidget)
        self.bar_1_label_1.setGeometry(QtCore.QRect(35, 7, 15, 20))
        self.bar_1_label_1.setObjectName("bar_1_label_1")
        """Label_2"""
        self.bar_1_label_2 = QtWidgets.QLabel("y", self.centralWidget)
        self.bar_1_label_2.setGeometry(QtCore.QRect(35, 25, 15, 20))
        self.bar_1_label_2.setObjectName("bar_1_label_2")
        """Label_3"""
        self.bar_1_label_3 = QtWidgets.QLabel("x", self.centralWidget)
        self.bar_1_label_3.setGeometry(QtCore.QRect(35, 57, 15, 20))
        self.bar_1_label_3.setObjectName("bar_1_label_3")
        """Label_4"""
        self.bar_1_label_4 = QtWidgets.QLabel("y", self.centralWidget)
        self.bar_1_label_4.setGeometry(QtCore.QRect(35, 75, 15, 20))
        self.bar_1_label_4.setObjectName("bar_1_label_4")
        """Label_5"""
        self.bar_1_label_5 = QtWidgets.QLabel("Work%", self.centralWidget)
        self.bar_1_label_5.setGeometry(QtCore.QRect(5, 107, 35, 20))
        self.bar_1_label_5.setObjectName("bar_1_label_5")
        """Label_6"""
        self.bar_1_label_6 = QtWidgets.QLabel("Timer", self.centralWidget)
        self.bar_1_label_6.setGeometry(QtCore.QRect(5, 127, 25, 20))
        self.bar_1_label_6.setObjectName("bar_1_label_6")
        """Label_7"""
        self.bar_1_label_7 = QtWidgets.QLabel("Button", self.centralWidget)
        self.bar_1_label_7.setGeometry(QtCore.QRect(5, 147, 35, 20))
        self.bar_1_label_7.setObjectName("bar_1_label_7")
        """Label_pressed."""
        self.bar_1_label_pressed = QtWidgets.QLabel(self.centralWidget)
        self.bar_1_label_pressed.setGeometry(QtCore.QRect(750, 250, 70, 20))
        self.bar_1_label_pressed.setObjectName("bar_1_label_pressed")

        """Labels_bar_2."""
        """Label_1"""
        self.bar_2_label_1 = QtWidgets.QLabel("x", self.centralWidget)
        self.bar_2_label_1.setGeometry(QtCore.QRect(225, 7, 15, 20))
        self.bar_2_label_1.setObjectName("bar_2_label_1")
        """Label_2"""
        self.bar_2_label_2 = QtWidgets.QLabel("y", self.centralWidget)
        self.bar_2_label_2.setGeometry(QtCore.QRect(225, 25, 15, 20))
        self.bar_2_label_2.setObjectName("bar_2_label_2")
        """Label_3"""
        self.bar_2_label_3 = QtWidgets.QLabel("x", self.centralWidget)
        self.bar_2_label_3.setGeometry(QtCore.QRect(225, 57, 15, 20))
        self.bar_2_label_3.setObjectName("bar_2_label_3")
        """Label_4"""
        self.bar_2_label_4 = QtWidgets.QLabel("y", self.centralWidget)
        self.bar_2_label_4.setGeometry(QtCore.QRect(225, 75, 15, 20))
        self.bar_2_label_4.setObjectName("bar_2_label_4")
        """Label_5"""
        self.bar_2_label_5 = QtWidgets.QLabel("Work%", self.centralWidget)
        self.bar_2_label_5.setGeometry(QtCore.QRect(195, 107, 35, 20))
        self.bar_2_label_5.setObjectName("bar_2_label_5")
        """Label_6"""
        self.bar_2_label_6 = QtWidgets.QLabel("Timer", self.centralWidget)
        self.bar_2_label_6.setGeometry(QtCore.QRect(195, 127, 25, 20))
        self.bar_2_label_6.setObjectName("bar_2_label_6")
        """Label_7"""
        self.bar_2_label_7 = QtWidgets.QLabel("Button", self.centralWidget)
        self.bar_2_label_7.setGeometry(QtCore.QRect(195, 147, 35, 20))
        self.bar_2_label_7.setObjectName("bar_2_label_7")
        """Label_pressed."""
        self.bar_2_label_pressed = QtWidgets.QLabel(self.centralWidget)
        self.bar_2_label_pressed.setGeometry(QtCore.QRect(800, 250, 70, 20))
        self.bar_2_label_pressed.setObjectName("bar_2_label_pressed")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main window"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_bar_1_coord_1.setText(_translate("MainWindow", "Coordinate 1"))
        self.btn_bar_1_coord_2.setText(_translate("MainWindow", "Coordinate 2"))
        self.btn_bar_1_value.setText(_translate("MainWindow", "Values 1"))
        self.btn_bar_2_coord_1.setText(_translate("MainWindow", "Coordinate 1"))
        self.btn_bar_2_coord_2.setText(_translate("MainWindow", "Coordinate 2"))
        self.btn_bar_2_value.setText(_translate("MainWindow", "Values 2"))


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        self.width = 480
        self.height = 270
        HelpWindow.resize(self.width, self.height)
        self.setWindowIcon(QIcon('logo.png'))
        """BG."""
        file = 'Wallpaper.jpg'
        oImage = QImage(file)
        sImage = oImage.scaled(QSize(self.width, self.height))
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        """Main widget."""
        self.centralWidget = QtWidgets.QWidget(HelpWindow)
        self.centralWidget.setObjectName("centralWidget")
        """Labels."""
        """Label_1"""
        self.label_1 = QtWidgets.QLabel("This  software  was  brought  to  you  by", self.centralWidget)
        self.label_1.setGeometry(QtCore.QRect(80, 10, 400, 40))
        self.label_1.setObjectName("label_1")
        self.label_1.setFont(QtGui.QFont("Calibri", 14, QtGui.QFont.Bold))
        HelpWindow.setCentralWidget(self.centralWidget)
        """Label_text"""
        self.Label_mail_message = QtWidgets.QLabel("Give me your ideas on HOW TO IMPROVE the software and \nwhat usefull functions YOU think should be added!", self.centralWidget)
        self.Label_mail_message.setGeometry(QtCore.QRect(10, 180, 300, 40))
        self.Label_mail_message.setObjectName("Label_mail_message")
        self.Label_mail_message.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_mail_message.setFont(QtGui.QFont("Calibri", 14, QtGui.QFont.Bold))
        self.Label_mail_message.adjustSize()
        """Label_mail"""
        self.Label_mail = QtWidgets.QLabel("bot.supp@yandex.ru", self.centralWidget)
        self.Label_mail.setGeometry(QtCore.QRect(160, 230, 300, 40))
        self.Label_mail.setObjectName("Label_mail")
        self.Label_mail.setFont(QtGui.QFont("Times", 16))
        self.Label_mail.adjustSize()
        self.Label_mail.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "HelpWindow"))
