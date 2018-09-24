from Orange.widgets.widget import OWWidget

from Orange.widgets.tests.base import WidgetTest

from ...utils.sliders_widget_mixin import SlidersWidgetMixin


class TestSlidersWidgetMixin(WidgetTest):
    def setUp(self):
        class GenericWidget(SlidersWidgetMixin, OWWidget):
            setting_example = 1

        self.widget = self.create_widget(GenericWidget)

    def test_render(self):
        sliders = [{'label': 'Episodes:', 'key': 'setting_example',
                    'min': 0, 'max': 999, 'step': 10}]

        assert self.widget.render_sliders(sliders)
