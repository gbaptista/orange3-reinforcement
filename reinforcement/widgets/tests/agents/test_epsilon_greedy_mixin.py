import numpy as np

from ...agents.epsilon_greedy_mixin import EpsilonGreedyMixin


def test_should_explore():
    class GenericClass(EpsilonGreedyMixin):
        memory = {}

    generic_class = GenericClass()

    generic_class.epsilon_greedy = 1.0

    for _i in range(0, 1000):
        assert not generic_class.should_explore()

    generic_class.epsilon_greedy = 0.5

    should_explore_results = np.empty(0)

    for _i in range(0, 1000):
        should_explore_results = np.append(generic_class.should_explore(),
                                           should_explore_results)

    should_explore_unique_results = np.sort(np.unique(should_explore_results))

    assert np.array_equal(should_explore_unique_results, [0, 1])

    generic_class.epsilon_greedy = 0.0

    for _i in range(0, 1000):
        assert generic_class.should_explore()


def test_current_epsilon_greedy():
    class GenericClass(EpsilonGreedyMixin):
        memory = {}

    generic_class = GenericClass()

    generic_class.epsilon_greedy = 0.0
    generic_class.epsilon_greedy_decay = 0.10

    assert generic_class.current_epsilon_greedy() == 0.0

    for _i in range(0, 9):
        generic_class.current_epsilon_greedy()

    assert format(generic_class.current_epsilon_greedy(), '.1f') == '1.0'

    for _i in range(0, 1000):
        generic_class.current_epsilon_greedy()

    assert generic_class.current_epsilon_greedy() == 1.0
