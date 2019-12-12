from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QAbstractItemView, QHeaderView, QTableWidgetItem, QAction, \
    QMessageBox


class DepartUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dept_form.ui")  # 밖에 있는 main에서 실행할때
        self.ui.show()


        self.ui.tableWidget.setHorizontalHeaderLabels(["부서번호", "부서명", "위치"]) # 바로 넣어 주기

        # row단위 선택 / 그전에는 셀 단위로 선택 되었음
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 수정 불가능
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 균일한 간격으로 재배치
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_del.clicked.connect(self.delete_item)
        self.ui.btn_init.clicked.connect(self.init_item)
        self.ui.btn_update.hide()
        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.tableWidget)

        data = [(1,"마케팅", 8), (2, "개발", 10), (3,"인사",20)]   # data 넣기
        self.load_data(data)

    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):  # enumerate 0, 1, 2 담긴다

            item_no, item_name, item_floor = self.create_item(no, name, floor)

            nextIdx =  self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(nextIdx)
            self.ui.tableWidget.setItem(nextIdx, 0, item_no)
            self.ui.tableWidget.setItem(nextIdx, 1, item_name)
            self.ui.tableWidget.setItem(nextIdx, 2, item_floor)


    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)  # 바로가기 메뉴를 달겠다.
        update_action = QAction("수정할 자료 불러오기", tv)
        delete_action = QAction("삭제할 열 선택하기", tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)



    def __update(self):
        QMessageBox.information(self, 'Update', "수정할 자료를 불러오겠습니다.", QMessageBox.Ok)
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.le_no.setText(self.ui.tableWidget.item(selectionIdxs.row(), 0).text())
        self.ui.le_name.setText(self.ui.tableWidget.item(selectionIdxs.row(),1).text())
        self.ui.le_floor.setText(self.ui.tableWidget.item(selectionIdxs.row(),2).text())
        self.ui.btn_update.show()


    def __delete(self):
        QMessageBox.information(self, 'Delete', "삭제 하겠습니다.", QMessageBox.Ok)
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]  # 여러개중 하나 선택하기
        self.ui.tableWidget.removeRow(selectionIdxs.row())  # row 선택해서 삭제하기


    def add_item(self):
        item_no, item_name, item_floor = self.get_item_from_le() # 밑에서 받아오기
        currentIdx = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(currentIdx)       # Row 추가

        self.ui.tableWidget.setItem(currentIdx, 0, item_no)
        self.ui.tableWidget.setItem(currentIdx, 1, item_name)
        self.ui.tableWidget.setItem(currentIdx, 2, item_floor)
        self.init_item()



    def get_item_from_le(self):
        no    = self.ui.le_no.text()
        name  = self.ui.le_name.text()
        floor = self.ui.le_floor.text()
        return self.create_item(no, name, floor)


    def create_item(self, no, name, floor):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)  # Qt Core
        item_no.setData(Qt.DisplayRole, no)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        item_floor = QTableWidgetItem()
        item_floor.setTextAlignment(Qt.AlignCenter)
        item_floor.setData(Qt.DisplayRole, floor)

        return item_no, item_name, item_floor


    def update_item(self):
        item_no, item_name, item_floor = self.get_item_from_le()  # 밑에서 받아오기
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]


        self.ui.tableWidget.setItem(selectionIdxs.row(), 0, item_no)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 1, item_name)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 2, item_floor)
        self.init_item()
        self.ui.btn_update.hide()

    def delete_item(self):
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]  # 여러개중 하나 선택하기
        self.ui.tableWidget.removeRow(selectionIdxs.row())  # row 선택해서 삭제하기


    def init_item(self):
        self.ui.le_no.clear()
        self.ui.le_name.clear()
        self.ui.le_floor.clear()


if __name__  == "__main__":
    app = QApplication([])
    w=DepartUI()
    app.exec_()