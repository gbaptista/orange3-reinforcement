class AgentOutputSignalMixin:
    def agent_output_signal(self, agent_class):
        input_enviroment_id = 'CartPole-v1'

        assert self.widget.enviroment_id is None

        self.send_signal("Enviroment", input_enviroment_id)

        assert self.widget.enviroment_id == 'CartPole-v1'

        output_agent = self.get_output("Agent")

        assert isinstance(output_agent, agent_class)
