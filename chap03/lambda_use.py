from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class LambdaUse(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("lambda_use.ui")
        self.ui.show()
        self.ui.btn_ok.clicked.connect(lambda stat, button=self.ui.btn_ok: self.showLabel(stat, button))
        self.ui.btn_yes.clicked.connect(lambda stat, button=self.ui.btn_yes: self.showLabel(stat, button))
        self.ui.btn_yes.pressed.connect(lambda text=self.ui.btn_yes.text(): self.showLabelText(text))


    def showLabelText(self, text):
        QMessageBox.information(self, "btn_ok", text, QMessageBox.Ok)


    def showLabel(self, stat, button):
        message = button.text()
        # QMessageBox.information(self, "btn_ok", message, QMessageBox.Ok)
        self.ui.lbl_res.setText(message)


if __name__ == "__main__":
    app = QApplication([])
    w = LambdaUse()
    app.exec_()


