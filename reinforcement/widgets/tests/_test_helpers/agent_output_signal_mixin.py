class AgentOutputSignalMixin:
    def agent_output_signal(self, agent_class):
        input_environment_id = 'FrozenLake-v0'

        assert self.widget.environment_id is None

        self.send_signal("Environment", input_environment_id)

        assert self.widget.environment_id == 'FrozenLake-v0'

        output_agent = self.get_output("Agent")

        assert isinstance(output_agent, agent_class)
