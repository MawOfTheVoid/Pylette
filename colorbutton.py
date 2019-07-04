from PyQt5.QtWidgets import QPushButton, QColorDialog

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

    def pressed(self, event):
        pass
