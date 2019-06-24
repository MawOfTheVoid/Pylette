# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.12.2

from PyQt5.QtCore import QMetaObject, QRect, QCoreApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QFileDialog
import filemanager


class Ui_MainWindow(object):
    """Is responsible for the look of the mainwindow and the function calls
    when a Button is pressed"""

    def setup(self, MainWindow, conf):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 164)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.filemanager = filemanager.Filemanager(conf)
        self.conf = conf

        # initialising the buttons
        self.filedialog = QPushButton(self.centralwidget)
        self.filedialog.setGeometry(QRect(10, 10, 141, 121))
        self.filedialog.setAcceptDrops(True)

        self.export_as_png = QPushButton(self.centralwidget)
        self.export_as_png.setGeometry(QRect(150, 10, 161, 121))
        self.export_as_png.setDefault(False)

        # binding the buttons
        self.filedialog.clicked.connect(self.filedialog_buttonpress)
        self.export_as_png.clicked.connect(self.export_press)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filedialog.setText(_translate("MainWindow", "Filedialog"))
        self.export_as_png.setText(_translate("MainWindow", "Export"))

    def filedialog_buttonpress(self):
        self.filemanager.add_file_from_filedialog()

    def export_press(self):
        # open a savefialog
        # call settings
        # check wether the end of string has a fileending that fits with the
        # the fileending in the second element of the tuple
        # if not append the file extension
        # check wether export as a picture a known text type or an unknown type
        # call appropiate function
        saveable_formats = """Png (*.png);;Jpg (*.jpg);;
        Bmp (*.bmp)"""
        filename = QFileDialog.getSaveFileName(
            None, caption="Export colors",
            filter=saveable_formats)
        print(filename[1][6:-1])
        print(self.filemanager.get_all_colors())
