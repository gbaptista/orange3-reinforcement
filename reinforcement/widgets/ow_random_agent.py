from Orange.widgets.widget import Input

from .bases.agent_widget import AgentWidget

from .agents.random.random_agent import RandomAgent


class OWRandomAgent(AgentWidget):
    id = "orange.widgets.reinforcement.random_agent"
    name = "Random Agent"
    description = """Random Agent."""
    icon = "icons/random_agent_icon.svg"

    class Inputs:
        enviroment_id = Input("Enviroment", str)

    @Inputs.enviroment_id
    def set_enviroment_id(self, enviroment_id):
        self.build_and_send_agent(enviroment_id, RandomAgent)
