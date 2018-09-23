from Orange.widgets.widget import Input

from .bases.agent_widget import AgentWidget

from .agents.q_learning.q_learning_agent import QLearningAgent


class OWQLearningAgent(AgentWidget):
    id = "orange.widgets.reinforcement.q_learning_agent"
    name = "Q-learning Agent"
    description = """Q-learning Agent."""
    icon = "icons/q_learning_agent_icon.svg"

    class Inputs:
        enviroment_id = Input("Enviroment", str)

    @Inputs.enviroment_id
    def set_enviroment_id(self, enviroment_id):
        self.build_and_send_agent(enviroment_id, QLearningAgent)
