from PyQt5.QtWidgets import QFileDialog
from PIL import Image


def export_format(fileending):
    # check if the fileending is a picture
    picture_endings = [".png", ".jpg", ".bmp"]
    if fileending in picture_endings:
        return "picture"
    # add checks for other files here


def get_path():
    # gets the path where to save and adds the appropriate fileending
    # if it is not there
    saveable_formats = """Png (*.png);;Jpg (*.jpg);;
    Bmp (*.bmp)"""
    file = QFileDialog.getSaveFileName(
        None, caption="Export colors",
        filter=saveable_formats)
    # filename[1][6:-1]
    fileending = file[1][6:-1]
    filepath = file[0]
    if not filepath.endswith(fileending):
        filepath += fileending
    file_type = export_format(fileending)
    return filepath, file_type


def remove_alpha(colors):
    # doest "remove" the alpha channel but 255 is not transparent
    for color in colors:
        color.setAlpha(255)


def save_picture(path, settings, colors):
    # gets called when its known that the palette should be saved as a picture
    # sorts the qcolors by theyre hsv value (mostly by hue)
    colors.sort(key=lambda qcolor: qcolor.getHsv())
    palette = Image.new("RGB", size=(len(colors), 1))
    # pretty much useless
    if settings["alpha"] is False:
        remove_alpha(colors)

    # puts one pixel text to the other; you get a pixelstrip
    for index, qcolor in enumerate(colors):
        palette.putpixel((index, 0), qcolor.getRgb())

    # the strip gets independently resized after its creation
    if settings["resize"][0] is True:
        _, width, height = settings["resize"]
        palette = palette.resize((width, height), resample=Image.NEAREST)
    elif settings["scale"][0] is True:
        factor = settings["scale"][1]
        palette = palette.resize(
            (palette.width * factor, palette.height * factor),
            resample=Image.NEAREST)
    # platte.save() when developing; palette.save() when shipping
    # palette.show()
    palette.save(path)
