from PyQt5.QtWidgets import QColorDialog


class Color_dialog__object():
    """Gives an interface to access the colors of a picture."""

    def __init__(self, filepath, conf):
        self.conf = conf
        self.filepath = filepath
        self.is_changed = False
        self.filename = "Custom Colors"
        self.mutable_list = []

    def reset_list(self):
        self.mutable_list = []

    def get_colors(self):
        return self.mutable_list

    def open_dialog(self):
        color = QColorDialog.getColor()
        print(color)

        if color.isValid():
            print(color.name())
            self.mutable_list.append(color)
