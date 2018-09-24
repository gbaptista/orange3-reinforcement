from Orange.widgets.tests.base import WidgetTest

from ..agents.q_learning.q_learning_agent import QLearningAgent

from ..ow_q_learning_agent import OWQLearningAgent

from ._test_helpers.agent_output_signal_mixin import AgentOutputSignalMixin


class TestOWQLearningAgent(AgentOutputSignalMixin, WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWQLearningAgent)

    def test_output_signal(self):
        self.agent_output_signal(QLearningAgent)
