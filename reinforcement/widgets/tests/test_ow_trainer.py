from Orange.widgets.tests.base import WidgetTest

from ..agents.random.random_agent import RandomAgent

from ..ow_trainer import OWTrainer


class TestOWTrainer(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWTrainer)

    def test_input_signal(self):
        input_agent = RandomAgent('FrozenLake-v0')

        assert self.widget.agent is None

        self.send_signal("Agent", input_agent)

        assert self.widget.agent is not None
