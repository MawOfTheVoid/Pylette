import json

class ConfigManager():
    """Reads the config.pyl and provides an interface for the other classes"""

    # Two main resposiblilities
    # giving other classes an interface
    # translating the settings-popup to a dictionary to dump into json

    def __init__(self):
        self.adress = "config.json"
        self.dict = self.get_dict_from_file()

    def get_dict_from_file(self):
        # try opening the file
        # create one if not there
        # try dumping the file
        # return the dict

        # optional: checking the keys and values of the dict fro integrety
        pass

    def get_picture_import_settings(self):
        return self.dict["picture_import"]

    def get_text_import_settings(self):
        return self.dict["text_import"]

    def get_picture_export_settings(self):
        return self.dict["picture_export"]

    def get_text_export_settings(self):
        return self.dict["text_export"]
