from Orange.widgets.tests.base import WidgetTest

from ..agents.openai.baselines.dqn.dqn_agent import DQNAgent

from ..ow_dqn_agent import OWDQNAgent

from ._test_helpers.agent_output_signal_mixin import AgentOutputSignalMixin


class TestOWDQNAgent(AgentOutputSignalMixin, WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWDQNAgent)

    def test_output_signal(self):
        assert not self.get_output("Agent")

        self.agent_output_signal(DQNAgent)

        assert self.get_output("Agent")
