import threading
from PIL import Image, ImageGrab
import os
import time
import pyautogui
import random
import string
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import gui

run = False
stop_event = threading.Event()


class Example(QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.helpMenu.triggered.connect(help_form.show)
        """BG."""
        self.previus_bg()
        """Cooldown button's counters."""
        self.cooldown_counter_1 = 0
        self.cooldown_counter_2 = 0
        self.cooldown_counter_3 = 0
        self.cooldown_counter_4 = 0
        self.cooldown_counter_5 = 0
        self.cooldown_counter_6 = 0
        self.cooldown_counter_7 = 0
        self.cooldown_counter_8 = 0
        self.cooldown_counter_9 = 0
        self.cooldown_counter_10 = 0
        """Menu."""
        self.save_button.triggered.connect(self.save_menu_button)
        self.open_button.triggered.connect(self.open_menu_button)
        self.set_bg_image.triggered.connect(self.set_bg)
        # self.help_button.triggered.connect(self.call_for_help)
        """Nones for checking the existence."""
        self.first_r = 256
        self.valued_first_bar = None
        self.first_center_x = None
        self.first_center_y = None
        self.second_r = 256
        self.valued_second_bar = None
        self.second_center_x = None
        self.second_center_y = None
        self.first_bar_pressed_counter = 0
        self.second_bar_pressed_counter = 0

        """Buttons Start, Stop."""
        self.btn_start.clicked.connect(self.start_software)
        self.btn_stop.clicked.connect(self.stop_software)
        """Bar_1 Buttons."""
        self.btn_bar_1_coord_1.clicked.connect(lambda: self.find_mouse_position(self.ed_bar_1_coord_1_x,
                                                                                self.ed_bar_1_coord_1_y))
        self.btn_bar_1_coord_2.clicked.connect(lambda: self.find_mouse_position(self.ed_bar_1_coord_2_x,
                                                                                self.ed_bar_1_coord_2_y))
        self.btn_bar_1_value.clicked.connect(self.value_first_bar)
        self.btn_bar_1_color.clicked.connect(self.first_bar_color)

        """Bar_2 Buttons."""
        self.btn_bar_2_coord_1.clicked.connect(lambda: self.find_mouse_position(self.ed_bar_2_coord_1_x,
                                                                                self.ed_bar_2_coord_1_y))
        self.btn_bar_2_coord_2.clicked.connect(lambda: self.find_mouse_position(self.ed_bar_2_coord_2_x,
                                                                                self.ed_bar_2_coord_2_y))
        self.btn_bar_2_value.clicked.connect(self.value_second_bar)
        self.btn_bar_2_color.clicked.connect(self.second_bar_color)

    def find_mouse_position(self, coordinate_x_entry, coordinate_y_entry):
        """Нахождение позиции указателя мыши."""

        time.sleep(1)
        h_x, h_y = pyautogui.position()
        h_x = str(h_x)
        h_y = str(h_y)
        coordinate_x_entry.setText(h_x)
        coordinate_y_entry.setText(h_y)

    def value_first_bar(self):
        """Нахождение заданной величины в прямоугольнике."""

        temp = int(self.ed_bar_1_coord_2_x.text()) - int(self.ed_bar_1_coord_1_x.text())
        res_hp = int(self.ed_bar_1_coord_1_x.text()) + (temp * int(self.ed_bar_1_value.text()) / 100)
        res_hp = res_hp // 1
        self.valued_first_bar = res_hp
        print(self.valued_first_bar)

        """Нахождение центра."""
        avr_x = int(self.ed_bar_1_coord_1_x.text()) + (int(self.ed_bar_1_coord_2_x.text()) - int(self.ed_bar_1_coord_1_x.text()) // 2)
        self.first_center_x = avr_x
        print(self.first_center_x)
        avr_y = int(self.ed_bar_1_coord_1_y.text()) + ((int(self.ed_bar_1_coord_2_y.text()) - int(self.ed_bar_1_coord_1_y.text())) // 2)
        self.first_center_y = avr_y
        print(self.first_center_y)

    def value_second_bar(self):
        """Нахождение заданной величины в прямоугольнике."""

        temp = int(self.ed_bar_2_coord_2_x.text()) - int(self.ed_bar_2_coord_1_x.text())
        res_hp = int(self.ed_bar_2_coord_1_x.text()) + (temp * int(self.ed_bar_2_value.text()) / 100)
        res_hp = res_hp // 1
        self.valued_second_bar = res_hp
        print(self.valued_second_bar)

        """Нахождение центра."""
        avr_x = int(self.ed_bar_2_coord_1_x.text()) + (int(self.ed_bar_2_coord_2_x.text()) - int(self.ed_bar_2_coord_1_x.text()) // 2)
        self.second_center_x = avr_x
        print(self.second_center_x)
        avr_y = int(self.ed_bar_2_coord_1_y.text()) + ((int(self.ed_bar_2_coord_2_y.text()) - int(self.ed_bar_2_coord_1_y.text())) // 2)
        self.second_center_y = avr_y
        print(self.second_center_y)

    def first_bar_analizer(self):
        """Проверка цвета пикселя."""

        x = self.valued_first_bar
        y = self.first_center_y

        if not run:
            stop_event.set()
        else:
            time.sleep(int(self.ed_bar_1_refresh.text()))

            img = ImageGrab.grab()
            img.save("firstscreen.bmp", "BMP")

            image = Image.open("firstscreen.bmp")
            pix = image.load()

            if pix[x, y][0] <= self.first_r and pix[x, y][1] <= self.first_g and pix[x, y][2] <= self.first_b:
                pyautogui.press(self.ed_bar_1_Action.text())
                self.bars_statistics.append(self.ed_bar_1_Action.text() + ' pressed')

            image.close()
            os.remove("firstscreen.bmp")
            """Очистка оперативной памяти."""
            del (image, img, pix)
            self.first_bar_analizer()

    def second_bar_analizer(self):
        """Проверка цвета пикселя."""

        x = self.valued_second_bar
        y = self.second_center_y

        if not run:
            stop_event.set()
        else:
            time.sleep(int(self.ed_bar_2_refresh.text()))

            img = ImageGrab.grab()
            img.save("secondscreen.bmp", "BMP")
            image = Image.open("secondscreen.bmp")
            pix = image.load()

            if pix[x, y][0] <= self.second_r and pix[x, y][1] <= self.second_g and pix[x, y][2] <= self.second_b:
                pyautogui.press(self.ed_bar_2_Action.text())
                self.bars_statistics.append(self.ed_bar_2_Action.text() + ' pressed')

            image.close()
            os.remove("secondscreen.bmp")
            """Очистка оперативной памяти."""
            del (image, img, pix)
            self.second_bar_analizer()

    # def buttons(self):
    #     """Нажатия кнопок."""
    #
    #     if not run:
    #         stop_event.set()
    #     else:
    #         time.sleep(float(self.Action_timer_1.text()))
    #         pyautogui.press(self.Action_edit_1.text(), int(self.Action_presses_1.text()), float(self.Action_interval_1.text()))
    #
    #         self.buttons()

    def first_bar_color(self):
        time.sleep(1)
        im = ImageGrab.grab()
        mouse_x, mouse_y = pyautogui.position()
        rgb_im = im.convert('RGB')
        self.first_r, self.first_g, self.first_b = rgb_im.getpixel((mouse_x, mouse_y))
        palette = self.ed_bar_1_color.palette()
        palette.setColor(QPalette.Active, QPalette.Base, QColor(self.first_r, self.first_g, self.first_b))
        self.ed_bar_1_color.setPalette(palette)

    def second_bar_color(self):
        time.sleep(1)
        im = ImageGrab.grab()
        mouse_x, mouse_y = pyautogui.position()
        rgb_im = im.convert('RGB')
        self.second_r, self.second_g, self.second_b = rgb_im.getpixel((mouse_x, mouse_y))
        palette = self.ed_bar_2_color.palette()
        palette.setColor(QPalette.Active, QPalette.Base, QColor(self.second_r, self.second_g, self.second_b))
        self.ed_bar_2_color.setPalette(palette)

    def cooldown_buttons(self):
        if not run:
            stop_event.set()
        else:
            if self.cooldown_counter_1 >= int(self.cooldown_timer_1.text()):
                self.cooldown_counter_1 = 0
                pyautogui.press(self.cooldown_edit_1.text())
            if self.cooldown_counter_2 >= int(self.cooldown_timer_2.text()):
                self.cooldown_counter_2 = 0
                pyautogui.press(self.cooldown_edit_2.text())
            if self.cooldown_counter_3 >= int(self.cooldown_timer_3.text()):
                self.cooldown_counter_3 = 0
                pyautogui.press(self.cooldown_edit_3.text())
            if self.cooldown_counter_4 >= int(self.cooldown_timer_4.text()):
                self.cooldown_counter_4 = 0
                pyautogui.press(self.cooldown_edit_4.text())
            if self.cooldown_counter_5 >= int(self.cooldown_timer_5.text()):
                self.cooldown_counter_5 = 0
                pyautogui.press(self.cooldown_edit_5.text())
            if self.cooldown_counter_6 >= int(self.cooldown_timer_6.text()):
                self.cooldown_counter_6 = 0
                pyautogui.press(self.cooldown_edit_6.text())
            if self.cooldown_counter_7 >= int(self.cooldown_timer_7.text()):
                self.cooldown_counter_7 = 0
                pyautogui.press(self.cooldown_edit_7.text())
            if self.cooldown_counter_8 >= int(self.cooldown_timer_8.text()):
                self.cooldown_counter_8 = 0
                pyautogui.press(self.cooldown_edit_8.text())
            if self.cooldown_counter_9 >= int(self.cooldown_timer_9.text()):
                self.cooldown_counter_9 = 0
                pyautogui.press(self.cooldown_edit_9.text())
            if self.cooldown_counter_10 >= int(self.cooldown_timer_10.text()):
                self.cooldown_counter_10 = 0
                pyautogui.press(self.cooldown_edit_10.text())

            time.sleep(1)
            self.cooldown_counter_1 += 1
            self.cooldown_counter_2 += 1
            self.cooldown_counter_3 += 1
            self.cooldown_counter_4 += 1
            self.cooldown_counter_5 += 1
            self.cooldown_counter_6 += 1
            self.cooldown_counter_7 += 1
            self.cooldown_counter_8 += 1
            self.cooldown_counter_9 += 1
            self.cooldown_counter_10 += 1

            self.cooldown_buttons()

    def save_menu_button(self):
        file = QFileDialog.getSaveFileName(self, 'Save', '/config', "Text files (*.txt)")[0]
        if file != "":
            with open(file, 'w') as f:
                """Bar_1"""
                """Bar_1 Coordinates."""
                f.write("Bar 1 coordinate 1 x\n")
                f.write(self.ed_bar_1_coord_1_x.text())
                f.write("\nBar 1 coordinate 1 y\n")
                f.write(self.ed_bar_1_coord_1_y.text())
                f.write("\nBar 1 coordinate 2 x\n")
                f.write(self.ed_bar_1_coord_2_x.text())
                f.write("\nBar 1 coordinate 2 y\n")
                f.write(self.ed_bar_1_coord_2_y.text())
                """Bar_1 Values."""
                f.write("\nValued first bar\n")
                f.write(str(self.valued_first_bar))
                f.write("\nFirst center x\n")
                f.write(str(self.first_center_x))
                f.write("\nFirst center y\n")
                f.write(str(self.first_center_y))
                """Bar_1 Colors."""
                f.write("\nFirst red\n")
                f.write(str(self.first_r))
                f.write("\nFirst green\n")
                f.write(str(self.first_g))
                f.write("\nFirst blue\n")
                f.write(str(self.first_b))
                """Bar_2"""
                """Bar_2 Coordinates."""
                f.write("\nBar 2 coordinate 1 x\n")
                f.write(self.ed_bar_2_coord_1_x.text())
                f.write("\nBar 2 coordinate 1 y\n")
                f.write(self.ed_bar_2_coord_1_y.text())
                f.write("\nBar 2 coordinate 2 x\n")
                f.write(self.ed_bar_2_coord_2_x.text())
                f.write("\nBar 2 coordinate 2 y\n")
                f.write(self.ed_bar_2_coord_2_y.text())
                """Bar_2 Values."""
                f.write("\nValued second bar\n")
                f.write(str(self.valued_second_bar))
                f.write("\nSecond center x\n")
                f.write(str(self.second_center_x))
                f.write("\nSecond center y\n")
                f.write(str(self.second_center_y))
                """Bar_2 Colors."""
                f.write("\nSecond red\n")
                f.write(str(self.second_r))
                f.write("\nSecond greed\n")
                f.write(str(self.second_g))
                f.write("\nSecond blue\n")
                f.write(str(self.second_b))
                """Bar 1 timers and actions."""
                f.write("\nBar 1 refresh\n")
                f.write(self.ed_bar_1_refresh.text())
                f.write("\nBar 1 action\n")
                f.write(self.ed_bar_1_Action.text())
                f.write("\nBar 1 value\n")
                f.write(self.ed_bar_1_value.text())
                """Bar 2 timers and actions."""
                f.write("\nBar 2 refresh\n")
                f.write(self.ed_bar_2_refresh.text())
                f.write("\nBar 2 action\n")
                f.write(self.ed_bar_2_Action.text())
                f.write("\nBar 2 value\n")
                f.write(self.ed_bar_2_value.text())
                """Cooldown."""
                f.write("\ncooldown_timer_1\n")
                f.write(self.cooldown_timer_1.text())
                f.write("\ncooldown_edit_1\n")
                f.write(self.cooldown_edit_1.text())
                f.write("\ncooldown_timer_2\n")
                f.write(self.cooldown_timer_2.text())
                f.write("\ncooldown_edit_2\n")
                f.write(self.cooldown_edit_2.text())
                f.write("\ncooldown_timer_3\n")
                f.write(self.cooldown_timer_3.text())
                f.write("\ncooldown_edit_3\n")
                f.write(self.cooldown_edit_3.text())
                f.write("\ncooldown_timer_4\n")
                f.write(self.cooldown_timer_4.text())
                f.write("\ncooldown_edit_4\n")
                f.write(self.cooldown_edit_4.text())
                f.write("\ncooldown_timer_5\n")
                f.write(self.cooldown_timer_5.text())
                f.write("\ncooldown_edit_5\n")
                f.write(self.cooldown_edit_5.text())
                f.write("\ncooldown_timer_6\n")
                f.write(self.cooldown_timer_6.text())
                f.write("\ncooldown_edit_6\n")
                f.write(self.cooldown_edit_6.text())
                f.write("\ncooldown_timer_7\n")
                f.write(self.cooldown_timer_7.text())
                f.write("\ncooldown_edit_7\n")
                f.write(self.cooldown_edit_7.text())
                f.write("\ncooldown_timer_8\n")
                f.write(self.cooldown_timer_8.text())
                f.write("\ncooldown_edit_8\n")
                f.write(self.cooldown_edit_8.text())
                f.write("\ncooldown_timer_9\n")
                f.write(self.cooldown_timer_9.text())
                f.write("\ncooldown_edit_9\n")
                f.write(self.cooldown_edit_9.text())
                f.write("\ncooldown_timer_10\n")
                f.write(self.cooldown_timer_10.text())
                f.write("\ncooldown_edit_10\n")
                f.write(self.cooldown_edit_10.text())

    def open_menu_button(self):
        file = QFileDialog.getOpenFileName(self, 'Open', '/config', "Text files (*.txt)")[0]

        if file != "":
            with open(file, 'r') as f:
                """Bar_1"""
                """Bar_1 Coordinates."""
                f.readline()
                import re
                self.ed_bar_1_coord_1_x.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_1_coord_1_y.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_1_coord_2_x.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_1_coord_2_y.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                """Bar_1 Values."""
                self.valued_first_bar = float(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.first_center_x = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.first_center_y = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                """Bar_1 Colors."""
                self.first_r = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.first_g = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.first_b = int(re.sub(r'\s+', '', f.readline()))
                palette = self.ed_bar_1_color.palette()
                palette.setColor(QPalette.Active, QPalette.Base, QColor(self.first_r, self.first_g, self.first_b))
                self.ed_bar_1_color.setPalette(palette)
                f.readline()

                """Bar_2"""
                """Bar_2 Coordinates."""
                self.ed_bar_2_coord_1_x.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_2_coord_1_y.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_2_coord_2_x.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_2_coord_2_y.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                """Bar_2 Values."""
                self.valued_second_bar = float(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.second_center_x = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.second_center_y = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                """Bar_2 Colors."""
                self.second_r = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.second_g = int(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.second_b = int(re.sub(r'\s+', '', f.readline()))
                palette = self.ed_bar_2_color.palette()
                palette.setColor(QPalette.Active, QPalette.Base, QColor(self.second_r, self.second_g, self.second_b))
                self.ed_bar_2_color.setPalette(palette)
                f.readline()

                """Bar 1 timers and actions."""
                self.ed_bar_1_refresh.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_1_Action.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_1_value.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                """Bar 2 timers and actions."""
                self.ed_bar_2_refresh.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_2_Action.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.ed_bar_2_value.setText(str(re.sub(r'\s+', '', f.readline())))
                """Cooldown."""
                f.readline()
                self.cooldown_timer_1.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_1.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_2.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_2.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_3.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_3.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_4.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_4.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_5.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_5.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_6.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_6.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_7.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_7.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_8.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_8.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_9.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_9.setText(str(re.sub(r'\s+', '', f.readline())))
                f.readline()
                self.cooldown_timer_10.setText(re.sub(r'\s+', '', f.readline()))
                f.readline()
                self.cooldown_edit_10.setText(str(re.sub(r'\s+', '', f.readline())))

    def set_bg(self):
        file = QFileDialog.getOpenFileName(self, 'Open background image')[0]

        if file != "":
            self.bg_image = file
            oImage = QImage(self.bg_image)
            sImage = oImage.scaled(QSize(self.width, self.height))
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))
            self.setPalette(palette)
            with open('BG_set.txt', 'tw') as f:
                f.write(self.bg_image)

    def previus_bg(self):
        try:
            f = open('BG_set.txt', 'r')
            self.bg_image = f.readline()
            oImage = QImage(self.bg_image)
            sImage = oImage.scaled(QSize(self.width, self.height))
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))
            self.setPalette(palette)
            f.close()
        except FileNotFoundError:
            oImage = QImage("Wallpaper.jpg")
            sImage = oImage.scaled(QSize(self.width, self.height))
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))
            self.setPalette(palette)

    def start_software(self):
        """Функция запуска."""
        global run
        run = True
        # предпросмотр области bar`ов.
        # изменение интерфеса пользователями под себя
        # подсказки к элементам

        if self.first_r == 256:
            QMessageBox.warning(self, 'Warning', "First bar's color is not set!")
        elif self.valued_first_bar is None:
            QMessageBox.warning(self, 'Warning', "First bar's values are not set!")
        else:
            first_bar_thread = threading.Thread(target=self.first_bar_analizer, args=[])
            first_bar_thread.start()

        if self.second_r == 256:
            QMessageBox.warning(self, 'Warning', "Second bar's color is not set!")
        elif self.valued_second_bar is None:
            QMessageBox.warning(self, 'Warning', "Second bar's values are not set!")
        else:
            second_bar__thread = threading.Thread(target=self.second_bar_analizer, args=[])
            second_bar__thread.start()

        # if (self.Action_timer_1.text() and self.Action_edit_1.text() is None) or \
        #         (self.Action_timer_1.text() and self.Action_edit_1.text() is not None):
        #     buttons_thread = threading.Thread(target=self.buttons, args=[])
        #     buttons_thread.start()
        # else:
        #     QMessageBox.warning(self, 'Warning', "Timer or action is not set!")

        if (self.cooldown_timer_1.text() and self.cooldown_edit_1.text() is None) or \
                (self.cooldown_timer_1.text() and self.cooldown_edit_1.text() is not None):
            cooldown_buttons_thread = threading.Thread(target=self.cooldown_buttons, args=[])
            cooldown_buttons_thread.start()
        else:
            QMessageBox.warning(self, 'Warning', "Cooldown buttons timer or action is not set!")

    def stop_software(self):
        """Функция остановки."""

        global run
        if run:
            run = False
            self.bars_statistics.append('stopping...')


class HelpForm(QMainWindow, gui.Ui_HelpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    help_form = HelpForm()
    help_form.show()
    app.exec()

# Сделать два языка словарём
