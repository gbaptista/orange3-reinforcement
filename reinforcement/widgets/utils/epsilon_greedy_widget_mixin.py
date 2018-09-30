from Orange.widgets.settings import Setting

from .sliders_widget_mixin import SlidersWidgetMixin


class EpsilonGreedyWidgetMixin(SlidersWidgetMixin):
    setting_epsilon_greedy = Setting(0.8)
    setting_epsilon_greedy_decay = Setting(0.001)

    def epsilon_greedy_sliders(self):
        self.setting_epsilon_greedy = 0.80
        self.setting_epsilon_greedy_decay = 0.001

        return [
            {'label': 'Epsilon greedy:', 'key': 'setting_epsilon_greedy',
             'min': 0.00, 'max': 1.00, 'step': 0.05,
             'callback': self.epsilon_greedy_settings_changed},
            {'label': 'Epsilon Greedy decay:',
             'key': 'setting_epsilon_greedy_decay',
             'min': 0.000, 'max': 0.10, 'step': 0.001,
             'callback': self.epsilon_greedy_settings_changed}]

    def render_epsilon_greedy_sliders(self):
        self.render_sliders(self.epsilon_greedy_sliders())

        return True

    def epsilon_greedy_settings_changed(self):
        pass
