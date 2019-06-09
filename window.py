# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    """Is responsible for the look of the Window and the function calls when
    a Button is pressed"""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 164)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.filedialog = QtWidgets.QPushButton(self.centralwidget)
        self.filedialog.setGeometry(QtCore.QRect(10, 10, 141, 121))
        self.filedialog.setAcceptDrops(True)

        self.export_as_png = QtWidgets.QPushButton(self.centralwidget)
        self.export_as_png.setGeometry(QtCore.QRect(150, 10, 161, 121))
        self.export_as_png.setDefault(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filedialog.setText(_translate("MainWindow", "Filedialog"))
        self.export_as_png.setText(_translate("MainWindow", "Export as png"))
