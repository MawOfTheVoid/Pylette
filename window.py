# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maybe_final.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import export_assistant as export
from settings_window import Settings_window
from colorbutton import Color_button
import filemanager
import config


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.init_rest(MainWindow)
        self.create_window(MainWindow)
        self.upper_layout(MainWindow)
        self.create_color_buttons(MainWindow)
        self.lower_layout(MainWindow)
        self.color_button_list()
        self.reset_all_color_btn()
        self.bind_buttons()

    def init_rest(self, MainWindow):
        self.conf = config.ConfigManager()
        self.filemanager = filemanager.Filemanager(self.conf)
        self.settings_window = Settings_window(MainWindow, self.conf)


    def create_window(self, MainWindow):
        MainWindow.setWindowTitle("Pylette")
        MainWindow.resize(785, 275)
        MainWindow.setMinimumSize(QtCore.QSize(375, 0))

    def upper_layout(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setSpacing(6)

        self.color_combo = QtWidgets.QComboBox(self.centralwidget)
        self.color_combo.setMinimumSize(QtCore.QSize(100, 0))
        self.color_combo.addItem("")
        self.color_combo.setItemText(0, "No Colors available")
        self.color_combo.addItem("")
        self.color_combo.setItemText(1, "Custom Color")
        self.horizontalLayout.addWidget(self.color_combo)

        spacerItem = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.filedialog_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filedialog_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.filedialog_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.filedialog_btn.setText("Filedialog")
        self.horizontalLayout.addWidget(self.filedialog_btn)

        self.colordialog_btn = QtWidgets.QPushButton(self.centralwidget)
        self.colordialog_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.colordialog_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.colordialog_btn.setText("Custom Color")
        self.horizontalLayout.addWidget(self.colordialog_btn)

        self.settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.settings_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.settings_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.settings_btn.setText("Settings")
        self.horizontalLayout.addWidget(self.settings_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        spacerItem1 = QtWidgets.QSpacerItem(
            30, 10, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)

    def create_color_buttons(self, MainWindow):
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)

        self.color_button_1 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_1.sizePolicy().hasHeightForWidth())
        self.color_button_1.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_1, 0, 1, 1, 1)

        self.color_button_13 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_13.sizePolicy().hasHeightForWidth())
        self.color_button_13.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_13, 1, 3, 1, 1)

        self.color_button_14 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_14.sizePolicy().hasHeightForWidth())
        self.color_button_14.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_14, 1, 4, 1, 1)

        self.color_button_12 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_12.sizePolicy().hasHeightForWidth())
        self.color_button_12.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_12, 1, 2, 1, 1)

        self.color_button_3 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_3.sizePolicy().hasHeightForWidth())
        self.color_button_3.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_3, 0, 3, 1, 1)

        self.color_button_2 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_2.sizePolicy().hasHeightForWidth())
        self.color_button_2.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_2, 0, 2, 1, 1)

        self.color_button_11 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_11.sizePolicy().hasHeightForWidth())
        self.color_button_11.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_11, 1, 1, 1, 1)

        self.color_button_10 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_10.sizePolicy().hasHeightForWidth())
        self.color_button_10.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_10, 1, 0, 1, 1)

        self.color_button_0 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_0.sizePolicy().hasHeightForWidth())
        self.color_button_0.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_0, 0, 0, 1, 1)

        self.color_button_4 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_4.sizePolicy().hasHeightForWidth())
        self.color_button_4.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_4, 0, 4, 1, 1)

        self.color_button_6 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_6.sizePolicy().hasHeightForWidth())
        self.color_button_6.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_6, 0, 6, 1, 1)

        self.color_button_5 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_5.sizePolicy().hasHeightForWidth())
        self.color_button_5.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_5, 0, 5, 1, 1)

        self.color_button_7 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_7.sizePolicy().hasHeightForWidth())
        self.color_button_7.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_7, 0, 7, 1, 1)

        self.color_button_8 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_8.sizePolicy().hasHeightForWidth())
        self.color_button_8.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_8, 0, 8, 1, 1)

        self.color_button_9 =Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_9.sizePolicy().hasHeightForWidth())
        self.color_button_9.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_9, 0, 9, 1, 1)

        self.color_button_15 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_15.sizePolicy().hasHeightForWidth())
        self.color_button_15.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_15, 1, 5, 1, 1)

        self.color_button_16 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_16.sizePolicy().hasHeightForWidth())
        self.color_button_16.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_16, 1, 6, 1, 1)

        self.color_button_17 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_17.sizePolicy().hasHeightForWidth())
        self.color_button_17.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_17, 1, 7, 1, 1)

        self.color_button_18 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_18.sizePolicy().hasHeightForWidth())
        self.color_button_18.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_18, 1, 8, 1, 1)

        self.color_button_19 = Color_button(self.centralwidget, 0, self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.color_button_19.sizePolicy().hasHeightForWidth())
        self.color_button_19.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.color_button_19, 1, 9, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

    def lower_layout(self, MainWindow):
        spacerItem2 = QtWidgets.QSpacerItem(
            30, 10, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(
            QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setSpacing(6)

        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.delete_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_btn.setText("Delete File")
        self.delete_btn.setDisabled(True)
        self.horizontalLayout_2.addWidget(self.delete_btn)

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.reset_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.reset_btn.setText("Reset File")
        self.reset_btn.setDisabled(True)
        self.horizontalLayout_2.addWidget(self.reset_btn)

        spacerItem3 = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Maximum,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.export_btn = QtWidgets.QPushButton(self.centralwidget)
        self.export_btn.setMinimumSize(QtCore.QSize(150, 0))
        self.export_btn.setText("Export")
        self.horizontalLayout_2.addWidget(self.export_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def color_button_list(self):
        self.color_btn_list = [
            self.color_button_0,
            self.color_button_1,
            self.color_button_2,
            self.color_button_3,
            self.color_button_4,
            self.color_button_5,
            self.color_button_6,
            self.color_button_7,
            self.color_button_8,
            self.color_button_9,
            self.color_button_10,
            self.color_button_11,
            self.color_button_12,
            self.color_button_13,
            self.color_button_14,
            self.color_button_15,
            self.color_button_16,
            self.color_button_17,
            self.color_button_18,
            self.color_button_19
        ]

#    def color_button_list_operations(self):
#        for btn in self.color_btn_list:
#            btn.clicked.connect(btn.pressed)

    def bind_buttons(self):
        self.filedialog_btn.clicked.connect(self.filedialog_buttonpress)
        self.export_btn.clicked.connect(self.export_press)
        self.settings_btn.clicked.connect(self.settings_press)
        self.colordialog_btn.clicked.connect(self.colordialog_press)
        self.color_combo.currentIndexChanged.connect(self.update_gui)
        self.delete_btn.clicked.connect(self.delete_press)
        self.reset_btn.clicked.connect(self.reset_press)

    def reset_press(self):
        combo_index = self.color_combo.currentIndex()
        object_index = combo_index - 1
        self.filemanager.color_objects[object_index].reset_list()
        self.update_gui()

    def delete_press(self):
        combo_index = self.color_combo.currentIndex()
        object_index = combo_index - 1
        del self.filemanager.color_objects[object_index]
        self.color_combo.removeItem(combo_index)
        self.update_gui()

    def update_gui(self):
        combo_index = self.color_combo.currentIndex()
        object_index = combo_index - 1
        self.update_first_combo()
        if combo_index == 0:
            self.delete_btn.setDisabled(True)
            self.reset_btn.setDisabled(True)
        elif combo_index == 1:
            self.delete_btn.setDisabled(True)
            self.reset_btn.setDisabled(False)
        else:
            self.delete_btn.setDisabled(False)
            self.reset_btn.setDisabled(False)

        self.reset_all_color_btn()
        self.update_colorbuttons(object_index, combo_index)

        # the rest comes later when the color buttons work

    def update_first_combo(self):
        if (
            len(self.filemanager.color_objects) == 1
                and not self.filemanager.color_objects[0].mutable_list):
            self.color_combo.setItemText(0, "No Colors available")
        else:
            self.color_combo.setItemText(0, "All Colors")

    def colordialog_press(self):
        self.filemanager.open_color_dialog()
        self.update_gui()

    def settings_press(self):
        self.settings_window.load_settings()
        self.settings_window.exec_()

    def filedialog_buttonpress(self):
        succesful = self.filemanager.add_file_from_filedialog()
        if succesful:
            filename = self.filemanager.get_filenames()[-1]
            self.color_combo.addItem(filename)
        self.update_gui()

    def export_press(self):
        colors = self.filemanager.get_all_colors()
        if not colors:
            QtWidgets.QMessageBox.critical(
                self.export_btn, 'Fatal Error!!!!!',
                """If you dont select any colors to export your
                computer may explode!!!\n
                You have been warned...""", QtWidgets.QMessageBox.Ok)
            return
        path, file_type = export.get_path()
        if file_type == "picture":
            settings = self.conf.get_picture_export_settings()
            export.save_picture(path, settings, colors)
        else:
            # check for other formats
            pass

    def update_colorbuttons(self, object_index, combo_index):
        if combo_index == 0:
            self.update_colorbuttons_all_palettes()
        else:
            self.update_colorbuttons_one_palette(object_index)

    def reset_all_color_btn(self):
        for btn in self.color_btn_list:
            btn.reset()

    def update_colorbuttons_one_palette(self, object_index):
        palette_length = len(self.filemanager.color_objects[object_index].mutable_list)
        colors = self.filemanager.color_objects[object_index].mutable_list
        # All buttons can be used
        if palette_length > 20:
            for index in range(0, 20):
                self.color_btn_list[index].update(colors, index)
        elif palette_length >= 0 and palette_length < 20:
            for index in range(0, palette_length):
                self.color_btn_list[index].update(colors, index)
            for index in range(palette_length, 20):
                self.color_btn_list[index].setDisabled(True)

    def update_colorbuttons_all_palettes(self):
        pass
