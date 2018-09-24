from ...agents.agent_play_mixin import AgentPlayMixin


def test_play():
    class GenericAgent(AgentPlayMixin):
        pass

    generic_agent = GenericAgent()

    assert not generic_agent.playing
    assert generic_agent.episodes_interval == 0.0
    assert generic_agent.games_interval == 0.0
