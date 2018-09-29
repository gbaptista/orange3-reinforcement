from Orange.widgets.tests.base import WidgetTest

from ..agents.random.random_agent import RandomAgent

from ..ow_play import OWPlay


class TestOWPlay(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWPlay)

    def test_input_signal(self):
        input_agent = RandomAgent('FrozenLake-v0')

        assert input_agent.episodes_interval == 0.0
        assert input_agent.games_interval == 0.0

        assert self.widget.agent is None

        self.send_signal("Agent", input_agent)

        assert self.widget.agent is not None

        assert input_agent.episodes_interval == 0.04
        assert input_agent.games_interval == 0.5
