from Orange.widgets.tests.base import WidgetTest

from ..ow_enviroment_info import OWEnviromentInfo


class TestOWEnviromentInfo(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWEnviromentInfo)

    def test_input_signal(self):
        input_enviroment_id = 'CartPole-v1'

        assert self.widget.enviroment_id == '?'

        self.send_signal("Enviroment", input_enviroment_id)

        assert self.widget.enviroment_id == 'CartPole-v1'
        assert str(self.widget.observation_space) == 'Box(4,)'
        assert str(self.widget.action_space) == 'Discrete(2)'
        assert str(self.widget.reward_range) == '(-inf, inf)'
        assert self.widget.timestep_limit == 500
        assert self.widget.trials == 100
        assert self.widget.reward_threshold == 475.0
