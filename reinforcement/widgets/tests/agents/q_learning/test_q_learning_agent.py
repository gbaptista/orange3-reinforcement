from Orange.widgets.utils.concurrent import methodinvoke

from ....agents.q_learning.q_learning_agent import QLearningAgent


def test_train_episode():
    enviroment_id = 'FrozenLake-v0'

    q_learning_agent = QLearningAgent(enviroment_id)

    assert q_learning_agent.name == 'QLearning Agent'

    result_keys = list(q_learning_agent.train_episode().keys())

    assert result_keys == ['steps_to_finish', 'total_reward']
