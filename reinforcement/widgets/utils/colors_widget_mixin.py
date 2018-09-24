from Orange.widgets.utils import colorpalette, colorbrewer


class ColorsWidgetMixin:
    colors = []

    def generate_colors(self, number_of_colors):
        scheme = colorbrewer.colorSchemes["qualitative"]["Dark2"]
        if number_of_colors > len(scheme):
            scheme = colorpalette.DefaultRGBColors

        self.colors = colorpalette.ColorPaletteGenerator(number_of_colors,
                                                         scheme)
