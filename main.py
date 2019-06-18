from PyQt5 import QtWidgets
import window
import config
import sys

if __name__ == "__main__":
    conf = config.ConfigManager()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = window.Ui_MainWindow()
    ui.setup(MainWindow, conf)
    MainWindow.show()
    sys.exit(app.exec_())
