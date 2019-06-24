from PyQt5.QtWidgets import QFileDialog

def get_path():
    saveable_formats = """Png (*.png);;Jpg (*.jpg);;
    Bmp (*.bmp)"""
    filename = QFileDialog.getSaveFileName(
        None, caption="Export colors",
        filter=saveable_formats)
    print(filename[1][6:-1])
    return None, None, None

def save_picture(path, format, settings):
    pass
