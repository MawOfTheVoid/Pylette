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

def save_picture(path, settings, colors):
    colors.sort(key=lambda qcolor: qcolor.getHsv())
    palette = Image.new("RGBA", size=(len(colors), 1))
    for index, qcolor in enumerate(colors):
        palette.putpixel((index, 0), qcolor.getRgb())
    palette.resize((800,800), resample=Image.NEAREST).show()
