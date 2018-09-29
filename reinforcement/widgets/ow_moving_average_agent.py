from .bases.agent_widget import AgentWidget

from .agents.moving_average.moving_average_agent import MovingAverageAgent


class OWMovingAverageAgent(AgentWidget):
    id = "orange.widgets.reinforcement.moving_average_agent"
    name = "Moving Average Agent"
    description = """Moving Average Agent."""
    icon = "icons/moving_average_agent_icon_temp_1.svg"

    def set_enviroment_id(self, enviroment_id):
        self.build_and_send_agent(enviroment_id, MovingAverageAgent)
