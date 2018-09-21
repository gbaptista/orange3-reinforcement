from functools import partial

import gym

from Orange.widgets.utils.concurrent import ThreadExecutor

from Orange.util import Reprable


class Agent(Reprable):
    enviroment_id = None
    enviroment = None

    train_results = {}

    ow_widget_on_finish = None

    playing = False

    _progress = 0
    _executor = None

    def __init__(self, enviroment_id, ow_widget):
        self.enviroment_id = enviroment_id
        self.ow_widget = ow_widget
        self.enviroment = gym.make(self.enviroment_id)

    def train_episode(self):
        pass

    def on_progress(self, progress):
        progress = int(progress)
        # Performance reasons: only update the
        # progress when is realy necessary.
        if progress != self._progress:
            self._progress = progress
            self.ow_widget.progressBarSet(progress)

    def on_finish(self):
        self.ow_widget.progressBarFinished()
        self.ow_widget_on_finish()

    def train_task(self, episodes, on_progress, on_finish):
        episode = 1

        self.train_results = {}

        while episode <= episodes:
            on_progress(self, (episode/episodes) * 100.0)

            self.enviroment.reset()

            result = self.train_episode()

            self.train_results[episode] = result

            episode += 1

        on_finish(self)

    def play(self):
        self._executor = ThreadExecutor()

        self.enviroment = gym.make(self.enviroment_id)

        self._executor.submit(partial(self.play_task))

    def train(self, episodes, ow_widget_on_finish):
        self.ow_widget_on_finish = ow_widget_on_finish

        self._executor = ThreadExecutor()

        self.ow_widget.progressBarInit()

        def on_progress(self, progress):
            self.on_progress(progress)

        def on_finish(self):
            self.on_finish()

        self._executor.submit(partial(self.train_task,
                                      episodes,
                                      on_progress,
                                      on_finish))
