from ....agents.moving_average.moving_average_agent import MovingAverageAgent


def test_train_episode():
    enviroment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(enviroment_id)

    assert moving_average_agent.name == 'Moving Average Agent'

    result_keys = list(moving_average_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish', 'total_reward']


def test_train_task():
    enviroment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(enviroment_id)

    def on_progress(_self, _progress):
        pass

    def on_finish(_self):
        pass

    moving_average_agent.train_task(10, 0, on_progress, on_finish)

    assert moving_average_agent.memory['averages'].size == 4
