# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maybe_final.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
import export_assistant as export
from settings_window import Settings_window
import filemanager
import config


class Ui_MainWindow(object):

    def __init__(self, MainWindow):
        self.init_rest(MainWindow)
        self.create_window(MainWindow)
        self.upper_layout(MainWindow)
        self.create_color_buttons(MainWindow)
        self.lower_layout(MainWindow)
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

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_8, 0, 1, 1, 1)

        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_15, 1, 3, 1, 1)

        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_16, 1, 4, 1, 1)

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_11, 1, 2, 1, 1)

        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)

        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_12, 0, 2, 1, 1)

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_10, 1, 1, 1, 1)

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_9, 1, 0, 1, 1)

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)

        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_14, 0, 4, 1, 1)

        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_18, 0, 6, 1, 1)

        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_17, 0, 5, 1, 1)

        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_19, 0, 7, 1, 1)

        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_20, 0, 8, 1, 1)

        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_21.sizePolicy().hasHeightForWidth())
        self.pushButton_21.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_21, 0, 9, 1, 1)

        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_22, 1, 5, 1, 1)

        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_23, 1, 6, 1, 1)

        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_24, 1, 7, 1, 1)

        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_25, 1, 8, 1, 1)

        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.pushButton_26, 1, 9, 1, 1)

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
        self.horizontalLayout_2.addWidget(self.delete_btn)

        self.reset_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.reset_btn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.reset_btn.setText("Reset File")
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

    def bind_buttons(self):
        self.filedialog_btn.clicked.connect(self.filedialog_buttonpress)
        self.export_btn.clicked.connect(self.export_press)
        self.settings_btn.clicked.connect(self.settings_press)
        self.colordialog_btn.clicked.connect(self.colordialog_press)
        self.color_combo.currentIndexChanged.connect(self.update_gui)

    def update_gui(self, event):
        print(event)

    def colordialog_press(self):
        self.filemanager.open_color_dialog()

    def settings_press(self):
        self.settings_window.load_settings()
        self.settings_window.exec_()

    def filedialog_buttonpress(self):
        succesful = self.filemanager.add_file_from_filedialog()
        if succesful:
            filename = self.filemanager.get_filenames()[-1]
            self.color_combo.addItem(filename)

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
