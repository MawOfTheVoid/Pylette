from colordialogobject import Colordialog__object
from PyQt5.QtWidgets import QFileDialog, QMessageBox
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
        # no file opened
        if file_name[0] == "":
            return
        return self.create_new_object(file_name[0])

    def create_new_object(self, filepath):
        # check the fileending
        # create an object accordingly
        # add it to the appropiate list
        # update the gui

        if self.is_picture(filepath):
            picture = pictureobject.Picture_object(filepath, self.conf)
            if picture.filename not in self.get_filenames():
                self.color_objects.append(picture)
                return True
            else:
                QMessageBox.warning(
                    None, 'U trying to trick me?',
                    """U open a file just once!
                    \n\tCapisce?""", QMessageBox.Ok)
                return False
        # Add checks for special text files
        else:
            string = "You tried to open an unsupported fileformat!\n"
            string += "Try better next time..."
            QMessageBox.warning(
                None, "Unsupported filetype",
                string, QMessageBox.Ok)

    def get_filenames(self):
        names = []
        for object in self.color_objects:
            names.append(object.filename)
        return names

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
        # checks if the extension is one of the ones that pillow supports
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
        # just a forwarder
        self.colordialog.get_custom_color()
