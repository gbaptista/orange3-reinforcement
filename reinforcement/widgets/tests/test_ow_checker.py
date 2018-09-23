from Orange.widgets.tests.base import WidgetTest

from ..ow_checker import OWChecker


class TestOWChecker(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWChecker)

    def test_input_signal(self):
        input_enviroment_id = 'CartPole-v1'

        assert self.widget.enviroment_id == 'Not found.'

        self.send_signal("Enviroment", input_enviroment_id)

        assert self.widget.enviroment_id == 'CartPole-v1'
