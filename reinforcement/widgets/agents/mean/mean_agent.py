from copy import deepcopy
import numpy as np

from ..agent import Agent
from ..epsilon_greedy_mixin import EpsilonGreedyMixin


class MeanAgent(Agent, EpsilonGreedyMixin):
    name = 'Mean Agent'

    def __init__(self, environment_id):
        super().__init__(environment_id)

        self.number_of_actions = self.environment.action_space.n

        self.memory = {}

        self.memory['rewards_mean'] = np.zeros(self.number_of_actions)
        self.memory['rewards_count'] = np.zeros(self.number_of_actions)

        self.initial_memory = deepcopy(self.memory)

    def _best_action(self):
        return np.ndarray.argmax(self.memory['rewards_mean'])

    def _action_and_info(self, action):
        if 'epsilon_greedy' in self.memory:
            info = {'epsilon_greedy': self.memory['epsilon_greedy']}
        else:
            info = {'epsilon_greedy': self.epsilon_greedy}

        return (action, info)

    def train_action(self, state):
        if self.should_explore():
            return self._action_and_info(
                self.environment.action_space.sample()
            )

        return self._action_and_info(self._best_action())

    def play_action(self, _state):
        return self._best_action()

    def process_reward(self, _state, action, reward, _new_state):
        self.memory['rewards_count'][action] += 1

        self.memory['rewards_mean'][action] = (
            (1 - 1.0 / self.memory['rewards_count'][action])
            * self.memory['rewards_mean'][action] + 1.0
            / self.memory['rewards_count'][action] * reward
        )
