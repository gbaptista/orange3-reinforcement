import gym

from Orange.widgets import gui

from .bases.enviroment_input_widget import EnviromentInputWidget


class OWChecker(EnviromentInputWidget):
    id = "orange.widgets.reinforcement.checker"
    name = "Checker"
    description = """Check Open IA Enviroment."""
    icon = "icons/checker_icon.svg"
    priority = 80
    keywords = ["OpenAI Gym", "Enviroment", "Checker", "Debug"]

    enviroment = None

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

    def set_enviroment_id(self, enviroment_id):
        self.enviroment_id = 'Not found.'

        if enviroment_id is not None:
            self.enviroment_id = enviroment_id
