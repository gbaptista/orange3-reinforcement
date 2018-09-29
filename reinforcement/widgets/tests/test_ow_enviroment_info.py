from Orange.widgets.tests.base import WidgetTest

from ..ow_enviroment_info import OWEnviromentInfo


class TestOWEnviromentInfo(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWEnviromentInfo)

    def test_input_signal(self):
        input_enviroment_id = 'FrozenLake-v0'

        assert self.widget.enviroment_id == '?'

        self.send_signal("Enviroment", input_enviroment_id)

        assert self.widget.enviroment_id == 'FrozenLake-v0'
        assert str(self.widget.observation_space) == 'Discrete(16)'
        assert str(self.widget.action_space) == 'Discrete(4)'
        assert str(self.widget.reward_range) == '(0, 1)'
        assert self.widget.timestep_limit == 100
        assert self.widget.trials == 100
        assert self.widget.reward_threshold == 0.78
