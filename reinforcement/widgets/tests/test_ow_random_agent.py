from Orange.widgets.tests.base import WidgetTest

from ..agents.random.random_agent import RandomAgent

from ..ow_random_agent import OWRandomAgent

from ._test_helpers.agent_output_signal_mixin import AgentOutputSignalMixin


class TestOWRandomAgent(AgentOutputSignalMixin, WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWRandomAgent)

    def test_output_signal(self):
        self.agent_output_signal(RandomAgent)
