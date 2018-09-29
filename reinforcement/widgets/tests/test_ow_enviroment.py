from Orange.widgets.tests.base import WidgetTest

from ..ow_enviroment import OWEnviroment


class TestOWEnviroment(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWEnviroment)

    def test_enviroments_combo(self):
        output_enviroment_id = self.get_output("Enviroment")

        assert output_enviroment_id == 'FrozenLake-v0'

        assert self.widget.enviroments_combo.currentText() == 'FrozenLake-v0'

        self.widget.enviroments_combo.setCurrentIndex(2)

        assert not (self.widget.enviroments_combo.currentText()
                    == 'FrozenLake-v0')
