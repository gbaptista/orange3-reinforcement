import time

from copy import deepcopy
from functools import partial
import numpy as np

from Orange.widgets.utils.concurrent import ThreadExecutor


class AgentTrainMixin():
    train_results = None
    initial_train_results = None

    trained_episodes = 0
    initial_trained_episodes = 0

    memory = None
    initial_memory = None

    _progress = 0

    def train(self, episodes, seconds, ow_widget, ow_widget_on_finish):
        self.ow_widget = ow_widget
        self.ow_widget_on_finish = ow_widget_on_finish

        self._executor = ThreadExecutor()

        self.ow_widget.progressBarInit()

        def on_progress(self, progress):
            self.on_progress(progress)

        def on_finish(self):
            self.on_finish()

        self._executor.submit(partial(self.train_task,
                                      episodes,
                                      seconds,
                                      on_progress,
                                      on_finish))

    def train_episode(self):
        done = False

        steps_to_finish = 0
        total_reward = 0

        state = self.environment.reset()

        while not done:
            # pylint: disable=assignment-from-no-return
            action, action_info = self.train_action(state)

            new_state, reward, done, _info = self.environment.step(action)

            self.process_reward(state, action, reward, new_state)

            state = new_state

            steps_to_finish += 1
            total_reward += reward

        return {'steps_to_finish': steps_to_finish,
                'total_reward': total_reward,
                'last_action_info': action_info}

    def process_reward(self, state, action, reward, new_state):
        pass

    def train_action(self, state):
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

    @staticmethod
    def spend_seconds(started_time):
        return time.time()-started_time

    def has_available_time(self, started_time, seconds):
        return self.spend_seconds(started_time) < seconds

    def current_progress(self, started_time, seconds,
                         episodes, iterations):
        progress = self._progress

        estimated_seconds = seconds

        spend_seconds = self.spend_seconds(started_time)

        if episodes > 0 and spend_seconds > 0:
            iteration_mean_seconds = spend_seconds / iterations
            estimated_seconds += episodes * iteration_mean_seconds

        if estimated_seconds > 0.0:
            progress = (spend_seconds/estimated_seconds) * 100

            if progress >= 100.0:
                progress = 99.999

        return progress

    def update_progress(self):
        self.iterations += 1

        self.on_progress(self,
                         self.current_progress(self.started_time,
                                               self.seconds,
                                               self.episodes,
                                               self.iterations))

        self.trained_episodes += 1

        if not self.has_available_time(self.started_time, self.seconds):
            self.episode += 1

    def should_keep_learning(self):
        return (self.episode <= self.episodes
                or self.has_available_time(self.started_time,
                                           self.seconds))

    def learn_iteration_callback(self):
        if(self.should_keep_learning()):
            # pylint: disable=assignment-from-no-return
            result = self.train_episode()

            self.train_results = np.append(self.train_results, result)

            self.update_progress()

            return False
        else:
            self.on_finish(self)

            return True

    def start_learning(self):
        while(not self.learn_iteration_callback()):
            continue

    def train_task(self, episodes, seconds, on_progress, on_finish):
        self.episodes = episodes
        self.seconds = seconds

        self.on_progress = on_progress
        self.on_finish = on_finish

        self.episode = 1
        self.iterations = 0

        self.started_time = time.time()

        self.trained_episodes = self.initial_trained_episodes
        self.train_results = deepcopy(self.initial_train_results)
        self.memory = deepcopy(self.initial_memory)

        self.start_learning()
