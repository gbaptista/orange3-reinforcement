from Orange.widgets.tests.base import WidgetTest

from ...bases.reinforcement_widget import ReinforcementWidget


class TestReinforcementWidget(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(ReinforcementWidget)

    def test_category(self):
        assert self.widget.category == 'Reinforcement'
