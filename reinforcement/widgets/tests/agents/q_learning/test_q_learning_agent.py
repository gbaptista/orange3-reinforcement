from ....agents.q_learning.q_learning_agent import QLearningAgent


def test_train_episode():
    enviroment_id = 'CartPole-v1'

    random_agent = QLearningAgent(enviroment_id)

    assert random_agent.name == 'QLearning Agent'
