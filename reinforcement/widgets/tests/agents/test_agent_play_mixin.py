import gym

from ...agents.agent_play_mixin import AgentPlayMixin


class GenericAgent(AgentPlayMixin):
    environment_id = 'FrozenLake-v0'

    environment = gym.make('FrozenLake-v0')

    def play_action(self, _state):
        return 0


def test_play():
    generic_agent = GenericAgent()

    generic_agent.playing = False

    assert not generic_agent.playing

    generic_agent.play()

    assert generic_agent.playing

    generic_agent.playing = False

    assert generic_agent.episodes_interval == 0.0
    assert generic_agent.games_interval == 0.0


def test_stop():
    generic_agent = GenericAgent()

    generic_agent.playing = True

    assert generic_agent.playing

    generic_agent.stop()

    assert not generic_agent.playing


def test_play_task():
    generic_agent = GenericAgent()

    state = 0

    generic_agent.playing = False

    generic_agent.play_task(state)

    assert not generic_agent.playing
