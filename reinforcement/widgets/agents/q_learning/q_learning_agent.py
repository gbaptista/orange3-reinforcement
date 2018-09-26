import numpy as np
from ..agent import Agent


class QLearningAgent(Agent):
    name = 'QLearning Agent'

    def __init__(self, enviroment_id):
        super().__init__(enviroment_id)

        self.number_of_states = self.enviroment.observation_space.n
        self.number_of_actions = self.enviroment.action_space.n
        self.gamma = 1

        self.q_table = np.zeros((self.number_of_states,
                                 self.number_of_actions))

    def train_action(self, state):
        random_values = (self.q_table[state]
                         + np.random.rand(1, self.number_of_actions)
                         / 1000)

        return np.ndarray.argmax(random_values)

    def process_reward(self, state, action, reward, new_state):
        self.q_table[state, action] = (reward
                                       + self.gamma
                                       * np.max(self.q_table[new_state]))

    def play_action(self, state):
        return np.ndarray.argmax(self.q_table[state])
