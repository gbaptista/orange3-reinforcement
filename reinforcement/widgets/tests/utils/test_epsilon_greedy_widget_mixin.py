from Orange.widgets.widget import OWWidget

from Orange.widgets.tests.base import WidgetTest

from ...utils.epsilon_greedy_widget_mixin import EpsilonGreedyWidgetMixin


class TestAutoApplyWidgetMixin(WidgetTest):
    def setUp(self):
        class GenericWidget(EpsilonGreedyWidgetMixin, OWWidget):
            pass

        self.widget = self.create_widget(GenericWidget)

    def test_render_epsilon_greedy_sliders(self):

        self.widget.setting_epsilon_greedy = 0.8
        self.widget.setting_epsilon_greedy_decay = 0.0

        assert self.widget.render_epsilon_greedy_sliders()
