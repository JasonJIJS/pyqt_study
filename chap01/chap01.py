from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("chap01.ui")
        self.ui.btn_ok.clicked.connect(self.showProp)
        self.ui.show()

    def showProp(self):
        print("red {} green {} blue {}".format(
              self.ui.spin_red.value(), self.ui.spin_green.value(), self.ui.spin_blue.value()))

        # print("showProp")
        # print(self.ui.spin_red.value())
        self.ui.spin_red.setValue(128)      # setValue에 값 지정
        self.ui.spin_green.setValue(128)
        self.ui.spin_blue.setValue(128)

        # print(dir(self.ui.spin_red))





if __name__ == "__main__":
    app = QApplication([])
    w = MyApp()
    app.exec()


    # app = QApplication(sys.argv)
    # MainWindow = QMainWindow()
    # ui = hello_pyqt5.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())