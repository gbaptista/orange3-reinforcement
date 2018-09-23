import gym

from Orange.widgets import gui

from Orange.widgets.widget import Input

from .bases.reinforcement_widget import ReinforcementWidget


class OWChecker(ReinforcementWidget):
    id = "orange.widgets.reinforcement.checker"
    name = "Checker"
    description = """Check Open IA Enviroment."""
    icon = "icons/checker_icon.svg"
    priority = 80
    keywords = ["OpenAI Gym", "Enviroment", "Checker", "Debug"]

    enviroment = None

    class Inputs:
        enviroment_id = Input("Enviroment", str)

    def __init__(self):
        super().__init__()

        self.set_enviroment_id(None)

        gui.label(self.controlArea, self, "%%(%s)s" % 'enviroment_id')

        gui.button(self.controlArea, self, "Open", callback=self.open)
        gui.button(self.controlArea, self, "Close", callback=self.close)

    def close(self):
        self.enviroment.close()

    def open(self):
        if self.enviroment:
            self.enviroment.close()

        self.enviroment = gym.make(self.enviroment_id)
        self.enviroment.reset()
        self.enviroment.render()

    @Inputs.enviroment_id
    def set_enviroment_id(self, enviroment_id):
        self.enviroment_id = 'Not found.'

        if enviroment_id is not None:
            self.enviroment_id = enviroment_id
