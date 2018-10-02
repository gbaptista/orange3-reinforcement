from copy import copy

import numpy as np

from AnyQt.QtWidgets import QListView

from Orange.widgets import gui
from Orange.widgets.widget import Input
from Orange.widgets.settings import Setting
from Orange.widgets.utils import colorpalette

from .agents.agent import Agent

from .bases.reinforcement_widget import ReinforcementWidget
from .utils.colors_widget_mixin import ColorsWidgetMixin
from .utils.sliders_widget_mixin import SlidersWidgetMixin
from .utils.chart_shortener_mixin import ChartShortenerMixin
from .utils.plot_areas_widget_mixin import PlotAreasWidgetMixin


class OWBenchmark(ColorsWidgetMixin, ReinforcementWidget,
                  ChartShortenerMixin, SlidersWidgetMixin,
                  PlotAreasWidgetMixin):
    id = "orange.widgets.reinforcement.benchmark"
    name = "Benchmark"
    description = """Compare Agents performance."""
    icon = "icons/benchmark_icon.svg"
    priority = 90
    keywords = ["OpenAI Gym", "Environment", "Info", "Details"]

    want_main_area = True
    resizing_enabled = True

    agent = None
    environment_id = None

    selected_agents = Setting([])
    setting_max_points = Setting(200)
    setting_first_and_last_values = Setting(False)

    settings_plot_total_reward = Setting(True)
    settings_plot_steps_to_finish = Setting(False)
    settings_plot_epsilon_greedy = Setting(False)

    class Inputs:
        agent = Input("Agent", Agent, multiple=True)

    def __init__(self):
        super().__init__()

        self.agents = []

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
                     callback=self.settings_changed)

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
                                    callback=self.settings_changed)

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
        for i, _plot_view in enumerate(self.PLOT_VIEWS):
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

            self.render_plot_area(i, 'Episode',
                                  plot_view['title'],
                                  plot_view['invert_y'])

        self.on_plot_views_changed()

    def settings_changed(self):
        self.render_agents_lines()

    def set_agent_color(self, agent_index):
        item = self.list_box.item(agent_index)

        if item:
            item.setIcon(colorpalette.ColorPixmap(self.colors[agent_index]))

    def render_agents_lines(self):
        self.plot_items[0].clear()
        self.plot_items[1].clear()
        self.plot_items[2].clear()

        self.generate_colors(len(self.agents))

        for agent_index in range(len(self.agents)):
            self.set_agent_color(agent_index)

            has_train_results = bool(len(
                self.agents[agent_index].train_results
            ))

            if agent_index in self.selected_agents and has_train_results:
                self.render_result_lines_for_agent(agent_index)

    def render_result_lines_for_agent(self, agent_index):
        self.render_agent_result_line(agent_index, 0, ('total_reward', None))

        self.render_agent_result_line(agent_index, 1,
                                      ('steps_to_finish', None))

        result_sample = self.agents[agent_index].train_results[0]

        if 'epsilon_greedy' in result_sample['last_action_info']:
            self.render_agent_result_line(agent_index, 1,
                                          ('last_action_info',
                                           'epsilon_greedy'))

    def render_agent_result_line(self, agent_index, line_index, keys):
        key, sub_key = keys

        result_line = self.agent_result_to_line(self.agents[agent_index],
                                                key, sub_key)

        self.add_line(line_index, agent_index, {'x': result_line['x'],
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

    def rebuild_agents_list(self, channel_id, agent):
        old_agents = copy(self.agents)

        self.agents = []
        for old_agent in old_agents:
            if old_agent.channel_id != channel_id:
                self.agents.append(old_agent)

        self.agents.append(agent)

    @Inputs.agent
    def set_agent(self, agent, channel):
        if agent is not None:
            channel_id = channel[0]

            agent.channel_id = channel_id

            self.rebuild_agents_list(channel_id, agent)

            self.agent_names = [agent.name for agent in self.agents]
            self.selected_agents = list(range(len(self.agents)))

            self.render_agents_lines()
