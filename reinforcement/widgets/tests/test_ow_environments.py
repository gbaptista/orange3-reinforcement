from Orange.widgets.tests.base import WidgetTest

from ..ow_environments import OWEnvironments


class TestOWEnvironments(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWEnvironments)

    def test_output_signal(self):
        output_table = self.get_output("Environments")

        assert len(output_table.domain.attributes) == 3
        assert not output_table.domain.class_vars
        assert len(output_table.domain.metas) == 1
