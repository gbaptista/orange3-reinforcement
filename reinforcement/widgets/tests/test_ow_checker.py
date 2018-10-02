from Orange.widgets.tests.base import WidgetTest

from ..ow_checker import OWChecker


class TestOWChecker(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWChecker)

    def test_input_signal(self):
        input_environment_id = 'FrozenLake-v0'

        assert self.widget.environment_id == 'Not found.'

        self.send_signal("Environment", input_environment_id)

        assert self.widget.environment_id == 'FrozenLake-v0'
