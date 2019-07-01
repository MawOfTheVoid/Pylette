from colordialogobject import Colordialog__object
from PyQt5.QtWidgets import QFileDialog
import pictureobject


class Filemanager():
    """Provides an interface for dataobjects or creates them
    on demand"""

    def __init__(self, conf):
        self.color_objects = []
        self.conf = conf
        self.colordialog = Colordialog__object()
        self.color_objects.append(self.colordialog)

    def add_file_from_filedialog(self):
        file_name = QFileDialog.getOpenFileName()
        if file_name[0] == "":
            print("No file opened")
            return
        self.create_new_object(file_name[0])

    def add_file_from_drag(self):
        # dont know yet
        pass

    def create_new_object(self, filepath):
        # check the fileending
        # create an object accordingly
        # add it to the appropiate list
        # update the gui

        if self.is_picture(filepath):
            picture = pictureobject.Picture_object(filepath, self.conf)
            self.color_objects.append(picture)
        # Add checks for special text files and gifs
        pass

    def delete_file(self):
        # search for the object
        # remove it
        # update gui
        pass

    def get_all_objects(self):
        # open new list
        # add every object to it
        # return
        pass

    def get_all_colors(self):
        colors = []
        for object in self.color_objects:
            colors += object.get_colors()
        return colors

    def is_picture(self, filepath):
        if (
                filepath[-4:] == ".png" or filepath[-4:] == ".gif" or
                filepath[-4:] == ".bmp" or filepath[-4:] == ".eps" or
                filepath[-4:] == ".dib" or filepath[-4:] == ".ico" or
                filepath[-4:] == ".msp" or filepath[-4:] == ".pcx" or
                filepath[-4:] == ".ppm" or filepath[-4:] == ".tif" or
                filepath[-4:] == ".tga" or filepath[-4:] == ".jpg"
                ):
            return True
        elif filepath[-5:] == ".jpeg" or filepath[-5:] == ".tiff":
            return True
        elif filepath[-3:] == ".im":
            return True
        else:
            return False

    def open_color_dialog(self):
        self.colordialog.get_custom_color()
