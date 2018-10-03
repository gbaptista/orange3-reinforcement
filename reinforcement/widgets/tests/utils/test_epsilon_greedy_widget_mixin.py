from Orange.widgets.widget import OWWidget

from Orange.widgets.tests.base import WidgetTest

from ...utils.epsilon_greedy_widget_mixin import EpsilonGreedyWidgetMixin
from ...agents.mean.mean_agent import MeanAgent


class TestAutoApplyWidgetMixin(WidgetTest):
    def setUp(self):
        class GenericWidget(EpsilonGreedyWidgetMixin, OWWidget):
            pass

        self.widget = self.create_widget(GenericWidget)

    def test_render_epsilon_greedy_sliders(self):
        self.widget.setting_epsilon_greedy = 0.8
        self.widget.setting_epsilon_greedy_decay = 0.0

        assert self.widget.render_epsilon_greedy_sliders()

    def test_epsilon_greedy_sliders(self):
        assert len(self.widget.epsilon_greedy_sliders()) == 2

    def test_set_agent_epsilon_greedy_settings(self):
        environment_id = 'FrozenLake-v0'

        self.widget.agent = MeanAgent(environment_id)

        self.widget.setting_epsilon_greedy = 0.8
        self.widget.setting_epsilon_greedy_decay = 0.01

        assert self.widget.agent.epsilon_greedy == 0.0
        assert self.widget.agent.epsilon_greedy_decay == 0.0

        self.widget.set_agent_epsilon_greedy_settings()

        assert self.widget.agent.epsilon_greedy == 0.8
        assert self.widget.agent.epsilon_greedy_decay == 0.01

        self.widget.setting_epsilon_greedy = 0.7
        self.widget.setting_epsilon_greedy_decay = 0.05

        self.widget.epsilon_greedy_settings_changed()

        assert self.widget.agent.epsilon_greedy == 0.7
        assert self.widget.agent.epsilon_greedy_decay == 0.05
