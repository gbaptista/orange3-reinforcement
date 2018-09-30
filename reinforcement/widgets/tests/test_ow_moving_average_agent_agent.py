from Orange.widgets.tests.base import WidgetTest

from ..agents.moving_average.moving_average_agent import MovingAverageAgent

from ..ow_moving_average_agent import OWMovingAverageAgent

from ._test_helpers.agent_output_signal_mixin import AgentOutputSignalMixin


class TestOWMovingAverageAgent(AgentOutputSignalMixin, WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWMovingAverageAgent)

    def test_output_signal(self):
        self.agent_output_signal(MovingAverageAgent)
