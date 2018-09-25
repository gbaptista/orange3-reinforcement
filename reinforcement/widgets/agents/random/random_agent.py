from time import sleep

from ..agent import Agent


class RandomAgent(Agent):
    name = 'Random Agent'

    def train_episode(self):
        done = False

        _state = self.enviroment.reset()

        steps_to_finish = 0
        total_reward = 0

        while not done:
            action = self.enviroment.action_space.sample()

            _new_state, reward, done, _info = self.enviroment.step(action)

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

            if self.episodes_interval > 0.0:
                sleep(self.episodes_interval)

            _new_state, _reward, done, _info = self.enviroment.step(action)

            self.enviroment.render()

            if done:
                if self.games_interval > 0.0:
                    sleep(self.games_interval)

                self.enviroment.reset()
                self.enviroment.render()

        self.enviroment.close()
