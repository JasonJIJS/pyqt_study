import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = uic.loadUi("hello_pyqt5.ui")
        self.ui = uic.loadUi("chap01/chap01.ui")

        self.ui.show()

if __name__ == "__main__":

    app = QApplication([])
    w = MyApp()
    app.exec_()
    #
    # MainWindow = QMainWindow()
    # ui = hello_pyqt5.Ui_MainWindow()
    # ui = uic.loadUi("hello_pyqt5.ui")
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app_exec)