import numpy as np


class EpsilonGreedyMixin():
    epsilon_greedy = 0.0
    epsilon_greedy_decay = 0.0

    def should_explore(self):
        return np.random.random() < self.current_epsilon_greedy()

    def action_with_epsilon_greedy_info(self, action):
        if 'epsilon_greedy' in self.memory:
            info = {'epsilon_greedy': self.memory['epsilon_greedy']}
        else:
            info = {'epsilon_greedy': self.epsilon_greedy}

        return (action, info)

    def current_epsilon_greedy(self):
        if self.epsilon_greedy_decay == 0.0:
            return self.epsilon_greedy

        if 'epsilon_greedy' not in self.memory:
            self.memory['epsilon_greedy'] = self.epsilon_greedy

            return self.memory['epsilon_greedy']

        if self.memory['epsilon_greedy'] <= 0.0:
            return 0.0

        self.memory['epsilon_greedy'] -= self.epsilon_greedy_decay

        return self.memory['epsilon_greedy']
