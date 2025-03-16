import sys
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem,QApplication,QWidget
from ui.http_client import Ui_Form
from luoji.requ import requs


class MyShow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Push_url.clicked.connect(self.Submit_Url)
        self.jia_button.clicked.connect(self.add_row)
        self.jian_button.clicked.connect(self.remove_row)


    def add_row(self):
        row_posttion = self.movetable.rowCount()
        self.movetable.insertRow(row_posttion)

    def remove_row(self):
        select_row = self.movetable.currentRow()
        if select_row >= 0:
            self.movetable.removeRow(select_row)
    def Submit_Url(self):
        url = self.Url_name.text().strip()
        if url:
            method = self.select_box.currentText()  # 获取选择的请求方式

            # 获取电影信息
            movies = requs(url, method)

            # 清空之前的显示
            self.movetable.setRowCount(0)

            # 将电影信息显示到表格
            for movie in movies:
                row_position = self.movetable.rowCount()
                self.movetable.insertRow(row_position)
                self.movetable.setItem(row_position, 0, QTableWidgetItem(movie[0]))  # 电影名
                self.movetable.setItem(row_position, 1, QTableWidgetItem(movie[1]))  # 导演
                self.movetable.setItem(row_position, 2, QTableWidgetItem(movie[3]))  # 评分
                self.movetable.setItem(row_position, 3, QTableWidgetItem(movie[4]))
        else:
            self.data_text.setPlainText('请输入有效的 URL')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyShow()
    window.show()
    sys.exit(app.exec())
