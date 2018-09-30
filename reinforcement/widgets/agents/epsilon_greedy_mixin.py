import numpy as np


class EpsilonGreedyMixin():
    epsilon_greedy = 0.0
    epsilon_greedy_decay = 0.0

    def should_explore(self):
        return np.random.random() > self.current_epsilon_greedy()

    def current_epsilon_greedy(self):
        if self.epsilon_greedy_decay == 0.0:
            return self.epsilon_greedy

        if 'epsilon_greedy' not in self.memory:
            self.memory['epsilon_greedy'] = self.epsilon_greedy

            return self.memory['epsilon_greedy']

        if self.memory['epsilon_greedy'] >= 1.0:
            return self.memory['epsilon_greedy']

        self.memory['epsilon_greedy'] += self.epsilon_greedy_decay

        return self.memory['epsilon_greedy']
