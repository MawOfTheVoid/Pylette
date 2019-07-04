from PyQt5.QtWidgets import QPushButton, QColorDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class Color_button(QPushButton):

    def __init__(self, parent, index, window_instance):
        super().__init__(parent)
        self.index = index
        self.list = []
        self.window_instance = window_instance

    def update(self, colorlist, index):
        self.setDisabled(False)
        self.index = index
        self.list = colorlist
        color = self.list[self.index].getRgb()
        self.setStyleSheet(f"background-color:rgb{color}")

    def reset(self):
        self.setStyleSheet("")
        self.setDisabled(True)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
            self.colordialog()
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")
            self.delete()

    def delete(self):
        if not len(self.list):
            return
        del self.list[self.index]
        self.list = []
        self.index = None
        self.setStyleSheet("")
        self.setDisabled(True)
        self.window_instance.update_gui()

    def colordialog(self):
        try:
            color = QColorDialog.getColor(self.list[self.index])
            if color.isValid():
                self.list[self.index] = color
                self.setStyleSheet(f"background-color:rgb{color.getRgb()}")
        except:
            QMessageBox.critical(
                None, 'Fatal Error!!!!!',
                """You need to open colors to change them!!!\n
                You have been warned...""", QMessageBox.Ok)
