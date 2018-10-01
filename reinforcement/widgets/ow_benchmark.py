import numpy as np

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
from .utils.sliders_widget_mixin import SlidersWidgetMixin
from .utils.chart_shortener_mixin import ChartShortenerMixin


class OWBenchmark(ColorsWidgetMixin, ReinforcementWidget,
                  ChartShortenerMixin, SlidersWidgetMixin):
    id = "orange.widgets.reinforcement.benchmark"
    name = "Benchmark"
    description = """Compare Agents performance."""
    icon = "icons/benchmark_icon.svg"
    priority = 90
    keywords = ["OpenAI Gym", "Enviroment", "Info", "Details"]

    want_main_area = True
    resizing_enabled = True

    graph_name = "plot"

    agent = None
    enviroment_id = None

    selected_agents = Setting([])
    setting_max_points = Setting(200)
    setting_first_and_last_values = Setting(False)

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

    def sliders(self):
        return [
            {'label': 'Max Points:', 'key': 'setting_max_points',
             'min': 10, 'max': 1000, 'step': 200,
             'callback': self.settings_changed}]

    def render_layout(self):
        gui.separator(self.controlArea, 0, 6)

        gui.checkBox(self.controlArea, self,
                     'setting_first_and_last_values',
                     'Absolute first and last values.',
                     callback=self.on_agents_changed)

        self.render_sliders(self.sliders(), 200, 2)

        self.render_plot_views()

        gui.separator(self.controlArea, 0, 6)

        cbox = gui.vBox(self.controlArea, "Agents:")
        cbox.setFlat(True)

        self.list_box = gui.listBox(cbox,
                                    self,
                                    "selected_agents",
                                    "agent_names",
                                    selectionMode=QListView.MultiSelection,
                                    callback=self.on_agents_changed)

    PLOT_VIEWS = [{'title': 'Total Reward',
                       'key': 'settings_plot_total_reward',
                       'invert_y': False},
                      {'title': 'Steps to Finish',
                       'key': 'settings_plot_steps_to_finish',
                       'invert_y': True},
                      {'title': 'Epsilon Greedy',
                       'key': 'settings_plot_epsilon_greedy',
                       'invert_y': False}]

    def on_plot_views_changed(self):
        for i, plot_view in enumerate(self.PLOT_VIEWS):
            self.plot_areas[i].setParent(None)

        if self.settings_plot_total_reward:
            self.mainArea.layout().addWidget(self.plot_areas[0], True)

        if self.settings_plot_steps_to_finish:
            self.mainArea.layout().addWidget(self.plot_areas[1], True)

        if self.settings_plot_epsilon_greedy:
            self.mainArea.layout().addWidget(self.plot_areas[2], True)
            

    def render_plot_views(self):
        box = gui.widgetBox(self.controlArea, box=True)

        self.settings_plot_total_reward = True
        self.settings_plot_steps_to_finish = True
        self.settings_plot_epsilon_greedy = True

        for i, plot_view in enumerate(self.PLOT_VIEWS):
            gui.checkBox(box, self,
                     plot_view['key'],
                     plot_view['title'],
                     callback=self.on_plot_views_changed)

            self.render_plot_area(i, plot_view['title'], plot_view['invert_y'])

        self.on_plot_views_changed()

    def settings_changed(self):
        self.render_agents_lines()

    def on_agents_changed(self):
        self.render_agents_lines()

    def render_agents_lines(self):
        self.plot_items[0].clear()
        self.plot_items[1].clear()
        self.plot_items[2].clear()

        self.generate_colors(len(self.agents))

        for i in range(len(self.agents)):
            item = self.list_box.item(i)
            if item:
                item.setIcon(colorpalette.ColorPixmap(self.colors[i]))

            if i in self.selected_agents and self.agents[i].train_results:
                result_line = self.agent_result_to_line(self.agents[i],
                                                        'total_reward')

                self.add_line(0, i, {'x': result_line['x'],
                                     'y': result_line['y']})

                result_line = self.agent_result_to_line(self.agents[i],
                                                        'steps_to_finish')

                self.add_line(1, i, {'x': result_line['x'],
                                     'y': result_line['y']})

                result_sample = self.agents[i].train_results[0]

                if 'epsilon_greedy' in result_sample['last_action_info']:
                    result_line = self.agent_result_to_line(self.agents[i],
                                                            'last_action_info',
                                                            'epsilon_greedy')

                    self.add_line(2, i, {'x': result_line['x'],
                                         'y': result_line['y']})

    def agent_result_to_line(self, agent, key, sub_key=None):
        x_points = np.empty(0)
        y_points = np.empty(0)

        if sub_key:
            map_lambda = map(lambda result: result[key][sub_key],
                             agent.train_results)
        else:
            map_lambda = map(lambda result: result[key],
                             agent.train_results)

        result_values_for_key = np.fromiter(map_lambda, np.float64)

        bool_first_and_last_values = bool(self.setting_first_and_last_values)

        shortened_results = self.shorten_points(result_values_for_key,
                                                int(self.setting_max_points),
                                                bool_first_and_last_values)

        for episode in shortened_results:
            result = shortened_results[episode]

            x_value = episode
            y_value = result

            x_points = np.append(x_points, x_value)
            y_points = np.append(y_points, y_value)

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

    def render_plot_area(self, i, y_label, invert_y=False):
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
        axis.setLabel("Episode")

        axis = self.plot_items[i].getAxis("left")
        axis.setTickFont(tickfont)
        axis.setPen(pen)
        axis.setLabel(y_label)

        self.plot_areas[i].setCentralItem(self.plot_items[i])
