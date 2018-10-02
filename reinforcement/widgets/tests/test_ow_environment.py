from Orange.widgets.tests.base import WidgetTest

from ..ow_environment import OWEnvironment


class TestOWEnvironment(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWEnvironment)

    def test_environments_combo(self):
        output_environment_id = self.get_output("Environment")

        assert output_environment_id == 'FrozenLake-v0'

        assert self.widget.environments_combo.currentText() == 'FrozenLake-v0'

        self.widget.environments_combo.setCurrentIndex(2)

        assert not (self.widget.environments_combo.currentText()
                    == 'FrozenLake-v0')
