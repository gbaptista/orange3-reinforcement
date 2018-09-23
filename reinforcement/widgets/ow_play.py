from Orange.widgets import gui

from Orange.widgets.widget import Input

from Orange.widgets.settings import Setting

from .agents.agent import Agent

from .utils.sliders_widget_mixin import SlidersWidgetMixin
from .bases.reinforcement_widget import ReinforcementWidget


class OWPlay(SlidersWidgetMixin, ReinforcementWidget):
    id = "orange.widgets.reinforcement.play"
    name = "Play"
    description = """Play Open IA Enviroment with some Agent."""
    icon = "icons/play_icon.svg"
    priority = 80
    keywords = ["OpenAI Gym", "Enviroment", "Play", "Agent"]

    # 0.04 seconds = 40 milliseconds
    setting_episodes_interval = Setting(40)

    # 0.5 seconds = 500 milliseconds
    setting_games_interval = Setting(500)

    class Inputs:
        agent = Input("Agent", Agent)

    def __init__(self):
        super().__init__()

        self.agent = None
        self.enviroment_id = 'Not received.'

        gui.separator(self.controlArea, 0, 6)

        gui.label(self.controlArea, self, "%%(%s)s" % 'enviroment_id')

        self.render_sliders(self.sliders())

        gui.separator(self.controlArea, 0, 10)

        gui.button(self.controlArea, self, "Play", callback=self.play)
        gui.button(self.controlArea, self, "Stop", callback=self.stop)

    def settings_changed(self):
        if self.agent is not None:
            self.agent.episodes_interval = (self.setting_episodes_interval
                                            / 1000)

            self.agent.games_interval = self.setting_games_interval / 1000

    def sliders(self):
        return [
            {'label': 'Interval between episodes (milliseconds):',
             'key': 'setting_episodes_interval',
             'min': 0, 'max': 200, 'step': 10,
             'callback': self.settings_changed},
            {'label': 'Interval between games  (milliseconds):',
             'key': 'setting_games_interval',
             'min': 0, 'max': 2000, 'step': 100,
             'callback': self.settings_changed}]

    def play(self):
        self.agent.play()

    def stop(self):
        self.agent.stop()

    @Inputs.agent
    def set_agent(self, agent):
        if agent is not None:
            self.agent = agent
            self.enviroment_id = self.agent.enviroment_id

            self.settings_changed()
