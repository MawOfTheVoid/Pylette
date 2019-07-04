from PyQt5.QtWidgets import QPushButton, QColorDialog
from PyQt5.QtCore import Qt


class Color_button(QPushButton):

    def __init__(self, parent, index):
        super().__init__(parent)
        self.index = index
        self.list = []

    def update(self, colorlist, index):
        self.setDisabled(False)
        self.index = index
        self.list = colorlist
        color = self.list[self.index].getRgb()
        style = f"background-color:rgb{color}"
        self.setStyleSheet(style)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")
            self.delete()

    def delete(self):
        self.list = []
        self.index = None
        self.setStyleSheet("")
        self.setDisabled(True)
