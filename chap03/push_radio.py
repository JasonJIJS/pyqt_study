from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QHeaderView


class PushRadioUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("push_radio_btns.ui")  # 밖에 있는 main에서 실행할때
        self.ui.show()

        self.ui.btn_ok.pressed.connect(self.clickshow)
        self.ui.btn_cancel.pressed.connect(self.clickshow2)

        self.ui.rb_male.pressed.connect(self.male_check)
        self.ui.rb_female.pressed.connect(self.female_check)


        self.tbl_widget = self.ui.table_widget           # 이걸로 참조하겠다.

        # 글자는 왼쪽 정렬
        self.tbl_widget.setItem(0,0, QTableWidgetItem("cell(0,0)"))

        # 글자 중앙 정렬
        item = QTableWidgetItem("cell(0,1)")
        item.setTextAlignment(Qt.AlignCenter)
        self.tbl_widget.setItem(0,1, item)

        # 글자 오른쪽 정렬
        item1 = QTableWidgetItem("cell(0,2)")
        item1.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tbl_widget.setItem(0,2, item1)

        # 헤더에 글자 넣기
        table_header = ["첫번째", "두번째", "세번째"]
        self.tbl_widget.setHorizontalHeaderLabels(table_header)

        # row단위 선택 / 그전에는 셀 단위로 선택 되었음
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 수정 불가능
        self.tbl_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 균일한 간격으로 재배치
        self.tbl_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.ui.btn_input.clicked.connect(self.input_table_item)

        # 삭제 하기
        self.ui.btn_del.clicked.connect(self.tbl_del_item)

    def tbl_del_item(self):
        selectionIdxs = self.tbl_widget.selectedIndexes()[0]        # 여러개중 하나 선택하기
        print(selectionIdxs.row()," ", selectionIdxs.column())
        self.tbl_widget.removeRow(selectionIdxs.row())              # row 선택해서 삭제하기


    def input_table_item(self):
        item = QTableWidgetItem("cell(1,1)")
        item.setTextAlignment(Qt.AlignCenter)
        currentRowCount = self.tbl_widget.rowCount()
        # print(currentRowCount)      # 확인위해 찍어봄
        self.tbl_widget.insertRow(currentRowCount)          # 한 줄 추가 하는 것

        v1 = self.ui.le_01.text()
        v2 = self.ui.le_02.text()
        v3 = self.ui.le_03.text()

        item01 = QTableWidgetItem(v1)
        item01.setTextAlignment(Qt.AlignCenter)
        item02 = QTableWidgetItem(v2)
        item02.setTextAlignment(Qt.AlignCenter)
        item03 = QTableWidgetItem(v3)
        item03.setTextAlignment(Qt.AlignCenter)

        print(v1)

        # self.tbl_widget.setItem(currentRowCount, 0, QTableWidgetItem("cell(1,0)"))
        # self.tbl_widget.setItem(currentRowCount, 1, QTableWidgetItem("cell(1,1)"))
        # self.tbl_widget.setItem(currentRowCount, 2, QTableWidgetItem("cell(1,2)"))
        # self.tbl_widget.setItem(currentRowCount, 0, QTableWidgetItem(v1))
        # self.tbl_widget.setItem(currentRowCount, 1, QTableWidgetItem(v2))
        # self.tbl_widget.setItem(currentRowCount, 2, QTableWidgetItem(v3))
        self.tbl_widget.setItem(currentRowCount, 0, QTableWidgetItem(item01))
        self.tbl_widget.setItem(currentRowCount, 1, QTableWidgetItem(item02))
        self.tbl_widget.setItem(currentRowCount, 2, QTableWidgetItem(item03))



    def clickshow(self):
        self.ui.lbl_push_res.setText(self.ui.btn_ok.text())

    def clickshow2(self):
        self.ui.lbl_push_res.setText(self.ui.btn_cancel.text())

    def male_check(self):
        self.ui.lbl_rb_res.setText(self.ui.rb_male.text())


    def female_check(self):
        self.ui.lbl_rb_res.setText(self.ui.rb_female.text())




if __name__  == "__main__":
    app = QApplication([])
    w=PushRadioUI()
    app.exec_()