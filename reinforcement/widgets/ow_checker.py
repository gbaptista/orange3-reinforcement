import gym

from Orange.widgets import gui

from .bases.environment_input_widget import EnvironmentInputWidget


class OWChecker(EnvironmentInputWidget):
    id = "orange.widgets.reinforcement.checker"
    name = "Checker"
    description = """Check Open IA Environment."""
    icon = "icons/checker_icon.svg"
    priority = 60
    keywords = ["OpenAI Gym", "Environment", "Checker", "Debug"]

    environment = None

    def __init__(self):
        super().__init__()

        self.set_environment_id(None)

        gui.label(self.controlArea, self, "%%(%s)s" % 'environment_id')

        gui.button(self.controlArea, self, "Open", callback=self.open)
        gui.button(self.controlArea, self, "Close", callback=self.close)

    def close(self):
        self.environment.close()

    def open(self):
        if self.environment:
            self.environment.close()

        self.environment = gym.make(self.environment_id)
        self.environment.render()

    def set_environment_id(self, environment_id):
        self.environment_id = 'Not found.'

        if environment_id is not None:
            self.environment_id = environment_id
