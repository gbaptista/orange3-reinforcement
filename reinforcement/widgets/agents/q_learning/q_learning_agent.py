import numpy as np
from ..agent import Agent


class QLearningAgent(Agent):
    name = 'QLearning Agent'

    def __init__(self, enviroment_id):
        super().__init__(enviroment_id)

        self.number_of_states = self.enviroment.observation_space.n
        self.number_of_actions = self.enviroment.action_space.n
        self.gamma = 1

        self.Q = np.zeros((self.number_of_states, self.number_of_actions))

    def train_episode(self):
        done = False

        steps_to_finish = 0
        total_reward = 0

        state = self.enviroment.reset()

        while not done:
            random_values = self.Q[state] + np.random.rand(1, self.number_of_actions) / 1000

            action = np.ndarray.argmax(random_values)

            new_state, reward, done, _info = self.enviroment.step(action)

            self.Q[state, action] = reward + self.gamma * np.max(self.Q[new_state])

            state = new_state

            steps_to_finish += 1
            total_reward += reward

        return {'steps_to_finish': steps_to_finish,
                'total_reward': total_reward}

    def play_task(self):
        state = self.enviroment.reset()

        self.enviroment.render()

        self.playing = True

        while self.playing:
            action = np.ndarray.argmax(self.Q[state])

            if self.episodes_interval > 0.0:
                sleep(self.episodes_interval)

            new_state, _reward, done, _info = self.enviroment.step(action)

            state = new_state

            self.enviroment.render()

            if done:
                if self.games_interval > 0.0:
                    sleep(self.games_interval)

                state = self.enviroment.reset()
                self.enviroment.render()

        self.enviroment.close()
