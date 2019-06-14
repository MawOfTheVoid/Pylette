import unittest
import sys
from pathlib import Path
from PyQt5 import QtWidgets

# move one directory up
path = Path(__file__).parents[1]
sys.path.insert(0, str(path))
from pictureobject import Picture_object

class Test_Picture_object(unittest.TestCase):

    def setUpClass():
        app = QtWidgets.QApplication(sys.argv)

    def test_email(self):
        picture1 = Picture_object(r"C:\some\absolute\path\test.png")
        picture2 = Picture_object(r"/hey/how/are/you.py")
        picture3 = Picture_object(r"you.py")
        picture3 = Picture_object(r"C:\some\absolute space\path\stuff.png")

        self.assertEqual(picture1.get_filename_from_path(r"C:\some\absolute\path\test.png"), "test.png")



if __name__ == "__main__":
    unittest.main()
