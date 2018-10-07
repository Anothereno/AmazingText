# -*- coding: utf-8 -*-

"""

Здесь обычно пишется описание программы, но пока мы над ней работаем, пишите тут свои идеи, например:

Функция сохранения


"""


import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt

import gui


class EditorWindow(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.box)

    def box(self):
        QMessageBox.warning(self, 'Warning', "LOL!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = EditorWindow()
    form.show()
    app.exec()
