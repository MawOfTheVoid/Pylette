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


def get_pixelcount(filepath):
    img = Image.open(filepath)
    return img.width * img.height


def all_colors_to_palette(unmutable_colorlist):
    colors = []
    for count_color in unmutable_colorlist:
        colors.append(count_color[1])
    return colors


def maxcolors(unmutable_list, maximal_colors):
    # colors = []
    # sort by amount
    # take the number of colors-1
    # copy to colors
    # return colors
    colors = []
    unmutable_list = sorted(unmutable_list, key=lambda color: color[0])
    temp = unmutable_list[0:maximal_colors]
    for count_color in temp:
        colors.append(count_color[1])
    return colors


def percent_threshold(unmutable_list, percent):
    # multiply size and hight of picture = a
    # colors = tuple
    # loop through colors
    # pixelcount / a = cpercent
    # if cpercent >= percent
    # append colors[1] to some list
    # return some list
    print("percent")
