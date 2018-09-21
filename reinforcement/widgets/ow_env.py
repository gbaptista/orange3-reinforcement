from AnyQt.QtCore import Qt

import gym

from Orange.widgets import gui

from Orange.widgets.widget import OWWidget, Msg
from Orange.widgets.settings import Setting
from Orange.widgets.utils.signals import Output

from .reinforcement_widget import ReinforcementWidget


class OWEnv(ReinforcementWidget):
    id = "orange.widgets.reinforcement.env"
    name = "Enviroment"
    description = "OpenAI Gym Enviroment."
    icon = "icons/OpenAI_Logo.svg"
    priority = 60
    category = "Reinforcement"
    keywords = ["OpenAI Gym", "Enviroment"]

    setting_auto_apply = Setting(True)
    setting_enviroment = Setting(-1)
    outdated_settings = False

    class Outputs:
        enviroment_id = Output("Enviroment", str)

    def __init__(self):
        super().__init__()

        default_enviroment = 0

        self.setting_enviroments = ()
        for i, enviroment in enumerate(gym.envs.registry.all()):
            self.setting_enviroments += (enviroment.id,)

            if enviroment.id == 'CartPole-v1':
                default_enviroment = i

        if self.setting_enviroment == -1:
            self.setting_enviroment = default_enviroment

        self.apply()

        self.render_layout()

    def render_layout(self):
        box = gui.widgetBox(self.controlArea, box=True)

        self.penalty_combo = gui.comboBox(
            box, self, "setting_enviroment", label="Enviroment: ",
            items=self.setting_enviroments, orientation=Qt.Horizontal,
            addSpace=4, callback=self.settings_changed
        )

        self.apply_button = gui.auto_commit(
            self.controlArea, self, 'setting_auto_apply', '&Apply',
            box=True, commit=self.apply
        )

    def settings_changed(self, *_args, **_kwargs):
        self.outdated_settings = True
        self.Warning.outdated_settings(shown=not self.setting_auto_apply)

        if self.setting_auto_apply:
            self.apply()

    def apply(self):
        selected_enviroment = self.setting_enviroments[self.setting_enviroment]

        self.Outputs.enviroment_id.send(selected_enviroment)

        self.outdated_settings = False
        self.Warning.outdated_settings.clear()

    class Warning(OWWidget.Warning):
        outdated_settings = Msg("Press Apply to submit changes.")
