from .bases.agent_widget import AgentWidget

from .agents.random.random_agent import RandomAgent


class OWRandomAgent(AgentWidget):
    id = "orange.widgets.reinforcement.random_agent"
    name = "Random Agent"
    description = """Random Agent."""
    icon = "icons/random_agent_icon.svg"

    def set_environment_id(self, environment_id):
        self.build_and_send_agent(environment_id, RandomAgent)
