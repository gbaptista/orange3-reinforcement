from copy import deepcopy
import numpy as np

from ..agent import Agent
from ..epsilon_greedy_mixin import EpsilonGreedyMixin


class MovingAverageAgent(Agent, EpsilonGreedyMixin):
    name = 'Moving Average Agent'

    REWARDS_SAMPLE = 500

    def __init__(self, environment_id):
        super().__init__(environment_id)

        self.number_of_actions = self.environment.action_space.n

        self.memory = {}

        self.memory['rewards'] = {}
        self.memory['averages'] = np.zeros(self.number_of_actions)

        for action in range(0, self.number_of_actions):
            self.memory['rewards'][action] = np.empty(0)

        self.initial_memory = deepcopy(self.memory)

    def _best_action(self):
        return np.ndarray.argmax(self.memory['averages'])

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
        self.memory['rewards'][action] = np.append(
            self.memory['rewards'][action], reward
        )

        if self.memory['rewards'][action].size >= self.REWARDS_SAMPLE:
            rewards_size = self.memory['rewards'][action].size
            rewards_sum = np.sum(self.memory['rewards'][action])

            new_average = rewards_sum / rewards_size
            current_average = self.memory['averages'][action]

            updated_average = (new_average + current_average) / 2

            self.memory['averages'][action] = updated_average

            self.memory['rewards'][action] = np.empty(0)
