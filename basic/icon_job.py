import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QToolTip, QMainWindow, QHBoxLayout, QVBoxLayout


class MyIcon(QWidget): # 위젯 상속받기 / QMainwindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("img/web.svg"))

        self.setGeometry(100, 100, 300, 200) # 좌표 / 폭

        btn = QPushButton("quit",self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())

        btn2 = QPushButton("setStatusMessage",self)
        btn2.move(150,50)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(btn2)
        hbox.addStretch(2)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(QPushButton("test1"))
        hbox2.addWidget(QPushButton("test2"))
        hbox2.addStretch(2)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        vbox.addStretch(1)


        # self.setLayout(hbox) # 전체 레이아웃을 hbox로 잡겠다
        self.setLayout(vbox)  # 전체 레이아웃을 vbox로 잡겠다


        # self.statusBar().showMessage('Ready', 3000) # 3초간 보여짐(생략가능)
        # self.statusBar().clearMessage()
        # btn.clicked.connect(self.clearStatus)   # btn 클릭시 clearStatus함수 실행.
        # btn2.clicked.connect(self.setStatusMsg) # btn2 클릭시 setStatusMsg 함수 실행

        #풍선 도우말
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # QCoreApplication.instance() 생성된 개체에 quit명령을 줌
        # btn.clicked.connect(QCoreApplication.instance().quit)
        self.show()     # 이거써야 보임



    def setStatusMsg(self):
        self.statusBar().showMessage("set Message")


    def clearStatus(self):
        self.statusBar().clearMessage()     # 메세지 클리어






if __name__ == "__main__":
    app = QApplication([])
    w= MyIcon()
    app.exec()
