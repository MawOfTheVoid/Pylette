class Filemanager():
    """Provides an interface for dataobjects and creates them
    on demand"""

    def __init__(self):
        self.pictureobjects = []
        self.text_objects = []
        self.color_dialog_object = []

    def add_file_from_filedialog(self):
        # open Filedialog
        # extract filepath
        # give filepath to create_new_object
        pass

    def add_file_from_drag(self):
        # dont know yet
        pass

    def create_new_object(self):
        # check the fileending
        # create an object accordingly
        # add it to the appropiate list
        # update the gui
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
