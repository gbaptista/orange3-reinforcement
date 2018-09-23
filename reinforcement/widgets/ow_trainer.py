from copy import deepcopy

from AnyQt.QtCore import pyqtSlot

from Orange.widgets import gui

from Orange.widgets.widget import Input, Output

from Orange.widgets.settings import Setting

from Orange.widgets.utils.concurrent import methodinvoke

from .agents.agent import Agent

from .utils.auto_apply_widget_mixin import AutoApplyWidgetMixin
from .bases.reinforcement_widget import ReinforcementWidget


class OWTrainer(AutoApplyWidgetMixin, ReinforcementWidget):
    id = "orange.widgets.reinforcement.trainer"
    name = "Trainer"
    description = """Train some Agent."""
    icon = "icons/ataricontrol.png"
    priority = 80
    keywords = ["OpenAI Gym", "Enviroment", "Train", "Agent"]

    setting_auto_apply = Setting(False)

    setting_episodes = Setting(10)
    setting_seconds = Setting(5)
    setting_minutes = Setting(0)
    setting_hours = Setting(0)
    setting_days = Setting(0)

    sliders = [
        {'label': 'Episodes:', 'key': 'setting_episodes',
         'min': 0, 'max': 999, 'step': 10},
        {'label': 'Seconds:', 'key': 'setting_seconds',
         'min': 0, 'max': 60, 'step': 5},
        {'label': 'Minutes:', 'key': 'setting_minutes',
         'min': 0, 'max': 60, 'step': 5},
        {'label': 'Hours:', 'key': 'setting_hours',
         'min': 0, 'max': 24, 'step': 1},
        {'label': 'Days:', 'key': 'setting_days',
         'min': 0, 'max': 45, 'step': 1}]

    class Inputs:
        agent = Input("Agent", Agent)

    class Outputs:
        agent = Output("Agent", Agent)

    def __init__(self):
        super().__init__()

        self.set_agent(None)

        for slider in self.sliders:
            gui.separator(self.controlArea, 0, 10)

            gui.widgetLabel(self.controlArea, slider['label'])

            gui.hSlider(
                self.controlArea, self, slider['key'],
                minValue=slider['min'], maxValue=slider['max'],
                intOnly=False, ticks=1, createLabel=True, width=300,
                step=slider['step'])

        self.render_auto_apply_layout()

    def apply(self):
        self.agent.train(int(self.setting_episodes),
                         self.seconds(),
                         self,
                         methodinvoke(self, "on_finish"))

    def seconds(self):
        seconds = self.setting_seconds

        seconds += self.setting_minutes * 60
        seconds += self.setting_hours * 60 * 60
        seconds += self.setting_days * 24 * 60 * 60

        return int(seconds)

    @pyqtSlot()
    def on_finish(self):
        self.Outputs.agent.send(self.agent)

    @Inputs.agent
    def set_agent(self, agent):
        self.agent = None
        self.enviroment_id = 'Not received.'

        if agent is not None:
            agent.prepare_to_pickle()

            self.agent = deepcopy(agent)

            self.agent.initial_trained_episodes = agent.trained_episodes
            self.agent.initial_train_results = deepcopy(agent.train_results)

            self.enviroment_id = self.agent.enviroment_id

            self.agent.train(int(self.setting_episodes),
                             self.seconds(),
                             self,
                             methodinvoke(self, "on_finish"))
