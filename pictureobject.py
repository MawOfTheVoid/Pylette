from PIL import Image
from PyQt5.QtGui import QColor
import gc


class Picture_object():
    """Get the colordata from a function and
    provides an Interface to access it"""

    # braucht den filename von mimedata und
    def __init__(self, filepath):
        self.is_changed = False
        self.filename = self.get_filename_from_path(filepath)
        self.unmutable_list = self.get_list_from_file(filepath)
        self.mutable_list = self.reset_list()

    def get_filename_from_path(self, filepath):
        filepath = filepath.replace("\\", "/").split("/")
        return filepath[-1]

    def get_list_from_file(self, filepath):
        # öffnet datei mit pillow  	✓
        # checkt ob die länge der zweiten unterliste4 lang ist
        # wenn nicht dann 255 anhängen
        # in QColors umwandeln
        # liste in tulpe umwandeln
        # liste zurückgeben

        gc.collect()
        img = Image.open(filepath)
        colorlist = img.getcolors(maxcolors=3840 * 2160)
        qcolorlist = []
        """TODO Gifs do not Work!!!"""
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
        return qcolorlist

    def reset_list(self):
        # mutable_list = []
        # durch liste loopen
        # unmutable_list[1] an mutable_list anhängen
        pass

    def get_colors(self):
        return self.mutable_list
