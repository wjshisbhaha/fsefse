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


