from Orange.widgets.widget import OWWidget

from Orange.widgets.tests.base import WidgetTest

from ...utils.epsilon_greedy_widget_mixin import EpsilonGreedyWidgetMixin


class TestAutoApplyWidgetMixin(WidgetTest):
    def setUp(self):
        class GenericWidget(EpsilonGreedyWidgetMixin, OWWidget):
            pass

        self.widget = self.create_widget(GenericWidget)

    def test_render_epsilon_greedy_sliders(self):
        assert self.widget.render_epsilon_greedy_sliders()
