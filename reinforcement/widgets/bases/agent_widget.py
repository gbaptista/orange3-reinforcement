from AnyQt.QtCore import Qt

from Orange.widgets import gui

from Orange.widgets.settings import Setting
from Orange.widgets.widget import Output

from ..agents.agent import Agent

from ..utils.auto_apply_widget_mixin import AutoApplyWidgetMixin
from .reinforcement_widget import ReinforcementWidget


class AgentWidget(AutoApplyWidgetMixin, ReinforcementWidget):
    priority = 80
    keywords = ["OpenAI Gym", "Enviroment", "Info", "Details"]

    agent = None
    enviroment_id = None

    setting_agent_name = Setting('')

    class Outputs:
        agent = Output("Agent", Agent)

    def __init__(self):
        super().__init__()

        self.setting_agent_name = self.name

        self.apply()
        self.render_layout()

    def render_layout(self):
        self.name_line_edit = gui.lineEdit(
            self.controlArea, self, 'setting_agent_name', box='Name',
            tooltip='The name will identify this model in other widgets',
            orientation=Qt.Horizontal, callback=self.settings_changed)

        self.render_auto_apply_layout()

    def apply(self):
        if self.agent is not None:
            self.agent.name = self.setting_agent_name

            self.Outputs.agent.send(self.agent)

        self.clear_outdated_warning()

    def build_and_send_agent(self, enviroment_id, agent_class):
        if enviroment_id is not None:
            self.enviroment_id = enviroment_id

            self.agent = agent_class(enviroment_id)

            self.agent.name += ' (' + enviroment_id + ')'

            if self.setting_agent_name == self.name:
                self.setting_agent_name = self.agent.name
            else:
                self.agent.name = self.setting_agent_name

            self.Outputs.agent.send(self.agent)
