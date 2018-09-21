from time import sleep

import numpy as np

from ..agent import Agent


class QLearningAgent(Agent):
    name = 'Q-learning Agent'

    gamma = 0.95
    learning_rate = 0.9

    def __init__(self, enviroment_id, ow_widget):
        super().__init__(enviroment_id, ow_widget)

        self.number_of_states = self.enviroment.observation_space.n
        self.number_of_actions = self.enviroment.action_space.n

        self.q_table = np.zeros([self.number_of_states,
                                 self.number_of_actions])

    def train_episode(self):
        done = False

        steps_to_finish = 0
        total_reward = 0

        state = self.enviroment.reset()

        while not done:

            random_values = (self.q_table[state]
                             + np.random.rand(1, self.number_of_actions)
                             / 1000)

            action = np.argmax(random_values, 1)[0]

            new_state, reward, done, _info = self.enviroment.step(action)

            # max = np.max(self.q_table[new_state])
            #
            # self.q_table[state, action] = ((1 - self.learning_rate)
            #                                * self.q_table[state, action]
            #                                + self.learning_rate
            #                                * (reward
            #                                   + self.gamma
            #                                   * max))

            self.q_table[state, action] = (reward
                                           + self.gamma
                                           * np.max(self.q_table[new_state]))

            state = new_state

            steps_to_finish += 1
            total_reward += reward

        return {'steps_to_finish': steps_to_finish,
                'total_reward': total_reward}

    def play_task(self):
        self.enviroment.reset()
        self.enviroment.render()

        self.playing = True

        while self.playing:
            action = self.enviroment.action_space.sample()

            # TODO: Slider
            sleep(0.04)

            _new_state, _reward, done, _info = self.enviroment.step(action)

            self.enviroment.render()

            if done:
                # TODO: Slider
                sleep(0.5)
                self.enviroment.reset()
                self.enviroment.render()

        self.enviroment.close()
