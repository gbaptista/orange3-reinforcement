from Orange.widgets import gui

from Orange.widgets.widget import Input

from .agents.agent import Agent

from .reinforcement_widget import ReinforcementWidget


class OWPlay(ReinforcementWidget):
    id = "orange.widgets.reinforcement.play"
    name = "Play"
    description = """Play Open IA Enviroment with some Agent."""
    icon = "icons/ataricontrol.png"
    priority = 80
    category = "Reinforcement"
    keywords = ["OpenAI Gym", "Enviroment", "Play", "Agent"]

    class Inputs:
        agent = Input("Agent", Agent)

    def __init__(self):
        super().__init__()

        self.set_agent(None)

        self.render_layout()

    def render_layout(self):
        gui.label(self.controlArea, self, "%%(%s)s" % 'enviroment_id')

        gui.button(self.controlArea, self, "Play", callback=self.play)
        gui.button(self.controlArea, self, "Stop", callback=self.stop)

    def play(self):
        self.agent.play()

    def stop(self):
        self.agent.stop()

    @Inputs.agent
    def set_agent(self, agent):
        self.agent = None
        self.enviroment_id = 'Not received.'

        if agent is not None:
            self.agent = agent
            self.enviroment_id = self.agent.enviroment_id
