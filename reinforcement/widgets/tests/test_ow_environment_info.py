from Orange.widgets.tests.base import WidgetTest

from ..ow_environment_info import OWEnvironmentInfo


class TestOWEnvironmentInfo(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWEnvironmentInfo)

    def test_gym_registry_by_id(self):
        input_environment_id = 'FrozenLake-v0'

        registry = self.widget.gym_registry_by_id(input_environment_id)

        assert registry.id == input_environment_id

    def test_input_signal(self):
        input_environment_id = 'FrozenLake-v0'

        assert self.widget.environment_id == '?'

        self.send_signal("Environment", input_environment_id)

        assert self.widget.environment_id == 'FrozenLake-v0'
        assert str(self.widget.observation_space) == 'Discrete(16)'
        assert str(self.widget.action_space) == 'Discrete(4)'
        assert str(self.widget.reward_range) == '(0, 1)'
        assert self.widget.timestep_limit == 100
        assert self.widget.trials == 100
        assert self.widget.reward_threshold == 0.78
