from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QAction, QMessageBox, QTableWidgetItem

from application_coffee_practice.dao.sale_dao import SaleDao


class SaleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/sale.ui")  # 밖에 있는 main에서 실행할때
        self.ui.show()

        self.ui.tableWidget.setHorizontalHeaderLabels(["번호", "코드", "가격", "판매개수", "마진율"])  # 바로 넣어 주기

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

        sale = SaleDao()
        self.load_data(sale.select_item())

        # code, price, saleCnt, marginRate
    def load_data(self, data):
        for idx, (no, code, price, saleCnt, marginRate) in enumerate(data):  # enumerate 0, 1, 2 담긴다
            item_no, item_code, item_price, item_saleCnt, item_marginRate \
            = self.create_item(no, code, price, saleCnt, marginRate)

            nextIdx = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(nextIdx)

            self.ui.tableWidget.setItem(nextIdx, 0, item_no)
            self.ui.tableWidget.setItem(nextIdx, 1, item_code)
            # num = format(int(item_price), ',')
            self.ui.tableWidget.setItem(nextIdx, 2, item_price)

            # self.ui.tableWidget.setItem(nextIdx, 2, num)
            self.ui.tableWidget.setItem(nextIdx, 3, item_saleCnt)
            self.ui.tableWidget.setItem(nextIdx, 4, item_marginRate)


    def set_context_menu(self ,tv):
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
        self.ui.le_code.setText(self.ui.tableWidget.item(selectionIdxs.row(), 0).text())
        self.ui.le_price.setText(self.ui.tableWidget.item(selectionIdxs.row(), 1).text())
        self.ui.le_saleCnt.setText(self.ui.tableWidget.item(selectionIdxs.row(), 2).text())
        self.ui.le_marginRate.setText(self.ui.tableWidget.item(selectionIdxs.row(), 3).text())


    def __delete(self):
        QMessageBox.information(self, 'Delete', "삭제 하겠습니다.", QMessageBox.Ok)
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]  # 여러개중 하나 선택하기
        self.ui.tableWidget.removeRow(selectionIdxs.row())  # row 선택해서 삭제하기


    def add_item(self):
        item_code, item_price, item_saleCnt, item_marginRate = self.get_item_from_le()  # 밑에서 받아오기
        currentIdx = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(currentIdx)  # Row 추가

        self.ui.tableWidget.setItem(currentIdx, 0, item_code)
        self.ui.tableWidget.setItem(currentIdx, 1, item_price)
        self.ui.tableWidget.setItem(currentIdx, 2, item_saleCnt)
        self.ui.tableWidget.setItem(currentIdx, 3, item_marginRate)

        self.init_item()


    def get_item_from_le(self):
        code       = self.ui.le_code.text()
        price      = self.ui.le_name.text()
        saleCnt    = self.ui.le_code.text()
        marginRate = self.ui.le_name.text()

        return self.create_item(code, price, saleCnt, marginRate)


    def create_item(self, no, code, price, saleCnt, marginRate):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)  # Qt Core
        item_no.setData(Qt.DisplayRole, no)
        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignCenter)  # Qt Core
        item_code.setData(Qt.DisplayRole, code)
        item_price = QTableWidgetItem()
        item_price.setTextAlignment(Qt.AlignCenter)
        item_price.setData(Qt.DisplayRole, price)
        item_saleCnt = QTableWidgetItem()
        item_saleCnt.setTextAlignment(Qt.AlignCenter)  # Qt Core
        item_saleCnt.setData(Qt.DisplayRole, saleCnt)
        item_marginRate = QTableWidgetItem()
        item_marginRate.setTextAlignment(Qt.AlignCenter)
        item_marginRate.setData(Qt.DisplayRole, marginRate)



        return item_no, item_code, item_price, item_saleCnt, item_marginRate


    def update_item(self):
        item_code, item_price, item_saleCnt, item_marginRate = self.get_item_from_le()  # 밑에서 받아오기
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]

        self.ui.tableWidget.setItem(selectionIdxs.row(), 0, item_code)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 1, item_price)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 2, item_saleCnt)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 3, item_marginRate)
        self.init_item()
        self.ui.btn_update.hide()


    def delete_item(self):
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]  # 여러개중 하나 선택하기
        self.ui.tableWidget.removeRow(selectionIdxs.row())  # row 선택해서 삭제하기


    def init_item(self):
        self.ui.le_code.clear()
        self.ui.le_price.clear()
        self.ui.le_saleCnt.clear()
        self.ui.le_marginRate.clear()






