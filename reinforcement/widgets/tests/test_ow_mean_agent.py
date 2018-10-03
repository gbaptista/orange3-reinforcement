from Orange.widgets.tests.base import WidgetTest

from ..agents.mean.mean_agent import MeanAgent

from ..ow_mean_agent import OWMeanAgent

from ._test_helpers.agent_output_signal_mixin import AgentOutputSignalMixin


class TestOWMeanAgent(AgentOutputSignalMixin, WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWMeanAgent)

    def test_output_signal(self):
        self.agent_output_signal(MeanAgent)
