from Orange.widgets.widget import OWWidget

from Orange.widgets.tests.base import WidgetTest

from ...utils.colors_widget_mixin import ColorsWidgetMixin


class TestColorsWidgetMixin(WidgetTest):
    def setUp(self):
        class GenericWidget(ColorsWidgetMixin, OWWidget):
            pass

        self.widget = self.create_widget(GenericWidget)

    def test_generate_colors(self):
        assert not self.widget.colors

        self.widget.generate_colors(3)

        assert self.widget.colors.number_of_colors == 8
