from .bases.agent_widget import AgentWidget

from .agents.mean.mean_agent import MeanAgent

from .utils.epsilon_greedy_widget_mixin import EpsilonGreedyWidgetMixin


class OWMeanAgent(AgentWidget, EpsilonGreedyWidgetMixin):
    id = "orange.widgets.reinforcement.mean_agent"
    name = "Mean Agent"
    description = """Mean Agent."""
    icon = "icons/men_agent_icon.svg"

    def render_custom_layout(self):
        self.render_epsilon_greedy_sliders()

    def set_environment_id(self, environment_id):
        self.build_and_send_agent(environment_id, MeanAgent)

    def set_agent_settings(self):
        self.set_agent_epsilon_greedy_settings()

        super().set_agent_settings()
