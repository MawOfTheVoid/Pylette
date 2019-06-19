import pictureobject_functions as pic_functions


class Picture_object():
    """Gives an interface to access the colors of a picture."""

    def __init__(self, filepath, conf):
        self.conf = conf
        self.is_changed = False
        self.filename = pic_functions.get_filename_from_path(filepath)
        self.pixels = pic_functions.get_pixelcount(filepath)
        self.unmutable_list = pic_functions.get_list_from_file(filepath)
        self.mutable_list = self.reset_list()
        for color in self.mutable_list:
            print(color.getRgb())

    def reset_list(self):
        # it takes the unmutable_list and calls
        # the necessary functions depending on the configuration
        settings = self.conf.get_picture_import_settings()
        if settings["reduce_colors"] is False:
            colors = pic_functions.all_colors_to_palette(self.unmutable_list)

        elif settings["maxcolors"][0] is True:
            maximal_colors = settings["maxcolors"][1]
            colors = pic_functions.maxcolors(self.unmutable_list, maximal_colors)

        elif settings["threshold"][0] is True:
                percent = settings["threshold"][2]
                colors = pic_functions.percent_threshold(self.unmutable_list, percent, self.pixels)
        return colors

    def get_colors(self):
        # a getter for other classes
        return self.mutable_list
