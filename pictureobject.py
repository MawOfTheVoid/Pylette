from PIL import Image
from PyQt5.QtGui import QColor
import gc


class Picture_object():
    """Gives an interface to access the colors of a picture."""

    def __init__(self, filepath, conf):
        self.conf = conf
        self.is_changed = False
        self.filename = self.get_filename_from_path(filepath)
        self.unmutable_list = self.get_list_from_file(filepath)
        self.mutable_list = self.reset_list()

    def get_filename_from_path(self, filepath):
        filepath = filepath.replace("\\", "/").split("/")
        return filepath[-1]

    def get_list_from_file(self, filepath):
        gc.collect()
        img = Image.open(filepath)
        colorlist = img.getcolors(maxcolors=1000000)
        qcolorlist = []
        """TODO Gifs do not work!!!"""
        # picture has no alpha channel
        if len(colorlist[0][1]) == 3:
            for count_color in colorlist:
                r, g, b = count_color[1]
                qcolorlist.append((count_color[0], QColor.fromRgb(r, g, b)))
        # picture has alpha channel
        elif len(colorlist[0][1]) == 4:
            for count_color in colorlist:
                r, g, b, a = count_color[1]
                qcolorlist.append(
                    (count_color[0], QColor.fromRgb(r, g, b, alpha=a))
                )
        print("done")
        qcolorlist = tuple(qcolorlist)
        del colorlist
        gc.collect()
        return qcolorlist

    def reset_list(self):
        # mutable_list = []
        # get the information from the configuration class
        # put it through the appropriate function which takes the list as
        # input and outputs a new list
        # mutable_list = said function
        pass

    def get_colors(self):
        return self.mutable_list
