from AnyQt.QtWidgets import QFrame
from AnyQt.QtWidgets import QListView

from AnyQt.QtGui import QPen, QPalette, QFont

import pyqtgraph as pg

from Orange.widgets import gui
from Orange.widgets.widget import Input
from Orange.widgets.settings import Setting
from Orange.widgets.utils import colorpalette

from .agents.agent import Agent

from .bases.reinforcement_widget import ReinforcementWidget
from .utils.colors_widget_mixin import ColorsWidgetMixin


class OWBenchmark(ColorsWidgetMixin, ReinforcementWidget):
    id = "orange.widgets.reinforcement.benchmark"
    name = "Benchmark"
    description = """Compare Agents performance."""
    icon = "icons/benchmark.png"
    priority = 80
    keywords = ["OpenAI Gym", "Enviroment", "Info", "Details"]

    want_main_area = True
    resizing_enabled = True

    graph_name = "plot"

    agent = None
    enviroment_id = None

    selected_agents = Setting([])

    class Inputs:
        agent = Input("Agent", Agent, multiple=True)

    def __init__(self):
        super().__init__()

        self.agents = {}
        self.agents_by_channel = {}

        self.plot_areas = {}
        self.plot_items = {}

        self.agent_names = []

        self.render_layout()

    def render_layout(self):
        cbox = gui.vBox(self.controlArea, "Agents:")
        cbox.setFlat(True)

        self.list_box = gui.listBox(cbox,
                                    self,
                                    "selected_agents",
                                    "agent_names",
                                    selectionMode=QListView.MultiSelection,
                                    callback=self.on_agents_changed)

        self.render_plot_area(0, 'Total Reward')
        self.render_plot_area(1, 'Steps to Finish')

    def on_agents_changed(self):
        self.render_agents_lines()

    def render_agents_lines(self):
        self.plot_items[0].clear()
        self.plot_items[1].clear()

        self.generate_colors(len(self.agents))

        for i in range(len(self.agents)):
            item = self.list_box.item(i)
            if item:
                item.setIcon(colorpalette.ColorPixmap(self.colors[i]))

            if i in self.selected_agents:
                result_line = self.agent_result_to_line(self.agents[i],
                                                        'total_reward')

                self.add_line(0, i, result_line['x'], result_line['y'])

                result_line = self.agent_result_to_line(self.agents[i],
                                                        'steps_to_finish')

                self.add_line(1, i, result_line['x'], result_line['y'])

    @staticmethod
    def agent_result_to_line(agent, key):
        x_points = []
        y_points = []

        for episode in agent.train_results:
            y_value = agent.train_results[episode][key]
            x_points.append(episode)
            y_points.append(y_value)

        return {'x': x_points, 'y': y_points}

    @Inputs.agent
    def set_agent(self, agent, channel):
        if agent is not None:
            channel_id = channel[0]
            self.agents_by_channel[channel_id] = agent

            self.agents = {}

            i = 0
            for channel_id in self.agents_by_channel:
                self.agents[i] = self.agents_by_channel[channel_id]
                i += 1

            self.agent_names = [self.agents[i].name for i in self.agents]
            self.selected_agents = list(range(len(self.agents)))

            self.render_agents_lines()

    def add_line(self, plot_area_i, line_i, x_values, y_values):
        color = self.colors[line_i]

        pen = QPen(color, 1)
        pen.setCosmetic(True)

        shadow_pen = QPen(pen.color().lighter(160), 2.5)
        shadow_pen.setCosmetic(True)

        line = pg.PlotDataItem(
            x_values, y_values,
            pen=pen, shadowPen=shadow_pen,
            symbol="+", symbolSize=3,
            symbolPen=shadow_pen, antialias=True
        )
        self.plot_items[plot_area_i].addItem(line)

    def render_plot_area(self, i, y_label):
        self.plot_areas[i] = pg.GraphicsView(background="w")
        self.plot_areas[i].setFrameStyle(QFrame.StyledPanel)

        self.plot_items[i] = pg.PlotItem(enableMenu=True)
        self.plot_items[i].setMouseEnabled(False, False)
        self.plot_items[i].hideButtons()

        pen = QPen(self.palette().color(QPalette.Text))

        tickfont = QFont(self.font())
        tickfont.setPixelSize(max(int(tickfont.pixelSize() * 2 // 3), 11))

        axis = self.plot_items[i].getAxis("bottom")
        axis.setTickFont(tickfont)
        axis.setPen(pen)
        axis.setLabel("Episode")

        axis = self.plot_items[i].getAxis("left")
        axis.setTickFont(tickfont)
        axis.setPen(pen)
        axis.setLabel(y_label)

        self.plot_areas[i].setCentralItem(self.plot_items[i])
        self.mainArea.layout().addWidget(self.plot_areas[i])
