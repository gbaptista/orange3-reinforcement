from ....agents.random.random_agent import RandomAgent


def test_train_episode():
    enviroment_id = 'FrozenLake-v0'

    random_agent = RandomAgent(enviroment_id)

    assert random_agent.name == 'Random Agent'

    result_keys = list(random_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish',
                           'total_reward',
                           'last_action_info']
