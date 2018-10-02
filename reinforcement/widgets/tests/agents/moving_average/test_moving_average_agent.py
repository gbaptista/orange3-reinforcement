from ....agents.moving_average.moving_average_agent import MovingAverageAgent


def test_train_episode():
    environment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(environment_id)

    assert moving_average_agent.name == 'Moving Average Agent'

    result_keys = list(moving_average_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish',
                           'total_reward',
                           'last_action_info']


def test_actions():
    environment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(environment_id)

    state = 0

    number_of_actions = moving_average_agent.environment.action_space.n
    possible_actions = range(0, number_of_actions)

    action, action_info = moving_average_agent.train_action(state)

    assert action in possible_actions
    assert action_info == {'epsilon_greedy': 0.0}

    assert moving_average_agent.play_action(state) in possible_actions


def test_process_reward():
    environment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(environment_id)

    state, action, reward, new_state = (None, 0, 10, None)

    assert moving_average_agent.memory['averages'][action] == 0

    for _i in range(0, moving_average_agent.REWARDS_SAMPLE):
        moving_average_agent.process_reward(state, action, reward, new_state)

    assert moving_average_agent.memory['averages'][action] == 5.0


def test_train_task():
    environment_id = 'FrozenLake-v0'

    moving_average_agent = MovingAverageAgent(environment_id)

    def on_progress(_self, _progress):
        pass

    def on_finish(_self):
        pass

    moving_average_agent.train_task(10, 0, on_progress, on_finish)

    assert moving_average_agent.memory['averages'].size == 4
