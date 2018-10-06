from .....agents.openai.baselines.openai_agent import OpenAIAgent


def test_openai_agent():
    environment_id = 'FrozenLake-v0'

    assert OpenAIAgent(environment_id)
