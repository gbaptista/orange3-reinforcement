import numpy as np


class EpsilonGreedyMixin():
    epsilon_greedy = 0.0
    epsilon_greedy_decay = 0.0

    def should_explore(self):
        return np.random.random() > self.epsilon_greedy
