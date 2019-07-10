from PyQt5.QtWidgets import QColorDialog


class Colordialog__object():
    """The class that is responsible for storing and
        creation of the custom colors"""

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
