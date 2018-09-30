import numpy as np

from ...agents.epsilon_greedy_mixin import EpsilonGreedyMixin


def test_should_explore():
    class GenericClass(EpsilonGreedyMixin):
        pass

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
