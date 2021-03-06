import json
import os


class ConfigManager():
    """Reads the config.pyl and provides an interface for the other classes"""

    # Two main resposiblilities
    # giving other classes an interface
    # translating the settings-popup to a dictionary to dump into json
    # the settings are only accessed through the configmanager to keep
    # everything always up to date without endlessly readig the file

    def __init__(self):
        self.adress = "config.json"
        # should never be changed
        self.default_json = {
            'picture_import': {
                'reduce_colors': True,
                'threshold': [False, 100],
                'maxcolors': [False, 8],
                'quantize': [True, 8]},
            'text_import': '',
            'picture_export': {
                'scale': [True, 32],
                'resize': [False, 800, 800],
                'alpha': False},
            'text_export': ''}
        self.dict = self.get_dict_from_file()

    def get_dict_from_file(self):
        # optional: checking the keys and values of the dict for integrety
        if not os.path.isfile(self.adress):
            with open(self.adress, "w") as file:
                json.dump(self.default_json, file, indent=1)
        with open(self.adress, "r") as file:
            return json.load(file)

    def dict_to_file(self, dict):
        with open(self.adress, "w") as file:
            json.dump(dict, file, indent=1)

    def update(self, settings):
        self.dict_to_file(settings)
        self.dict = self.get_dict_from_file()

    def get_picture_import_settings(self):
        return self.dict["picture_import"]

    def get_text_import_settings(self):
        return self.dict["text_import"]

    def get_picture_export_settings(self):
        return self.dict["picture_export"]

    def get_text_export_settings(self):
        return self.dict["text_export"]

    def get_all_settings(self):
        return self.dict.copy()
