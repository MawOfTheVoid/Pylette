from PIL import Image
from PyQt5.QtGui import QColor
import gc


def get_filename_from_path(filepath):
    filepath = filepath.replace("\\", "/").split("/")
    return filepath[-1]


def get_list_from_file(filepath):
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
    qcolorlist = tuple(qcolorlist)
    del colorlist
    gc.collect()
    return qcolorlist


def all_colors_to_palette(unmutable_colorlist):
    print("all")


def maxcolors(unmutable_list, maximal_colors):
    print("maxcolors")


def percent_threshold(unmutable_list, percent):
    print("percent")


def absolute_threshold(unmutable_list, number):
    print("absolute")
