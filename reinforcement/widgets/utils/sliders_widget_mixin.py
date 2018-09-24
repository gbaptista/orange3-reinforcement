from Orange.widgets import gui


class SlidersWidgetMixin:
    def render_sliders(self, sliders):
        for slider in sliders:
            if 'callback' not in slider:
                slider['callback'] = None

            gui.separator(self.controlArea, 0, 10)

            gui.widgetLabel(self.controlArea, slider['label'])

            gui.hSlider(
                self.controlArea, self, slider['key'],
                minValue=slider['min'], maxValue=slider['max'],
                intOnly=False, ticks=0.01, createLabel=True, width=300,
                step=slider['step'], callback=slider['callback'])

        return True
