from Orange.widgets import gui


class SlidersWidgetMixin:
    def render_sliders(self, sliders,
                       slider_width=300,
                       seperator_height=10,
                       label_format=' %d'):
        for slider in sliders:
            if 'callback' not in slider:
                slider['callback'] = None

            if 'label_format' not in slider:
                slider['label_format'] = label_format

            gui.separator(self.controlArea, 0, seperator_height)

            gui.widgetLabel(self.controlArea, slider['label'])

            gui.hSlider(
                self.controlArea, self, slider['key'],
                minValue=slider['min'], maxValue=slider['max'],
                intOnly=False, ticks=0.01, createLabel=True,
                width=slider_width, step=slider['step'],
                labelFormat=slider['label_format'],
                callback=slider['callback'])

        return True
