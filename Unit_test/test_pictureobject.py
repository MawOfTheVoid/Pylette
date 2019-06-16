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

    def setUp(self):
        # The class needs a working picture to initialise
        self.picture1 = Picture_object(r"Bold and Brash 2.png")
        self.picture2 = Picture_object(r"Bold and Brash 2.png")
        self.picture3 = Picture_object(r"Bold and Brash 2.png")
        self.picture4 = Picture_object(r"Bold and Brash 2.png")

    def test_get_filename_from_path(self):
        path1 = self.picture1.get_filename_from_path(r"F:/Stuff/to/test.py")
        path2 = self.picture2.get_filename_from_path(r"F:/Stu ff/to /test.py")
        path3 = self.picture3.get_filename_from_path(r"C:\hype\for\Botw2")
        path4 = self.picture4.get_filename_from_path(r"/one linux/path/qtlicense is weired")

        self.assertEqual(path1, 'test.py')
        self.assertEqual(path2, 'test.py')
        self.assertEqual(path3, 'Botw2')
        self.assertEqual(path4, 'qtlicense is weired')

    def test_get_list_from_file(self):
        # we just assume here that the baseline algorithm works correct
        # because there is no algorithm exactly as this one
        # So we test here only certain file extensions
        list1 = self.picture1.get_list_from_file(r"Bold and Brash 2.png")
        list2 = self.picture2.get_list_from_file(r"Bold and Brash 2.jpg")
        list3 = self.picture3.get_list_from_file(r"Bold and Brash 2.tif")
        list4 = self.picture4.get_list_from_file(r"Bold and Brash 2.ppm")

        # Todo finish the actual tests

if __name__ == "__main__":
    unittest.main()
