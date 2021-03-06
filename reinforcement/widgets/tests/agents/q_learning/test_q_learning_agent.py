from ....agents.q_learning.q_learning_agent import QLearningAgent


def test_train_episode():
    environment_id = 'FrozenLake-v0'

    q_learning_agent = QLearningAgent(environment_id)

    assert q_learning_agent.name == 'Q-learning Agent'

    result_keys = list(q_learning_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish',
                           'total_reward',
                           'last_action_info']
