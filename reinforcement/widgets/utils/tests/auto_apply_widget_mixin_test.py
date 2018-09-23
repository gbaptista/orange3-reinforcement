from Orange.widgets.widget import OWWidget

from Orange.widgets.tests.base import WidgetTest

from ..auto_apply_widget_mixin import AutoApplyWidgetMixin


class TestAutoApplyWidgetMixin(WidgetTest):
    def setUp(self):
        class GenericWidget(AutoApplyWidgetMixin, OWWidget):
            pass

        self.widget = self.create_widget(GenericWidget)

    def test_render(self):
        self.widget.render_auto_apply_layout()

        assert not self.widget.outdated_settings
