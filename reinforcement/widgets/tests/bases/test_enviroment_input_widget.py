from Orange.widgets.tests.base import WidgetTest

from ...bases.enviroment_input_widget import EnviromentInputWidget


class TestEnviromentInputWidget(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(EnviromentInputWidget)

    def test_input(self):
        input_enviroment_id = 'CartPole-v1'

        self.send_signal("Enviroment", input_enviroment_id)
