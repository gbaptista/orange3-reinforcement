from functools import partial

from time import sleep

import gym

from Orange.widgets.utils.concurrent import ThreadExecutor


class AgentPlayMixin():
    playing = False

    episodes_interval = 0.0
    games_interval = 0.0

    def play(self):
        self._executor = ThreadExecutor()

        self.enviroment = gym.make(self.enviroment_id)

        self.playing = True

        state = self.enviroment.reset()

        self.enviroment.render()

        self._executor.submit(partial(self.play_task, state))

    def stop(self):
        self.playing = False

    def play_action(self, state):
        pass

    def play_task(self, state):
        while self.playing:
            # pylint: disable=assignment-from-no-return
            action = self.play_action(state)

            sleep(self.episodes_interval)

            _new_state, _reward, done, _info = self.enviroment.step(action)

            self.enviroment.render()

            if done:
                sleep(self.games_interval)

                state = self.enviroment.reset()

                self.enviroment.render()

        self.enviroment.close()
