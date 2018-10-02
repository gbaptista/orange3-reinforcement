from AnyQt.QtCore import Qt

import gym

from Orange.widgets import gui

from Orange.widgets.settings import Setting
from Orange.widgets.utils.signals import Output

from .utils.auto_apply_widget_mixin import AutoApplyWidgetMixin
from .bases.reinforcement_widget import ReinforcementWidget


class OWEnvironment(AutoApplyWidgetMixin, ReinforcementWidget):
    id = "orange.widgets.reinforcement.environment"
    name = "Environment"
    description = "OpenAI Gym Environment."
    icon = "icons/environment_icon.svg"
    priority = 50
    keywords = ["OpenAI Gym", "Environment"]

    setting_auto_apply = Setting(True)
    setting_environment = Setting(-1)

    class Outputs:
        environment_id = Output("Environment", str)

    def __init__(self):
        super().__init__()

        default_environment = 0

        self.setting_environments = ()
        for i, environment in enumerate(gym.envs.registry.all()):
            self.setting_environments += (environment.id,)

            if environment.id == 'FrozenLake-v0':
                default_environment = i

        if self.setting_environment == -1:
            self.setting_environment = default_environment

        self.apply()

        self.render_layout()

    def render_layout(self):
        box = gui.widgetBox(self.controlArea, box=True)

        self.environments_combo = gui.comboBox(
            box, self, "setting_environment", label="Environment: ",
            items=self.setting_environments, orientation=Qt.Horizontal,
            addSpace=4, callback=self.settings_changed
        )

        self.render_auto_apply_layout()

    def apply(self):
        selected_environment = self.setting_environments[
            self.setting_environment
        ]

        self.Outputs.environment_id.send(selected_environment)

        self.clear_outdated_warning()
