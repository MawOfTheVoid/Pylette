from PyQt5.QtWidgets import QColorDialog


class Colordialog__object():
    """Gives an interface to access the colors of a picture."""

    def __init__(self):
        self.is_changed = False
        self.filename = "Custom Colors"
        self.mutable_list = []

    def reset_list(self):
        self.mutable_list = []

    def get_colors(self):
        return self.mutable_list

    def get_custom_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.mutable_list.append(color)
