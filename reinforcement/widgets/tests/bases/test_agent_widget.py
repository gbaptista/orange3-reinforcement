from Orange.widgets.tests.base import WidgetTest

from ...agents.random.random_agent import RandomAgent

from ...bases.agent_widget import AgentWidget


class TestAgentWidget(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(AgentWidget)

    def test_render(self):
        self.widget.build_and_send_agent('FrozenLake-v0', RandomAgent)

        self.widget.apply()
        self.widget.render_layout()

    def test_build_and_send_agent(self):
        assert self.widget.agent is None

        assert self.get_output("Agent") is None

        self.widget.setting_agent_name = None

        self.widget.build_and_send_agent('FrozenLake-v0', RandomAgent)

        assert self.widget.agent is not None

        assert self.widget.agent.name == 'Random Agent'

        assert self.get_output("Agent") is not None
