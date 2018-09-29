from Orange.widgets import gui


class SlidersWidgetMixin:
    def render_sliders(self, sliders, slider_width=300, seperator_height=10):
        for slider in sliders:
            if 'callback' not in slider:
                slider['callback'] = None

            gui.separator(self.controlArea, 0, seperator_height)

            gui.widgetLabel(self.controlArea, slider['label'])

            gui.hSlider(
                self.controlArea, self, slider['key'],
                minValue=slider['min'], maxValue=slider['max'],
                intOnly=False, ticks=0.01, createLabel=True,
                width=slider_width, step=slider['step'],
                callback=slider['callback'])

        return True
