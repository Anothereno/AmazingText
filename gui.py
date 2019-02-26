# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Main window")
        self.width = 800
        self.height = 470
        MainWindow.resize(self.width, self.height)
        self.setWindowIcon(QIcon('logo.png'))
        """Main widget"""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        """Button open"""
        self.open_txt = QtWidgets.QPushButton(self.centralwidget)
        self.open_txt.setGeometry(QtCore.QRect(625, 400, 100, 40))
        self.open_txt.setText("Open")
        """Button save"""
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(525, 400, 100, 40))
        self.save.setText("Save")

        """Menu"""
        self.mainMenu = self.menuBar()
        fileMenu = self.mainMenu.addMenu('File')
        viewMenu = self.mainMenu.addMenu('View')
        langMenu = self.mainMenu.addMenu('Language')
        """Menu actions"""
        """Save"""
        self.save = QAction(QIcon('save.png'), 'Save', self)
        self.save.setShortcut('Ctrl+S')
        fileMenu.addAction(self.save)
        """Open"""
        self.open = QAction(QIcon('open.png'), 'Open', self)
        self.open.setShortcut('Ctrl+O')
        fileMenu.addAction(self.open)
        """Exit"""
        exit = QAction(QIcon('power.png'), 'Exit', self)
        exit.triggered.connect(self.close)
        fileMenu.addAction(exit)

        """Main text field"""
        self.main_field = QtWidgets.QTextEdit(self.centralwidget)
        self.main_field.setGeometry(QtCore.QRect(0, 0, self.width, self.height - 100))

