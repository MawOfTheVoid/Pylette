import pictureobject_functions as pic_functions


class Picture_object():
    """Gives an interface to access the colors of a picture."""

    def __init__(self, filepath, conf):
        self.conf = conf
        self.is_changed = False
        self.filename = pic_functions.get_filename_from_path(filepath)
        self.unmutable_list = pic_functions.get_list_from_file(filepath)
        self.mutable_list = self.reset_list()

    def reset_list(self):
        # mutable_list = []
        # get the information from the configuration class
        # put it through the appropriate function which takes the list as
        # input and outputs a new list
        # mutable_list = said function
        pass

    def get_colors(self):
        return self.mutable_list
