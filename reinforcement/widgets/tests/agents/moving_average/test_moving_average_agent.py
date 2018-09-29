from ....agents.moving_average.moving_average_agent import MovingAverageAgent


def test_train_episode():
    enviroment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(enviroment_id)

    assert moving_average_agent.name == 'Moving Average Agent'

    result_keys = list(moving_average_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish', 'total_reward']
