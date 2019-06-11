from PyQt5.QtWidgets import QFileDialog
import pictureobject


class Filemanager():
    """Provides an interface for dataobjects or creates them
    on demand"""

    def __init__(self):
        self.picture_objects = []
        self.text_objects = []
        self.color_dialog_object = []

    def add_file_from_filedialog(self):
        # open Filedialog
        # extract filepath
        # give filepath to create_new_object

        file_name = QFileDialog.getOpenFileName()
        if file_name[0] == "":
            print("No file opened")
            return
        print(file_name[0])
        self.create_new_object(file_name[0])

    def add_file_from_drag(self):
        # dont know yet
        pass

    def create_new_object(self, filepath):
        # check the fileending
        # create an object accordingly
        # add it to the appropiate list
        # update the gui

        # TODO add more filextensions
        if self.is_picture(filepath):
            picture = pictureobject.Picture_object(filepath)
            print(picture.filename)
            self.picture_objects.append(picture)
        pass

    def delete_file(self):
        # search for the object
        # remove it
        # update gui
        pass

    def get_all_objects(self):
        # open new list
        # add every list to it
        # return
        pass

    def get_all_colors(self):
        # open new list
        # call get_colors on every element
        # add the new colors to the list
        # return
        pass

    def is_picture(self, filepath):
        if (
            filepath[-4:] == ".png" or filepath[-4:] == ".gif" or
            filepath[-4:] == ".bmp" or filepath[-4:] == ".eps" or
            filepath[-4:] == ".dib" or filepath[-4:] == ".ico" or
            filepath[-4:] == ".msp" or filepath[-4:] == ".pcx" or
            filepath[-4:] == ".ppm" or filepath[-4:] == ".sgi" or
            filepath[-4:] == ".tga" or filepath[-4:] == ".jpg"
                ):
            return True
        elif filepath[-5:] == ".jpeg" or filepath[-5:] == ".tiff":
            return True
        elif filepath[-3:] == ".im":
            return True
        else:
            return False
