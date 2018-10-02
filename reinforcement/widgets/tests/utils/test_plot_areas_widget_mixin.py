from Orange.widgets.widget import OWWidget

from Orange.widgets.tests.base import WidgetTest

from ...utils.colors_widget_mixin import ColorsWidgetMixin
from ...utils.plot_areas_widget_mixin import PlotAreasWidgetMixin


class TestPlotAreasWidgetMixin(WidgetTest):
    def setUp(self):
        class GenericWidget(PlotAreasWidgetMixin, ColorsWidgetMixin, OWWidget):
            pass

        self.widget = self.create_widget(GenericWidget)

    def test_render_plot_area(self):
        self.widget.plot_areas = {}
        self.widget.plot_items = {}

        assert not self.widget.plot_areas
        assert not self.widget.plot_items

        self.widget.render_plot_area(0, 'Label X', 'Label Y')

        assert len(self.widget.plot_areas) == 1
        assert len(self.widget.plot_items) == 1

    def test_add_line(self):
        self.widget.plot_areas = {}
        self.widget.plot_items = {}

        self.widget.generate_colors(2)

        self.widget.render_plot_area(0, 'Label X', 'Label Y')

        self.widget.add_line(0, 0, {'x': [0], 'y': [0]})
        self.widget.add_line(0, 1, {'x': [0], 'y': [0]})
