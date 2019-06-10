import window
import gui_interface
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    event_manager = gui_interface.Gui_interface()
    ui = window.Ui_MainWindow()
    ui.setupUi(MainWindow, event_manager)
    MainWindow.show()
    sys.exit(app.exec_())
