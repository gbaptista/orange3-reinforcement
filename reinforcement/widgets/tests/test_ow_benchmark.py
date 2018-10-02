from Orange.widgets.tests.base import WidgetTest

from ..agents.random.random_agent import RandomAgent

from ..ow_benchmark import OWBenchmark


class TestOWBenchmark(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWBenchmark)

    def test_input_signal(self):
        input_agent_a = RandomAgent('FrozenLake-v0')
        input_agent_b = RandomAgent('FrozenLake-v0')

        assert not self.widget.agents

        assert not self.widget.list_box.selectedItems()

        self.send_signal("Agent", input_agent_a, [0])

        assert len(self.widget.agents) == 1

        assert len(self.widget.list_box.selectedItems()) == 1

        self.send_signal("Agent", input_agent_b, [1])

        assert len(self.widget.agents) == 2

        assert len(self.widget.list_box.selectedItems()) == 2

        assert len(self.widget.plot_items) == 3
        assert len(self.widget.plot_areas) == 3

    def test_render_agents_lines(self):
        input_agent = RandomAgent('FrozenLake-v0')

        fake_result = {'steps_to_finish': 0,
                       'total_reward': 0,
                       'last_action_info': {'epsilon_greedy': 0}}

        input_agent.train_results = [fake_result, fake_result]

        self.send_signal("Agent", input_agent, [0])

        self.widget.render_plot_views()

        self.widget.render_agents_lines()

        assert len(self.widget.plot_items) == 3

    def test_agent_result_to_line(self):
        input_agent = RandomAgent('FrozenLake-v0')

        def on_progress(_self, _progress):
            pass

        def on_finish(_self):
            pass

        input_agent.train_task(10, 0, on_progress, on_finish)

        assert len(input_agent.train_results) == 10

        train_results_keys = list(input_agent.train_results[1].keys())

        assert train_results_keys == ['steps_to_finish',
                                      'total_reward',
                                      'last_action_info']

        result_line = self.widget.agent_result_to_line(input_agent,
                                                       'total_reward')

        assert list(result_line.keys()) == ['x', 'y']

        assert len(result_line['x']) == 10
        assert len(result_line['y']) == 10
