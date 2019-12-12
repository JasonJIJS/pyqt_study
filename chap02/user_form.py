from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication


class UserForm(QWidget):
    def __init__(self):
        super().__init__()
        # self.ui = uic.loadUi("user_form.ui") # 여기서는 이렇게
        self.ui = uic.loadUi("chap02/user_form.ui")  # 밖에 있는 main에서 실행할때

        self.ui.show()


if __name__  == "__main__":
    app = QApplication([])
    w=UserForm()
    app.exec()
