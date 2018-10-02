import pyqtgraph as pg

from AnyQt.QtWidgets import QFrame
from AnyQt.QtGui import QPen, QPalette, QFont


class PlotAreasWidgetMixin:
    plot_areas = {}
    plot_items = {}

    def render_plot_area(self, i, x_label, y_label, invert_y=False):
        self.plot_areas[i] = pg.GraphicsView(background="w")
        self.plot_areas[i].setFrameStyle(QFrame.StyledPanel)

        self.plot_items[i] = pg.PlotItem(enableMenu=True)
        self.plot_items[i].setMouseEnabled(False, False)
        self.plot_items[i].hideButtons()
        self.plot_items[i].enableAutoScale()
        self.plot_items[i].enableAutoRange(x=True, y=True)
        self.plot_items[i].showGrid(x=True, y=True, alpha=0.1)

        if invert_y:
            self.plot_items[i].invertY()

        pen = QPen(self.palette().color(QPalette.Text))

        tickfont = QFont(self.font())
        tickfont.setPixelSize(max(int(tickfont.pixelSize() * 2 // 3), 11))

        axis = self.plot_items[i].getAxis("bottom")
        axis.setTickFont(tickfont)
        axis.setPen(pen)
        axis.setLabel(x_label)

        axis = self.plot_items[i].getAxis("left")
        axis.setTickFont(tickfont)
        axis.setPen(pen)
        axis.setLabel(y_label)

        self.plot_areas[i].setCentralItem(self.plot_items[i])

    def add_line(self, plot_area_i, line_i, values):
        color = self.colors[line_i]

        pen = QPen(color, 1)
        pen.setCosmetic(True)

        shadow_pen = QPen(pen.color().lighter(160), 2.5)
        shadow_pen.setCosmetic(True)

        line = pg.PlotDataItem(
            values['x'], values['y'],
            pen=pen, shadowPen=shadow_pen,
            symbol="+", symbolSize=3,
            symbolPen=shadow_pen, antialias=True
        )
        self.plot_items[plot_area_i].addItem(line)
