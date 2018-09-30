from copy import deepcopy
import numpy as np

from ..agent import Agent


class QLearningAgent(Agent):
    name = 'Q-learning Agent'

    def __init__(self, enviroment_id):
        super().__init__(enviroment_id)

        self.number_of_states = self.enviroment.observation_space.n
        self.number_of_actions = self.enviroment.action_space.n
        self.gamma = 1

        self.memory = {}

        self.memory['q_table'] = np.zeros((self.number_of_states,
                                           self.number_of_actions))

        self.initial_memory = deepcopy(self.memory)

    def train_action(self, state):
        random_values = (self.memory['q_table'][state]
                         + np.random.rand(1, self.number_of_actions)
                         / 1000)

        return np.ndarray.argmax(random_values)

    def process_reward(self, state, action, reward, new_state):
        new_state_values = self.memory['q_table'][new_state]

        self.memory['q_table'][state, action] = (reward
                                                 + self.gamma
                                                 * np.max(new_state_values))

    def play_action(self, state):
        return np.ndarray.argmax(self.memory['q_table'][state])
