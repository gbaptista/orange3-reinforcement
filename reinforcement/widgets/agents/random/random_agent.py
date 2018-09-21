from time import sleep

from ..agent import Agent


class RandomAgent(Agent):
    name = 'Random Agent'

    def train_episode(self):
        done = False

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
