from ...agents.agent_train_mixin import AgentTrainMixin


def test_train():
    class GenericAgent(AgentTrainMixin):
        pass

    generic_agent = GenericAgent()

    assert not generic_agent.train_results
    assert not generic_agent.initial_train_results
    assert generic_agent.trained_episodes == 0
    assert generic_agent.initial_trained_episodes == 0
