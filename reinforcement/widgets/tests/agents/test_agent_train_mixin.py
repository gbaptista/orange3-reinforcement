from ...agents.random.random_agent import RandomAgent

from ...agents.agent_train_mixin import AgentTrainMixin


def test_train():
    class GenericAgent(AgentTrainMixin):
        pass

    generic_agent = GenericAgent()

    assert not generic_agent.train_results
    assert not generic_agent.initial_train_results
    assert generic_agent.trained_episodes == 0
    assert generic_agent.initial_trained_episodes == 0


def test_train_task():
    random_agent = RandomAgent('FrozenLake-v0')

    def on_progress(_self, _progress):
        pass

    def on_finish(_self):
        pass

    random_agent.train_task(10, 0, on_progress, on_finish)

    steps_to_finish_a = list(map(lambda result: result['steps_to_finish'],
                                 random_agent.train_results))

    assert len(random_agent.train_results) == 10
    assert len(steps_to_finish_a) == 10

    random_agent.train_task(10, 0, on_progress, on_finish)

    steps_to_finish_b = list(map(lambda result: result['steps_to_finish'],
                                 random_agent.train_results))

    assert len(random_agent.train_results) == 10
    assert len(steps_to_finish_b) == 10

    assert steps_to_finish_a != steps_to_finish_b
