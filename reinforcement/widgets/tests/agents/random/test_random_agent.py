from ....agents.random.random_agent import RandomAgent


def test_train_episode():
    enviroment_id = 'CartPole-v1'

    random_agent = RandomAgent(enviroment_id)

    assert random_agent.name == 'Random Agent'
