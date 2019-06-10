import filemanager


class Gui_interface():
    """Handles all Bittonpresses and events from the main window if possible"""

    def __init__(self):
        self.filehandler = filemanager.Filemanager()

    def filedialog_buttonpress(self):
        self.filehandler.add_file_from_filedialog()

    def export_press(self):
        print("Hey")
