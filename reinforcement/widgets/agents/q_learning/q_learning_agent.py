from copy import deepcopy
import numpy as np

from ..agent import Agent
from ..epsilon_greedy_mixin import EpsilonGreedyMixin


class QLearningAgent(Agent, EpsilonGreedyMixin):
    name = 'Q-learning Agent'

    def __init__(self, environment_id):
        super().__init__(environment_id)

        self.number_of_states = self.environment.observation_space.n
        self.number_of_actions = self.environment.action_space.n
        self.gamma = 0

        self.memory = {}

        self.memory['q_table'] = np.zeros((self.number_of_states,
                                           self.number_of_actions))

        self.initial_memory = deepcopy(self.memory)

    def _best_action(self, state):
        return np.ndarray.argmax(self.memory['q_table'][state])

    def train_action(self, state):
        if self.should_explore():
            return self.action_with_epsilon_greedy_info(
                self.environment.action_space.sample()
            )

        random_values = (self.memory['q_table'][state]
                         + np.random.rand(1, self.number_of_actions)
                         / 1000)

        return self.action_with_epsilon_greedy_info(
            np.ndarray.argmax(random_values)
        )

    def play_action(self, state):
        return self._best_action(state)

    def process_reward(self, state, action, reward, new_state):
        new_state_values = self.memory['q_table'][new_state]

        self.memory['q_table'][state, action] = (reward
                                                 + self.gamma
                                                 * np.max(new_state_values))
