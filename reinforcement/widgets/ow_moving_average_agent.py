from .bases.agent_widget import AgentWidget

from .agents.moving_average.moving_average_agent import MovingAverageAgent

from .utils.epsilon_greedy_widget_mixin import EpsilonGreedyWidgetMixin


class OWMovingAverageAgent(AgentWidget,
                           EpsilonGreedyWidgetMixin):
    id = "orange.widgets.reinforcement.moving_average_agent"
    name = "Moving Average Agent"
    description = """Moving Average Agent."""
    icon = "icons/moving_average_agent_icon_temp_1.svg"

    def render_custom_layout(self):
        self.render_epsilon_greedy_sliders()

    def set_enviroment_id(self, enviroment_id):
        self.build_and_send_agent(enviroment_id, MovingAverageAgent)

    def set_agent_settings(self):
        self.set_agent_epsilon_greedy_settings()

        super().set_agent_settings()
