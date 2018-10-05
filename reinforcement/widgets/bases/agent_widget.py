from AnyQt.QtCore import Qt

from Orange.widgets import gui

from Orange.widgets.settings import Setting
from Orange.widgets.widget import Input, Output

from ..agents.agent import Agent

from ..utils.auto_apply_widget_mixin import AutoApplyWidgetMixin
from .reinforcement_widget import ReinforcementWidget


class AgentWidget(AutoApplyWidgetMixin, ReinforcementWidget):
    priority = 70
    keywords = ["OpenAI Gym", "Environment", "Info", "Details"]

    agent = None
    environment_id = None

    setting_agent_name = Setting(None)

    class Inputs:
        environment_id = Input("Environment", str)

    class Outputs:
        agent = Output("Agent", Agent)

    def __init__(self):
        super().__init__()

        if not self.setting_agent_name:
            self.setting_agent_name = self.name

        self.apply()
        self.render_layout()

    def render_layout(self):
        self.name_line_edit = gui.lineEdit(
            self.controlArea, self, 'setting_agent_name', box='Name',
            tooltip='The name will identify this model in other widgets',
            orientation=Qt.Horizontal, callback=self.settings_changed)

        self.render_custom_layout()

        self.render_auto_apply_layout()

    def render_custom_layout(self):
        pass

    @Inputs.environment_id
    def set_environment_id(self, environment_id):
        pass

    def apply(self):
        if self.agent is not None:
            self.agent.name = self.setting_agent_name

            self.Outputs.agent.send(self.agent)

        self.clear_outdated_warning()

    def set_agent_settings(self):
        pass

    def build_and_send_agent(self, environment_id, agent_class):
        if environment_id is not None:
            self.environment_id = environment_id

            self.agent = agent_class(self.environment_id)

            self.set_agent_settings()

            self.Outputs.agent.send(self.agent)
