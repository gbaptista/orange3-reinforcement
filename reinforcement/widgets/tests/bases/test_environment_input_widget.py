from Orange.widgets.tests.base import WidgetTest

from ...bases.environment_input_widget import EnvironmentInputWidget


class TestEnvironmentInputWidget(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(EnvironmentInputWidget)

    def test_input(self):
        input_environment_id = 'FrozenLake-v0'

        self.send_signal("Environment", input_environment_id)
