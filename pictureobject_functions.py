from PIL import Image
from PyQt5.QtGui import QColor
import gc


def get_filename_from_path(filepath):
    # gets the filename of a given path; the replacement is needed to
    # make it work on windows and linux
    filepath = filepath.replace("\\", "/").split("/")
    return filepath[-1]


def get_list_from_file(filepath):
    # gets the the colors of the image (pixelcount (r, g, b))
    # converts the tuple to a QColor and appends it to a new list
    # which is in turn converted into a tuple and returned
    gc.collect()
    img = Image.open(filepath)
    # if you set it to lower than the amount of colors in a picture the
    # function returns none;
    # if the amount is too high the performance takes a hit
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
    # deleting isnt necessary but I want to free it before collection
    # but I also havent locked at how del or the gc works so heyyyyy
    del colorlist
    gc.collect()
    return qcolorlist


def get_pixelcount(filepath):
    # calculates the amount of pixels in a picture
    img = Image.open(filepath)
    return img.width * img.height


def all_colors_to_palette(unmutable_colorlist):
    # walks through the list and copies all QColors to the colors list
    colors = []
    for count_color in unmutable_colorlist:
        colors.append(count_color[1])
    return colors


def maxcolors(unmutable_list, maximal_colors):
    # makes the unmutable_list (which is a tuple) a proper list and sorts
    # it by the first value (which is the amount of this color) and copys
    # the content up to into a temporary list. From the temporary list it
    # only copys the QColors into the colors list and returns it
    colors = []
    unmutable_list = sorted(unmutable_list, key=lambda color: color[0])
    temp = unmutable_list[0:maximal_colors]
    for count_color in temp:
        colors.append(count_color[1])
    return colors


def percent_threshold(unmutable_list, percent_boundry, pixelcount):
    # calculates how much percent a color takes up and appends it to
    # colors if the percentage it takes up is equal or greater than the
    # percentage boundry
    colors = []
    unmutable_list = list(unmutable_list)
    for count_color in unmutable_list:
        amount = count_color[0]
        percent = (amount / pixelcount) * 100
        print(percent)
        if percent >= percent_boundry:
            colors.append(count_color[1])
    return colors
