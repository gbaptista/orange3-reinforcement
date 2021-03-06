from .bases.agent_widget import AgentWidget

from .agents.q_learning.q_learning_agent import QLearningAgent

from .utils.epsilon_greedy_widget_mixin import EpsilonGreedyWidgetMixin


class OWQLearningAgent(AgentWidget, EpsilonGreedyWidgetMixin):
    id = "orange.widgets.reinforcement.q_learning_agent"
    name = "Q-learning Agent"
    description = """Q-learning Agent."""
    icon = "icons/q_learning_agent_icon.svg"

    def render_custom_layout(self):
        self.render_epsilon_greedy_sliders()

    def set_environment_id(self, environment_id):
        self.build_and_send_agent(environment_id, QLearningAgent)

    def set_agent_settings(self):
        self.set_agent_epsilon_greedy_settings()

        super().set_agent_settings()
