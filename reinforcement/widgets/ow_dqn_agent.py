from .bases.agent_widget import AgentWidget

from .agents.openai.baselines.dqn.dqn_agent import DQNAgent


class OWDQNAgent(AgentWidget):
    id = "orange.widgets.reinforcement.dqn_agent"
    name = "DQN Agent (OpenAI Baselines)"
    description = """DQN Agent."""
    icon = "icons/dqn_agent_icon_1.svg"

    def set_environment_id(self, environment_id):
        self.build_and_send_agent(environment_id, DQNAgent)
