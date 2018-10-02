from ...agents.agent import Agent


def test_prepare_to_pickle():
    environment_id = 'FrozenLake-v0'

    agent = Agent(environment_id)

    assert agent.environment
    assert agent.environment_id == environment_id

    agent.ow_widget = True
    agent.ow_widget_on_finish = True

    assert agent.ow_widget
    assert agent.ow_widget_on_finish

    agent.prepare_to_pickle()

    assert not agent.ow_widget
    assert not agent.ow_widget_on_finish
