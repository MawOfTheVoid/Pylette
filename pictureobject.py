from PIL import Image


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
        # öffnet datei mit pillow
        # checkt ob die länge der zweiten unterliste4 lang ist
        # wenn nicht dann 255 anhängen
        # in QColors umwandeln
        # liste in tulpe umwandeln
        # liste zurückgeben
        pass

    def reset_list(self):
        # mutable_list = []
        # durch liste loopen
        # unmutable_list[1] an mutable_list anhängen
        pass

    def get_colors(self):
        return self.mutable_list
