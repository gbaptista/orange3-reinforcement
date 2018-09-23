from functools import partial

import gym

from Orange.widgets.utils.concurrent import ThreadExecutor


class AgentPlayMixin():
    playing = False

    episodes_interval = 0.0
    games_interval = 0.0

    def play(self):
        self._executor = ThreadExecutor()

        self.enviroment = gym.make(self.enviroment_id)

        self._executor.submit(partial(self.play_task))

    def stop(self):
        self.playing = False
