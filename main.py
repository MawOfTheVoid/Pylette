from PyQt5.QtWidgets import QApplication, QMainWindow
from window import Ui_MainWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    window = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
