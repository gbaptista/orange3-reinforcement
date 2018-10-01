from Orange.widgets.settings import Setting

from .sliders_widget_mixin import SlidersWidgetMixin


class EpsilonGreedyWidgetMixin(SlidersWidgetMixin):
    agent = None

    setting_epsilon_greedy = Setting(0.8)
    setting_epsilon_greedy_decay = Setting(0.000)

    def epsilon_greedy_sliders(self):
        return [
            {'label': 'Epsilon greedy:', 'key': 'setting_epsilon_greedy',
             'min': 0.00, 'max': 1.00, 'step': 0.05,
             'label_format': ' %03.2f',
             'callback': self.epsilon_greedy_settings_changed},
            {'label': 'Epsilon Greedy decay:',
             'key': 'setting_epsilon_greedy_decay',
             'min': 0.00000, 'max': 0.00100, 'step': 0.00001,
             'label_format': ' %06.5f',
             'callback': self.epsilon_greedy_settings_changed}]

    def render_epsilon_greedy_sliders(self):
        self.render_sliders(self.epsilon_greedy_sliders())

        return True

    def settings_changed(self):
        pass

    def epsilon_greedy_settings_changed(self):
        self.set_agent_epsilon_greedy_settings()

        self.settings_changed()

    def set_agent_epsilon_greedy_settings(self):
        if self.agent is not None:
            self.agent.epsilon_greedy = self.setting_epsilon_greedy
            self.agent.epsilon_greedy_decay = self.setting_epsilon_greedy_decay
