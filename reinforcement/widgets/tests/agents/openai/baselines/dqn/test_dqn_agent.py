from ......agents.openai.baselines.dqn.dqn_agent import DQNAgent


def test_train_episode():
    assert True
    environment_id = 'FrozenLake-v0'

    dqn_agent = DQNAgent(environment_id)

    dqn_agent.train(10, 0, None, None)

    assert dqn_agent.name == 'DQN Agent (OpenAI Baselines)'
