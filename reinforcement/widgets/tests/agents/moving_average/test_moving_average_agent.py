from ....agents.moving_average.moving_average_agent import MovingAverageAgent


def test_train_episode():
    enviroment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(enviroment_id)

    assert moving_average_agent.name == 'Moving Average Agent'

    result_keys = list(moving_average_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish', 'total_reward']


def test_actions():
    enviroment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(enviroment_id)

    state = 0

    number_of_actions = moving_average_agent.enviroment.action_space.n
    possible_actions = range(0, number_of_actions)

    assert moving_average_agent.train_action(state) in possible_actions
    assert moving_average_agent.play_action(state) in possible_actions


def test_process_reward():
    enviroment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(enviroment_id)

    state, action, reward, new_state = (None, 0, 10, None)

    assert moving_average_agent.memory['averages'][action] == 0

    for _i in range(0, moving_average_agent.REWARDS_SAMPLE):
        moving_average_agent.process_reward(state, action, reward, new_state)

    assert moving_average_agent.memory['averages'][action] == 5.0


def test_train_task():
    enviroment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(enviroment_id)

    def on_progress(_self, _progress):
        pass

    def on_finish(_self):
        pass

    moving_average_agent.train_task(10, 0, on_progress, on_finish)

    assert moving_average_agent.memory['averages'].size == 4
