from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# 假设你已经用 pyuic6 生成了 Ui_Form
class MyForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 创建 matplotlib 画布
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # 把 canvas 放到 Qt Designer 里你放的那个 widget 里
        layout = QVBoxLayout(self.ui.widget_plot)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)

        # 随便画个图
        self.plot_something()

    def plot_something(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot([0, 1, 2], [1, 4, 9])
        ax.set_title("嵌入式 Matplotlib 图")
        self.canvas.draw()

import numpy as np
import matplotlib.pyplot as plt  # 可选，用于 colormap 名称等

def plot(self):
    self.figure.clear()
    ax = self.figure.add_subplot(111)

    # 创建 6x6 的随机矩阵数据
    data = np.random.rand(6, 6)

    # 使用 imshow 显示热力图
    heatmap = ax.imshow(data, cmap='hot', interpolation='nearest')

    # 添加颜色条
    self.figure.colorbar(heatmap, ax=ax)

    ax.set_title("热力图示例")
    self.canvas.draw()


import sys
import pandas as pd
from PyQt6 import QtWidgets
from read_excel_ui import Ui_Form  # 假设你把生成的类保存为 read_excel_ui.py


class ExcelApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.df = None  # 存储 DataFrame

        # 连接按钮事件
        self.ui.pushButton.clicked.connect(self.load_excel)
        self.ui.pushButton_2.clicked.connect(self.export_excel)

    def load_excel(self):
        file_dialog = QtWidgets.QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "选择 Excel 文件", "", "Excel Files (*.xlsx *.xls)")

        if file_path:
            try:
                self.df = pd.read_excel(file_path)
                self.show_in_table(self.df)
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "错误", f"读取文件失败：{e}")

    def show_in_table(self, df):
        table = self.ui.tableWidget
        table.clear()
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(df.columns.astype(str))

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QtWidgets.QTableWidgetItem(str(df.iat[row, col]))
                table.setItem(row, col, item)

    def export_excel(self):
        if self.df is None:
            QtWidgets.QMessageBox.warning(self, "提示", "请先读取 Excel 文件")
            return

        folder_dialog = QtWidgets.QFileDialog(self)
        folder = folder_dialog.getExistingDirectory(self, "选择保存文件夹")
        if folder:
            save_path = f"{folder}/导出数据.xlsx"
            try:
                self.df.to_excel(save_path, index=False)
                QtWidgets.QMessageBox.information(self, "成功", f"数据已保存到：{save_path}")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "错误", f"保存失败：{e}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ExcelApp()
    window.show()
    sys.exit(app.exec())
