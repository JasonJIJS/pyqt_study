from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView


class SaledetailUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/saledetail.ui")  # 밖에 있는 main에서 실행할때
        self.ui.show()
        self.ui.tableWidget.setHorizontalHeaderLabels(["번호", "판매가격", "세금", "공급가격", "마진가"])  # 바로 넣어 주기

        # row단위 선택 / 그전에는 셀 단위로 선택 되었음
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 수정 불가능
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 균일한 간격으로 재배치
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)




