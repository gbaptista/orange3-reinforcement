from Orange.widgets.tests.base import WidgetTest

from ..agents.random.random_agent import RandomAgent

from ..ow_benchmark import OWBenchmark


class TestOWBenchmark(WidgetTest):
    def setUp(self):
        self.widget = self.create_widget(OWBenchmark)

    def test_input_signal(self):
        input_agent_a = RandomAgent('CartPole-v1')
        input_agent_b = RandomAgent('CartPole-v1')

        assert not self.widget.agents

        assert not self.widget.list_box.selectedItems()

        self.send_signal("Agent", input_agent_a, [0])

        assert len(self.widget.agents) == 1

        assert len(self.widget.list_box.selectedItems()) == 1

        self.send_signal("Agent", input_agent_b, [1])

        assert len(self.widget.agents) == 2

        assert len(self.widget.list_box.selectedItems()) == 2

        assert len(self.widget.plot_items) == 2
        assert len(self.widget.plot_areas) == 2
