from AnyQt.QtCore import pyqtSlot

from Orange.widgets.widget import Input, Output

from Orange.widgets.utils.concurrent import methodinvoke

from .agents.agent import Agent
from .agents.random.random_agent import RandomAgent

from .agent_widget import AgentWidget


class OWRandomAgent(AgentWidget):
    id = "orange.widgets.reinforcement.random_agent"
    name = "Random Agent"
    description = """Random Agent."""

    agent = None
    enviroment_id = None

    class Inputs:
        enviroment_id = Input("Enviroment", str)

    class Outputs:
        agent = Output("Agent", Agent)

    @pyqtSlot()
    def on_finish(self):
        self.Outputs.agent.send(self.agent)

    @Inputs.enviroment_id
    def set_enviroment_id(self, enviroment_id):
        if enviroment_id is not None:
            self.enviroment_id = enviroment_id

            self.agent = RandomAgent(enviroment_id, ow_widget=self)

            # TODO: Slider
            self.agent.train(100, methodinvoke(self, "on_finish"))
