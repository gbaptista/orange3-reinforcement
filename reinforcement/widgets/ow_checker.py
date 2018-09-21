import gym

from Orange.widgets import gui

from Orange.widgets.widget import Input

from .reinforcement_widget import ReinforcementWidget


class OWChecker(ReinforcementWidget):
    id = "orange.widgets.reinforcement.checker"
    name = "Checker"
    description = """Check Open IA Enviroment."""
    icon = "icons/ataricontrol.png"
    priority = 80
    category = "Reinforcement"
    keywords = ["OpenAI Gym", "Enviroment", "Checker", "Debug"]

    enviroment = None

    class Inputs:
        enviroment_id = Input("Enviroment", str)

    def __init__(self):
        super().__init__()

        self.set_enviroment_id(None)

        gui.label(self.controlArea, self, "%%(%s)s" % 'enviroment_id')

        gui.button(self.controlArea, self, "Start", callback=self.start_render)
        gui.button(self.controlArea, self, "Stop", callback=self.stop_render)

    def stop_render(self):
        self.enviroment.close()

    def start_render(self):
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
