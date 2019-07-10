from PyQt5.QtWidgets import QPushButton, QColorDialog, QMessageBox
from PyQt5.QtCore import Qt


class Color_button(QPushButton):
    """The butttons in the middle which change colors"""

    def __init__(self, parent, index, window_instance):
        super().__init__(parent)
        self.index = index
        self.list = []
        self.window_instance = window_instance

    def update(self, colorlist, index):
        # updates the colors of the button
        self.setDisabled(False)
        self.index = index
        self.list = colorlist
        color = self.list[self.index].getRgb()
        self.setStyleSheet(f"background-color:rgba{color}")

    def reset(self):
        # resets the stylesheet to get the original color scheme back
        # and disables the button
        self.setStyleSheet("")
        self.setDisabled(True)

    def mousePressEvent(self, QMouseEvent):
        # this is made to save the window.py many lines because of it gives the
        # responsibility of button presses to the colorbutton
        if QMouseEvent.button() == Qt.LeftButton:
            self.colordialog()
        elif QMouseEvent.button() == Qt.RightButton:
            self.delete()

    def delete(self):
        # delets the colors and calls a gui update
        if not len(self.list):
            return
        # deletes the color straight from the objects colorlist
        del self.list[self.index]
        self.list = []
        self.index = None
        self.setStyleSheet("")
        self.setDisabled(True)
        self.window_instance.update_gui()

    def colordialog(self):
        # changes the color of the pressed colorbutton
        self.window_instance.color_combo.setFocus()
        try:
            # self.list[self.index] is a qcolor
            color = QColorDialog.getColor(self.list[self.index])
            if color.isValid():
                self.list[self.index] = color
                self.setStyleSheet(f"background-color:rgba{color.getRgb()}")
        except Exception:
            QMessageBox.critical(
                None, 'Fatal Error!!!!!',
                """You need to open colors to change them!!!\n
                You have been warned...""", QMessageBox.Ok)
