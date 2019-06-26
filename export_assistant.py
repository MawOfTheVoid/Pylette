from PyQt5.QtWidgets import QFileDialog
from PIL import Image


def export_format(fileending):
    picture_endings = [".png", ".jpg", ".bmp"]
    if fileending in picture_endings:
        return "picture"


def get_path():
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
    for color in colors:
        color.setAlpha(255)


def save_picture(path, settings, colors):
    colors.sort(key=lambda qcolor: qcolor.getHsv())
    palette = Image.new("RGBA", size=(len(colors), 1))
    if settings["alpha"] is False:
        remove_alpha(colors)

    for index, qcolor in enumerate(colors):
        palette.putpixel((index, 0), qcolor.getRgb())

    if settings["resize"][0] is True:
        _, width, height = settings["resize"]
        palette = palette.resize((width, height), resample=Image.NEAREST)
    elif settings["scale"][0] is True:
        factor = settings["scale"][1]
        palette = palette.resize(
            (palette.width * factor, palette.height * factor),
            resample=Image.NEAREST)
    palette.show()
    # palette.save(path)
