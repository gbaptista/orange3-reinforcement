from Orange.widgets.tests.base import WidgetTest

from ..agents.random.random_agent import RandomAgent

from ..ow_trainer import OWTrainer


class TestOWTrainer(WidgetTest):

    def setUp(self):
        self.widget = self.create_widget(OWTrainer)

    def test_output_signal(self):
        agent = RandomAgent('CartPole-v1')

        self.send_signal("Agent", agent)

        assert self.widget.agent is not None
