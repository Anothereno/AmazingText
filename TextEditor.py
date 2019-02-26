# -*- coding: utf-8 -*-

"""

Здесь обычно пишется описание программы, но пока мы над ней работаем, пишите тут свои идеи, например:

Функция открытия не только .txt
Функция сохранения в разных форматах
Изменение шрифта
Контроль версий(сохрание последнего состояния файла, переопределить close)
Checkpoint Thread(temp директория)

"""


import os
import sys
import time
import codecs
from threading import Thread


from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt
import textract

import gui


class EditorWindow(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.open_txt.clicked.connect(self.open_text_file)

    def open_text_file(self):
        # try
        text_file = QFileDialog.getOpenFileName(self, 'Open', '/', "Text files (*.txt)")[0]
        self.text_file_temp = text_file

        f = codecs.open(self.text_file_temp, 'r', 'utf-8').read()
        self.main_field.setPlainText(f)

    def checkpoint(self):
        cp_time_min = 1  # Здесь следует заменить значение на текст из поля LineEdit
        cp_time_sec = cp_time_min * 60
        count_down = 0
        if count_down == cp_time_sec:
            pass
        time.sleep(1)

    def initialize(self):  # Должна ли это быть отдельная функция или все запихнуть в __init__?
        thread = Thread(target=self.checkpoint, args=[])
        thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = EditorWindow()
    form.show()
    app.exec()
