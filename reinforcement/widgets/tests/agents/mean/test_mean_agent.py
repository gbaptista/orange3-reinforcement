from ....agents.mean.mean_agent import MeanAgent


def test_train_episode():
    environment_id = 'FrozenLake-v0'

    mean_agent = MeanAgent(environment_id)

    assert mean_agent.name == 'Mean Agent'

    result_keys = list(mean_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish',
                           'total_reward',
                           'last_action_info']


def test_actions():
    environment_id = 'FrozenLake-v0'

    mean_agent = MeanAgent(environment_id)

    state = 0

    number_of_actions = mean_agent.environment.action_space.n
    possible_actions = range(0, number_of_actions)

    action, action_info = mean_agent.train_action(state)

    assert action in possible_actions
    assert action_info == {'epsilon_greedy': 0.0}

    assert mean_agent.play_action(state) in possible_actions


def test_process_reward():
    environment_id = 'FrozenLake-v0'

    mean_agent = MeanAgent(environment_id)

    state, action, reward, new_state = (None, 0, 10, None)

    assert mean_agent.memory['rewards_count'][action] == 0
    assert mean_agent.memory['rewards_mean'][action] == 0

    for _i in range(0, 10):
        mean_agent.process_reward(state, action, reward, new_state)

    state, action, reward, new_state = (None, 0, 20, None)

    for _i in range(0, 10):
        mean_agent.process_reward(state, action, reward, new_state)

    assert format(mean_agent.memory['rewards_mean'][action], '.1f') == '15.0'


def test_train_task():
    environment_id = 'FrozenLake-v0'

    mean_agent = MeanAgent(environment_id)

    def on_progress(_self, _progress):
        pass

    def on_finish(_self):
        pass

    mean_agent.train_task(10, 0, on_progress, on_finish)

    assert mean_agent.memory['rewards_count'].size == 4
    assert mean_agent.memory['rewards_mean'].size == 4
