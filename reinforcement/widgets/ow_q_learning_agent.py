from .bases.agent_widget import AgentWidget

from .agents.q_learning.q_learning_agent import QLearningAgent


class OWQLearningAgent(AgentWidget):
    id = "orange.widgets.reinforcement.q_learning_agent"
    name = "Q-learning Agent"
    description = """Q-learning Agent."""
    icon = "icons/q_learning_agent_icon.svg"

    def set_environment_id(self, environment_id):
        self.build_and_send_agent(environment_id, QLearningAgent)
